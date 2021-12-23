#!/usr/bin/env python
# coding: utf-8

# In[2]:


from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
from rdflib.plugins.sparql import prepareQuery


# In[32]:


g = Graph()
g.parse('C:/Users/XDavi/OneDrive/Documentos/Trabajo Web/output.nt')


# In[34]:


def pregunta_1():
    pr = Namespace("http://findmycontainer.es/lcc/ontology/Container#")
    owl = Namespace("http://www.w3.org/2002/07/owl#")
    rdfs = Namespace("http://www.w3.org/2000/01/rdf-schema#")
    q2 = prepareQuery('''
      SELECT
        DISTINCT ?district 
      WHERE {
        ?containerType  pr:isIn ?address.
        ?address pr:isIn ?district.
    }


      ''',
      initNs = {"pr": pr, "owl":owl, "rdfs":rdfs }
    )

    s = g.query(q2)
    for row in s:
        print(f'{row.district}')

def pregunta_2(y):
    if y == '1':
        pr = Namespace("http://findmycontainer.es/lcc/ontology/Container#")
        rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")

        q1 = prepareQuery('''
          SELECT
             ?containerType (COUNT(?containerType) AS ?tipo) 
    
          WHERE {
            ?container  rdf:type ?containerType;
                        pr:isIn ?address.
            ?address pr:isIn <http://findmycontainer.es/lcc/resource/District/Centro>.
          }
          GROUP BY ?containerType
          ''',
          initNs = {"pr": pr, "rdf": rdf}
        )

        s = g.query(q1)
        for row in s:
            print(f'{row.containerType} : {row.tipo}')
    if y == '2':
        pr = Namespace("http://findmycontainer.es/lcc/ontology/Container#")
        rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")

        q1 = prepareQuery('''
          SELECT
             ?containerType (COUNT(?containerType) AS ?tipo) 
    
          WHERE {
            ?container  rdf:type ?containerType;
                        pr:isIn ?address.
            ?address pr:isIn <http://findmycontainer.es/lcc/resource/District/Fuencarral-El%20Pardo>.
          }
          GROUP BY ?containerType
          ''',
          initNs = {"pr": pr, "rdf": rdf}
        )

        s = g.query(q1)
        for row in s:
            print(f'{row.containerType} : {row.tipo}')
    if y == '3':
        pr = Namespace("http://findmycontainer.es/lcc/ontology/Container#")
        rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")

        q1 = prepareQuery('''
          SELECT
             ?containerType (COUNT(?containerType) AS ?tipo) 
    
          WHERE {
            ?container  rdf:type ?containerType;
                        pr:isIn ?address.
            ?address pr:isIn <http://findmycontainer.es/lcc/resource/District/Latina>.
          }
          GROUP BY ?containerType
          ''',
          initNs = {"pr": pr, "rdf": rdf}
        )

        s = g.query(q1)
        for row in s:
            print(f'{row.containerType} : {row.tipo}')
    if y == '4':
        pr = Namespace("http://findmycontainer.es/lcc/ontology/Container#")
        rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")

        q1 = prepareQuery('''
          SELECT
             ?containerType (COUNT(?containerType) AS ?tipo) 
    
          WHERE {
            ?container  rdf:type ?containerType;
                        pr:isIn ?address.
            ?address pr:isIn <http://findmycontainer.es/lcc/resource/District/Chamber%C3%AD>.
          }
          GROUP BY ?containerType
          ''',
          initNs = {"pr": pr, "rdf": rdf}
        )

        s = g.query(q1)
        for row in s:
            print(f'{row.containerType} : {row.tipo}')
    if y == '5':
        pr = Namespace("http://findmycontainer.es/lcc/ontology/Container#")
        rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")

        q1 = prepareQuery('''
          SELECT
             ?containerType (COUNT(?containerType) AS ?tipo) 
    
          WHERE {
            ?container  rdf:type ?containerType;
                        pr:isIn ?address.
            ?address pr:isIn <http://findmycontainer.es/lcc/resource/District/Moncloa-Aravaca>.
          }
          GROUP BY ?containerType
          ''',
          initNs = {"pr": pr, "rdf": rdf}
        )

        s = g.query(q1)
        for row in s:
            print(f'{row.containerType} : {row.tipo}')
    if y == '6':
        pr = Namespace("http://findmycontainer.es/lcc/ontology/Container#")
        rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")

        q1 = prepareQuery('''
          SELECT
             ?containerType (COUNT(?containerType) AS ?tipo) 
    
          WHERE {
            ?container  rdf:type ?containerType;
                        pr:isIn ?address.
            ?address pr:isIn <http://findmycontainer.es/lcc/resource/District/Tetu%C3%A1n>.
          }
          GROUP BY ?containerType
          ''',
          initNs = {"pr": pr, "rdf": rdf}
        )

        s = g.query(q1)
        for row in s:
            print(f'{row.containerType} : {row.tipo}')
    if y == '7':
        pr = Namespace("http://findmycontainer.es/lcc/ontology/Container#")
        rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")

        q1 = prepareQuery('''
          SELECT
             ?containerType (COUNT(?containerType) AS ?tipo) 
    
          WHERE {
            ?container  rdf:type ?containerType;
                        pr:isIn ?address.
            ?address pr:isIn <http://findmycontainer.es/lcc/resource/District/Arganzuela>.
          }
          GROUP BY ?containerType
          ''',
          initNs = {"pr": pr, "rdf": rdf}
        )

        s = g.query(q1)
        for row in s:
            print(f'{row.containerType} : {row.tipo}')
    if y == '8':
        pr = Namespace("http://findmycontainer.es/lcc/ontology/Container#")
        rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")

        q1 = prepareQuery('''
          SELECT
             ?containerType (COUNT(?containerType) AS ?tipo) 
    
          WHERE {
            ?container  rdf:type ?containerType;
                        pr:isIn ?address.
            ?address pr:isIn <http://findmycontainer.es/lcc/resource/District/Barajas>.
          }
          GROUP BY ?containerType
          ''',
          initNs = {"pr": pr, "rdf": rdf}
        )

        s = g.query(q1)
        for row in s:
            print(f'{row.containerType} : {row.tipo}')
    if y == '9':
        pr = Namespace("http://findmycontainer.es/lcc/ontology/Container#")
        rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")

        q1 = prepareQuery('''
          SELECT
             ?containerType (COUNT(?containerType) AS ?tipo) 
    
          WHERE {
            ?container  rdf:type ?containerType;
                        pr:isIn ?address.
            ?address pr:isIn <http://findmycontainer.es/lcc/resource/District/Carabanchel>.
          }
          GROUP BY ?containerType
          ''',
          initNs = {"pr": pr, "rdf": rdf}
        )

        s = g.query(q1)
        for row in s:
            print(f'{row.containerType} : {row.tipo}')
    if y == '10':
        pr = Namespace("http://findmycontainer.es/lcc/ontology/Container#")
        rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")

        q1 = prepareQuery('''
          SELECT
             ?containerType (COUNT(?containerType) AS ?tipo) 
    
          WHERE {
            ?container  rdf:type ?containerType;
                        pr:isIn ?address.
            ?address pr:isIn <http://findmycontainer.es/lcc/resource/District/Chamart%C3%ADn>.
          }
          GROUP BY ?containerType
          ''',
          initNs = {"pr": pr, "rdf": rdf}
        )

        s = g.query(q1)
        for row in s:
            print(f'{row.containerType} : {row.tipo}')
    if y == '11':
        pr = Namespace("http://findmycontainer.es/lcc/ontology/Container#")
        rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")

        q1 = prepareQuery('''
          SELECT
             ?containerType (COUNT(?containerType) AS ?tipo) 
    
          WHERE {
            ?container  rdf:type ?containerType;
                        pr:isIn ?address.
            ?address pr:isIn <http://findmycontainer.es/lcc/resource/District/Ciudad%20Lineal>.
          }
          GROUP BY ?containerType
          ''',
          initNs = {"pr": pr, "rdf": rdf}
        )

        s = g.query(q1)
        for row in s:
            print(f'{row.containerType} : {row.tipo}')
    if y == '12':
        pr = Namespace("http://findmycontainer.es/lcc/ontology/Container#")
        rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")

        q1 = prepareQuery('''
          SELECT
             ?containerType (COUNT(?containerType) AS ?tipo) 
    
          WHERE {
            ?container  rdf:type ?containerType;
                        pr:isIn ?address.
            ?address pr:isIn <http://findmycontainer.es/lcc/resource/District/Hortaleza>.
          }
          GROUP BY ?containerType
          ''',
          initNs = {"pr": pr, "rdf": rdf}
        )

        s = g.query(q1)
        for row in s:
            print(f'{row.containerType} : {row.tipo}')
    if y == '13':
        pr = Namespace("http://findmycontainer.es/lcc/ontology/Container#")
        rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")

        q1 = prepareQuery('''
          SELECT
             ?containerType (COUNT(?containerType) AS ?tipo) 
    
          WHERE {
            ?container  rdf:type ?containerType;
                        pr:isIn ?address.
            ?address pr:isIn <http://findmycontainer.es/lcc/resource/District/Moratalaz>.
          }
          GROUP BY ?containerType
          ''',
          initNs = {"pr": pr, "rdf": rdf}
        )

        s = g.query(q1)
        for row in s:
            print(f'{row.containerType} : {row.tipo}')
    if y == '14':
        pr = Namespace("http://findmycontainer.es/lcc/ontology/Container#")
        rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")

        q1 = prepareQuery('''
          SELECT
             ?containerType (COUNT(?containerType) AS ?tipo) 
    
          WHERE {
            ?container  rdf:type ?containerType;
                        pr:isIn ?address.
            {?address pr:isIn <http://findmycontainer.es/lcc/resource/District/Puente%20de%20Vallecas>.} UNION
            {?address pr:isIn <http://findmycontainer.es/lcc/resource/District/Villa%20Vallecas>.} UNION
            {?address pr:isIn <http://findmycontainer.es/lcc/resource/District/Villa%20de%20Vallecas>.}
          }
          GROUP BY ?containerType
          ''',
          initNs = {"pr": pr, "rdf": rdf}
        )

        s = g.query(q1)
        for row in s:
            print(f'{row.containerType} : {row.tipo}')
    if y == '15':
        pr = Namespace("http://findmycontainer.es/lcc/ontology/Container#")
        rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")

        q1 = prepareQuery('''
          SELECT
             ?containerType (COUNT(?containerType) AS ?tipo) 
    
          WHERE {
            ?container  rdf:type ?containerType;
                        pr:isIn ?address.
            ?address pr:isIn <http://findmycontainer.es/lcc/resource/District/Retiro>.
          }
          GROUP BY ?containerType
          ''',
          initNs = {"pr": pr, "rdf": rdf}
        )

        s = g.query(q1)
        for row in s:
            print(f'{row.containerType} : {row.tipo}')
    if y == '16':
        pr = Namespace("http://findmycontainer.es/lcc/ontology/Container#")
        rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")

        q1 = prepareQuery('''
          SELECT
             ?containerType (COUNT(?containerType) AS ?tipo) 
    
          WHERE {
            ?container  rdf:type ?containerType;
                        pr:isIn ?address.
            ?address pr:isIn <http://findmycontainer.es/lcc/resource/District/Salamanca>.
          }
          GROUP BY ?containerType
          ''',
          initNs = {"pr": pr, "rdf": rdf}
        )

        s = g.query(q1)
        for row in s:
            print(f'{row.containerType} : {row.tipo}')
    if y == '17':
        pr = Namespace("http://findmycontainer.es/lcc/ontology/Container#")
        rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")

        q1 = prepareQuery('''
          SELECT
             ?containerType (COUNT(?containerType) AS ?tipo) 
    
          WHERE {
            ?container  rdf:type ?containerType;
                        pr:isIn ?address.
            ?address pr:isIn <http://findmycontainer.es/lcc/resource/District/San%20Blas>.
          }
          GROUP BY ?containerType
          ''',
          initNs = {"pr": pr, "rdf": rdf}
        )

        s = g.query(q1)
        for row in s:
            print(f'{row.containerType} : {row.tipo}')
    if y == '18':
        pr = Namespace("http://findmycontainer.es/lcc/ontology/Container#")
        rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")

        q1 = prepareQuery('''
          SELECT
             ?containerType (COUNT(?containerType) AS ?tipo) 
    
          WHERE {
            ?container  rdf:type ?containerType;
                        pr:isIn ?address.
            ?address pr:isIn <http://findmycontainer.es/lcc/resource/District/Usera>.
          }
          GROUP BY ?containerType
          ''',
          initNs = {"pr": pr, "rdf": rdf}
        )

        s = g.query(q1)
        for row in s:
            print(f'{row.containerType} : {row.tipo}')
    if y == '19':
        pr = Namespace("http://findmycontainer.es/lcc/ontology/Container#")
        rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")

        q1 = prepareQuery('''
          SELECT
             ?containerType (COUNT(?containerType) AS ?tipo) 
    
          WHERE {
            ?container  rdf:type ?containerType;
                        pr:isIn ?address.
            ?address pr:isIn <http://findmycontainer.es/lcc/resource/District/Vic%C3%A1lvaro>.
          }
          GROUP BY ?containerType
          ''',
          initNs = {"pr": pr, "rdf": rdf}
        )

        s = g.query(q1)
        for row in s:
            print(f'{row.containerType} : {row.tipo}')
    if y == '20':
        pr = Namespace("http://findmycontainer.es/lcc/ontology/Container#")
        rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")

        q1 = prepareQuery('''
          SELECT
             ?containerType (COUNT(?containerType) AS ?tipo) 
    
          WHERE {
            ?container  rdf:type ?containerType;
                        pr:isIn ?address.
            ?address pr:isIn <http://findmycontainer.es/lcc/resource/District/Villaverde>.
          }
          GROUP BY ?containerType
          ''',
          initNs = {"pr": pr, "rdf": rdf}
        )

        s = g.query(q1)
        for row in s:
            print(f'{row.containerType} : {row.tipo}')
'''def pregunta_3(lat,long):
     query = """
        PREFIX geosp: <http://www.opengis.net/ont/geosparql#>
        PREFIX opgs: <http://www.opengis.net/def/uom/OGC/1.0/>
        PREFIX geof: <http://www.opengis.net/def/function/geosparql/>
        PREFIX saref: <https://saref.etsi.org/core/>
        PREFIX bMad: <http://app.group01.es/ontology/bicimad#>
        PREFIX geo: <http://www.w3.org/2003/01/geo/wgs84_pos#>
        SELECT distinct ?container ?addressname ?distance { 
            SERVICE <http://localhost:7200/repositories/app> {
                ?container geosp:hasGeometry sf:Point.
                sf:Point geosp:asWKT ?container_position .
                ?container pr:isIn ?address .
                ?adress pr:hasFullAdress ?addressname .
                BIND( STR("POINT($long$ $lat$)^^geo:wktLiteral") AS ?my_position )
                BIND( geof:distance(?station_position, ?my_position, opgs:metre) AS ?distance ) .
                Filter(?distance < 300)
            }
        }
        ORDER BY ?distance
        """
    query = query.replace('$long$', long)
    query = query.replace('$lat$', lat)

    for row in g.query(query):
        print(row)'''


# ## ¡Binvenido a nuestro APP!  
# En nuestro app puedes consultar información sobre los contenedores de la Comudiad de Madrid.  
# Las preguntas que puedes hacernos son las siguientes:  
# Los distintos distritos que hay: Escriba 1.( Es recomendable para ver si su distrito está incluido.)  
# La distribución de los contenedores en un distrito en concreto: escriba 2  
# Consultar el id de los contenedores que están a menos de 300 metros de distancia respecto a otro contenedor de mismo tipo: escriba 3  

# In[ ]:


x = input('Escoja su opción:')

if x == '1':
     print(pregunta_1())
        
if x == '2':
    print('Centro:1')
    print('Fuencarral-El Pardo:2')
    print('La Latina:3')
    print('Chamberí:4')
    print('Moncloa-Aravaca:5')
    print('Tetuán:6')
    print('Arganzuela:7')
    print('Barajas:8')
    print('Carabanchel:9')
    print('Chamartín:10')
    print('Ciudad Lineal: 11')
    print('Hortaleza:12')
    print('Moratalaz:13')
    print('Vallecas:14')
    print('Retiro:15')
    print('Salamanca:16')
    print('San Blas:17')
    print('Usera:18')
    print('Vicalvaro:19')
    print('Villalba:20')
    y = input('Escoja uno de los anteriores número:')
    print(pregunta_2(y))
if x == '3':
    lat = input('Your latitude: ')
    long = input('Your longitude: ')


# In[ ]:




