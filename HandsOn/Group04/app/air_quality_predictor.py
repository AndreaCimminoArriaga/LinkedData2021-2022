from blessed import Terminal
term = Terminal()
print(term.home + term.clear)
print(term.crimson(r'''

              _                              _  _  _                                  _  _        _               
       /\    (_)                            | |(_)| |                                | |(_)      | |              
      /  \    _  _ __    __ _  _   _   __ _ | | _ | |_  _   _   _ __   _ __  ___   __| | _   ___ | |_  ___   _ __ 
     / /\ \  | || '__|  / _` || | | | / _` || || || __|| | | | | '_ \ | '__|/ _ \ / _` || | / __|| __|/ _ \ | '__|
    / ____ \ | || |    | (_| || |_| || (_| || || || |_ | |_| | | |_) || |  |  __/| (_| || || (__ | |_| (_) || |   
   /_/    \_\|_||_|     \__, | \__,_| \__,_||_||_| \__| \__, | | .__/ |_|   \___| \__,_||_| \___| \__|\___/ |_|   
                           | |                           __/ | | |                                                V1.0
                           |_|                          |___/  |_|                                                

  Welcome to Air quality predictor!
  Wait until the program initializes, please.
'''))

print('  [ ' +term.red + term.bold + 'INFO'+term.normal+ ' ] Importing libraries...')

from tqdm import tqdm
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi
from rdflib import Graph, Namespace
from rdflib.namespace import XSD
from rdflib.plugins.sparql import prepareQuery
print('  [  ' +term.green + term.bold + 'OK'+term.normal+ '  ] Libraries imported.')



# FUNCTIONS SECTION

# VORONOI FUNCTION
# https://coderedirect.com/questions/99152/colorize-voronoi-diagram
def voronoi_finite_polygons_2d(vor, radius=None):
    if vor.points.shape[1] != 2:
        raise ValueError("Requires 2D input")

    new_regions = []
    new_vertices = vor.vertices.tolist()

    center = vor.points.mean(axis=0)
    if radius is None:
        radius = vor.points.ptp().max()

    # Construct a map containing all ridges for a given point
    all_ridges = {}
    for (p1, p2), (v1, v2) in zip(vor.ridge_points, vor.ridge_vertices):
        all_ridges.setdefault(p1, []).append((p2, v1, v2))
        all_ridges.setdefault(p2, []).append((p1, v1, v2))

    # Reconstruct infinite regions
    for p1, region in enumerate(vor.point_region):
        vertices = vor.regions[region]

        if all(v >= 0 for v in vertices):
            # finite region
            new_regions.append(vertices)
            continue

        # reconstruct a non-finite region
        ridges = all_ridges[p1]
        new_region = [v for v in vertices if v >= 0]

        for p2, v1, v2 in ridges:
            if v2 < 0:
                v1, v2 = v2, v1
            if v1 >= 0:
                # finite ridge: already in the region
                continue

            # Compute the missing endpoint of an infinite ridge

            t = vor.points[p2] - vor.points[p1]  # tangent
            t /= np.linalg.norm(t)
            n = np.array([-t[1], t[0]])  # normal

            midpoint = vor.points[[p1, p2]].mean(axis=0)
            direction = np.sign(np.dot(midpoint - center, n)) * n
            far_point = vor.vertices[v2] + direction * radius

            new_region.append(len(new_vertices))
            new_vertices.append(far_point.tolist())

        # sort region counterclockwise
        vs = np.asarray([new_vertices[v] for v in new_region])
        c = vs.mean(axis=0)
        angles = np.arctan2(vs[:, 1] - c[1], vs[:, 0] - c[0])
        new_region = np.array(new_region)[np.argsort(angles)]

        # finish
        new_regions.append(new_region.tolist())

    return new_regions, np.asarray(new_vertices)


# GET COLOR BY RANGE
def color_number(values):
    m = max(values)
    if 0 <= m <= 25:
        return 0
    elif 25 < m <= 50:
        return 1
    elif 50 < m <= 75:
        return 2
    elif 75 < m <= 100:
        return 3
    elif m > 100:
        return 4


# CONVERT TYPES OF DATA
# (NO, PM, 03)
def convert(data):
    NO, PM, O3 = data
    return NO * 0.53, PM, O3 * 0.5


# GET THE MEAN BY YEARS
def get_mean(a, b):
    res = []
    for i, j in zip(a, b):
        if j is None and i is None:
            i, j = 0, 0
        elif i is None:
            i = j
        elif j is None:
            j = i
        res.append((i + j) / 2)
    return tuple(res)


# GET COLOR BY STATION AND YEAR
def get_color(target_day: str, station, g):
    str_day = target_day if int(target_day) >= 10 else '0' + target_day
    q2019 = get_no2_pm10_o3(station, f'2019-12-{str_day}', g)
    q2020 = get_no2_pm10_o3(station, f'2020-12-{str_day}', g)
    value = convert(get_mean(q2019, q2020))
    danger = {0: (121, 188, 106), 1: (187, 207, 76), 2: (238, 194, 11), 3: (242, 147, 5), 4: (232, 65, 11)}
    return tuple((np.array(danger[color_number(value)]) / 255).tolist() + [1.0])


def get_no2_pm10_o3(control_station, date, g):
    # Namespaces
    AQP_DATA = Namespace("http://www.airqualitypredictor.org/data/")
    AQP = Namespace("http://www.airqualitypredictor.org/ontology#")

    query = f"""
            SELECT ?max_PM10 ?max_NO_2 ?max_O_3
            WHERE {"{"}
            {"{"}
                {"{"}
                    ?sub1 a aqp:PM10 .
                    ?sub1 aqp:hasMaxValue ?max_PM10 .
                    ?sub1 aqp:isFrom aqp_data:{control_station} .
                    ?sub1 aqp:atDate ?date1 .
                    FILTER (?date1 = "{date}"^^xsd:date) .
                {"}"}
                UNION
                {"{"}
                    ?sub2 a aqp:NO2 .
                    ?sub2 aqp:hasMaxValue ?max_N0_2 .
                    ?sub2 aqp:isFrom aqp_data:{control_station} .
                    ?sub2 aqp:atDate ?date2 .
                    FILTER(?date2 = "{date}"^^xsd:date) .
                {"}"}
            {"}"}
            UNION 
            {"{"}
                ?sub3 a aqp:O_3 .
                ?sub3 aqp:hasMaxValue ?max_O_3 .
                ?sub3 aqp:isFrom aqp_data:{control_station} .
                ?sub3 aqp:atDate ?date3 .
                FILTER(?date3 = "{date}"^^xsd:date) .
            {"}"}
        {"}"}
            """

    q = prepareQuery(query, initNs={"aqp_data": AQP_DATA,
                                    "aqp": AQP,
                                    "xsd": XSD})

    for no2, pm10, o3 in g.query(q):
        no2 = no2.toPython() if no2 is not None else None
        pm10 = pm10.toPython() if pm10 is not None else None
        o3 = o3.toPython() if o3 is not None else None

        return no2, pm10, o3

    return None, None, None


# MAIN SECTION

def main():
    # Import ontology
    print('  [ ' +term.red + term.bold + 'INFO'+term.normal+ ' ] Importing data...')

    g = Graph()
    g.parse('data/ontology.owl', format='ttl')
    g.parse('data/output-diciembre-utf8.ttl', format='ttl')

    print('  [  ' +term.green + term.bold + 'OK'+term.normal+ '  ] Data imported.')

    # INIT VALUES
    dic = {58: [313, 137], 60: [621, 217], 57: [725, 245], 27: [1021, 333], 55: [1017, 403], 59: [887, 411],
           39: [535, 329], 50: [623, 387], 16: [805, 509], 11: [667, 453], 17: [535, 951], 54: [901, 825],
           40: [757, 755], 36: [781, 659], 56: [517, 769], 18: [465, 725], 47: [629, 703], 24: [411, 607],
           38: [553, 478], 48: [617, 511], 4: [537, 585], 35: [573, 605], 8: [645, 589], 49: [645, 627]}
    points = np.array(list(dic.values()))

    # compute Voronoi tesselation
    vor = Voronoi(points)

    run = True
    while run:
        # Initialize values
        target_day = input('  [ ' +term.red + term.bold + 'INFO'+term.normal+ ' ]  Please, now select the day of december you want to now about> ')

        print('  [ ' +term.red + term.bold + 'INFO'+term.normal+ ' ]  Generating image...')
        # PLOTTING SETTINGS
        regions, vertices = voronoi_finite_polygons_2d(vor)
        fig, ax = plt.subplots()
        fig.canvas.set_window_title('Air quality predictor')
        ax.set_title(f'Contamination forecast on day {target_day}, december of 2021')
        img = plt.imread('images/control_stations_locations.png')
        ax.imshow(img)

        # COLORIZE
        flag = 0
        d = list(dic.keys())
        for region in tqdm(regions):
            polygon = vertices[region]
            plt.fill(*zip(*polygon), alpha=0.5, color=get_color(target_day, d[flag], g), linewidth=2)
            flag += 1

        # PLOTTING SETTINGS
        plt.plot(points[:, 0], points[:, 1], 'ko')
        plt.xlim(0, 1258)
        plt.ylim(1076, 0)
        figure = plt.gcf()
        figure.set_size_inches(8, 6)
        plt.axis('off')
        plt.show()

        print('  [  ' +term.green + term.bold + 'OK'+term.normal+ '  ]  Predict done!')
        if input('  Do you want another predict?(y/n) ') == 'n':
            run = False


if __name__ == '__main__':
    main()
