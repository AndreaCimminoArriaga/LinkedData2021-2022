import rdflib
def bimad():
    a = input('What are you looking for?')
    if a == 'pos':
        lat = input('Your latitude: ')
        long = input('Your longitude: ')
        rad = input('Do you want a radius? [Y]es or [N]o ')
        if rad == 'Y' or rad == 'y':
            rad = input('Radius in meters: ')
            findRadius(lat, long, rad)
        elif rad == 'N' or rad == 'n':
            find(lat, long)
        
    elif a == 'street':
        street = str(input('Street: '))
        findStreet(street)

def findRadius(lat, long, rad):
    g = rdflib.Graph()
    query = '''
    PREFIX geosp: <http://www.opengis.net/ont/geosparql#>
    PREFIX opgs: <http://www.opengis.net/def/uom/OGC/1.0/>
    PREFIX geof: <http://www.opengis.net/def/function/geosparql/>
    PREFIX saref: <https://saref.etsi.org/core/>
    PREFIX bMad: <http://app.group01.es/ontology/bicimad#>
    PREFIX geo: <http://www.w3.org/2003/01/geo/wgs84_pos#>

    SELECT distinct ?station ?address ?numBikes ?distance { 
        SERVICE <http://localhost:7200/repositories/app> {
        ?station geosp:asWKT ?station_position .
        ?station bMad:hasAddress ?address.
        ?station bMad:numBikes ?numBikes.
        BIND( STR("POINT($long$ $lat$)^^geo:wktLiteral") AS ?my_position )
        BIND( geof:distance(?station_position, ?my_position, opgs:metre) AS ?distance ) .

    FILTER (?distance < $rad$)
        }
    } 
    ORDER BY DESC(?numBikes) ASC(?distance)
    '''
    query = query.replace('$long$', long)
    query = query.replace('$lat$', lat)
    query = query.replace('$rad$', rad)
    for row in g.query(query):
        print(row)

def find(lat, long):
    g = rdflib.Graph()
    query = """
        PREFIX geosp: <http://www.opengis.net/ont/geosparql#>
        PREFIX opgs: <http://www.opengis.net/def/uom/OGC/1.0/>
        PREFIX geof: <http://www.opengis.net/def/function/geosparql/>
        PREFIX saref: <https://saref.etsi.org/core/>
        PREFIX bMad: <http://app.group01.es/ontology/bicimad#>
        PREFIX geo: <http://www.w3.org/2003/01/geo/wgs84_pos#>

        SELECT distinct ?station ?address ?numBikes ?distance { 
            SERVICE <http://localhost:7200/repositories/app> {
                ?station geosp:asWKT ?station_position .
                ?station <http://app.group01.es/ontology/bicimad#hasAddress> ?address .
                ?station bMad:numBikes ?numBikes .
                BIND( STR("POINT($long$ $lat$)^^geo:wktLiteral") AS ?my_position )
                BIND( geof:distance(?station_position, ?my_position, opgs:metre) AS ?distance ) .
            }
        }
        ORDER BY ?distance
        """
    query = query.replace('$long$', long)
    query = query.replace('$lat$', lat)
    
    for row in g.query(query):
        print(row)
    
def existStreet(street):
    g = rdflib.Graph()
    query = '''
        PREFIX geosp: <http://www.opengis.net/ont/geosparql#>
        PREFIX opgs: <http://www.opengis.net/def/uom/OGC/1.0/>
        PREFIX geof: <http://www.opengis.net/def/function/geosparql/>
        PREFIX saref: <https://saref.etsi.org/core/>
        PREFIX bMad: <http://app.group01.es/ontology/bicimad#>
        PREFIX geo: <http://www.w3.org/2003/01/geo/wgs84_pos#>
        PREFIX street: <http://app.group01.es/resource/bicimad/Street/>

        ASK {
            SERVICE <http://localhost:7200/repositories/app> {
            street:$street$ a bMad:Street.
            }
        }
        '''

    query = query.replace('$street$', str(street))
    for i in g.query(query):
        return i
    
    
     # buscar la calle ASK
def findStreet(street):
    if existStreet(street):
        g = rdflib.Graph()
        query = '''
            PREFIX geosp: <http://www.opengis.net/ont/geosparql#>
            PREFIX opgs: <http://www.opengis.net/def/uom/OGC/1.0/>
            PREFIX geof: <http://www.opengis.net/def/function/geosparql/>
            PREFIX saref: <https://saref.etsi.org/core/>
            PREFIX bMad: <http://app.group01.es/ontology/bicimad#>
            PREFIX geo: <http://www.w3.org/2003/01/geo/wgs84_pos#>
            PREFIX street: <http://app.group01.es/resource/bicimad/Street/>

            SELECT distinct ?station ?add ?bikes { 
                SERVICE <http://localhost:7200/repositories/app> {
                    
                    ?station geosp:sfWithin street:$street$.
                    ?station bMad:hasAddress ?add.
                    ?station bMad:numBikes ?bikes.
                }
            }
            '''
        query = query.replace('$street$',street)
        for row in g.query(query):
            print(row)
            
        
    else:
        print('The street is not valid')

bimad()