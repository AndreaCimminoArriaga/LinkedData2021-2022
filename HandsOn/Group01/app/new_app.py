import rdflib
import pandas as pd
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

    SELECT distinct ?station ?address ?numBikes ?distance ?station_id { 
        SERVICE <http://localhost:7200/repositories/app> {
        ?station bMad:id ?station_id .
        ?station geosp:asWKT ?station_position .
        ?station bMad:hasAddress ?address.
        ?station bMad:numBikes ?numBikes.
        BIND( STR("POINT($long$ $lat$)^^geo:wktLiteral") AS ?my_position ) .
        BIND( geof:distance(?station_position, ?my_position, opgs:metre) AS ?distance ) .

    FILTER (?distance < $rad$)
        }
    } 
    ORDER BY DESC(?numBikes) ASC(?distance)
    '''
    query = query.replace('$long$', long)
    query = query.replace('$lat$', lat)
    query = query.replace('$rad$', rad)
    bicis = pd.DataFrame()
    id = []; address_=[];numBikes_=[];distance_=[]
    for row in g.query(query):
        id.append(row.station_id)
        address_.append(row.address)
        numBikes_.append(row.numBikes)
        distance_.append(row.distance)
    bicis['ID'] = id
    bicis['Address'] = address_
    bicis['NumBikes'] = numBikes_
    bicis['Distance'] = distance_
    print(bicis)
        

def find(lat, long):
    g = rdflib.Graph()
    query = """
        PREFIX geosp: <http://www.opengis.net/ont/geosparql#>
        PREFIX opgs: <http://www.opengis.net/def/uom/OGC/1.0/>
        PREFIX geof: <http://www.opengis.net/def/function/geosparql/>
        PREFIX saref: <https://saref.etsi.org/core/>
        PREFIX bMad: <http://app.group01.es/ontology/bicimad#>
        PREFIX geo: <http://www.w3.org/2003/01/geo/wgs84_pos#>

        SELECT distinct ?station_id ?address ?numBikes ?distance { 
            SERVICE <http://localhost:7200/repositories/app> {
                ?station bMad:id ?station_id .
                ?station geosp:asWKT ?station_position .
                ?station bMad:hasAddress ?address .
                ?station bMad:numBikes ?numBikes .
                BIND( STR("POINT($long$ $lat$)^^geo:wktLiteral") AS ?my_position )
                BIND( geof:distance(?station_position, ?my_position, opgs:metre) AS ?distance ) .
            }
        }
        ORDER BY ?distance
        """
    query = query.replace('$long$', long)
    query = query.replace('$lat$', lat)
    bicis = pd.DataFrame()
    id = []; address_=[];numBikes_=[];distance_=[]
    for row in g.query(query):
        id.append(row.station_id)
        address_.append(row.address)
        numBikes_.append(row.numBikes)
        distance_.append(row.distance)
    bicis['ID'] = id
    bicis['Address'] = address_
    bicis['NumBikes'] = numBikes_
    bicis['Distance'] = distance_
    print(bicis)
        
       
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

            SELECT distinct ?station_id ?address ?numBikes { 
                SERVICE <http://localhost:7200/repositories/app> {
                    
                    ?station bMad:id ?station_id .
                    ?station geosp:sfWithin street:$street$.
                    ?station bMad:hasAddress ?address.
                    ?station bMad:numBikes ?numBikes.
                }
            }
            '''
        query = query.replace('$street$',street)
        bicis = pd.DataFrame()
        id = []; address_=[];numBikes_=[]
        for row in g.query(query):
            id.append(row.station_id)
            address_.append(row.address)
            numBikes_.append(row.numBikes)
        bicis['ID'] = id
        bicis['Address'] = address_
        bicis['NumBikes'] = numBikes_
        print(bicis)
        
    else:
        print('The street is not valid')
bimad()