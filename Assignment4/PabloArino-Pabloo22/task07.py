# -*- coding: utf-8 -*-
"""Task07.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tV5j-DRcpPtoJGoMj8v2DSqR_9wyXeiE

**Task 07: Querying RDF(s)**
"""

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
from rdflib.plugins.sparql import prepareQuery

github_storage = "https://raw.githubusercontent.com/AndreaCimminoArriaga/LinkedData2021-2022/main/Assignment4/"

"""Leemos el fichero RDF de la forma que lo hemos venido haciendo"""
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage + "/resources/example6.rdf", format="xml")


NS = Namespace("http://somewhere#")


print('**TASK 7.1: List all subclasses of "Person" with RDFLib and SPARQL**')
print("With SPARQL:")
q1 = prepareQuery('''
  SELECT 
    ?x
  WHERE { 
    ?x rdfs:subClassOf ns:Person. 
  }
  ''', initNs={"rdfs": RDFS, "ns": NS})

for x in g.query(q1):
    print(x[0])

print("With RDFLib:")
for s, p, o in g.triples((None, RDFS.subClassOf, NS.Person)):
    print(s)

print('\n**TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**')
print("With SPARQL:")
q1 = prepareQuery('''
  SELECT DISTINCT
    ?x
  WHERE { 
    {?x a ns:Person. }
    UNION
    {?y rdfs:subClassOf ns:Person .
     ?x a ?y}
  }
  ''', initNs={"rdfs": RDFS, "ns": NS})
for x in g.query(q1):
    print(x[0])

print("With RDFLib:")


for s, p, o in g.triples((None, RDF.type, NS.Person)):
    print(s)

y = [s for s, p, o in g.triples((None, RDFS.subClassOf, NS.Person))]
for subclass in y:
    for s, p, o in g.triples((None, RDF.type, subclass)):
        print(s)

print('\n**TASK 7.3: List all individuals of "Person" and all their properties including their class with RDFLib and '
      'SPARQL**')
print("With SPARQL:")
q1 = prepareQuery('''
  SELECT DISTINCT
    ?individuals ?properties
  WHERE { 
    {?individuals a ns:Person . }
    UNION
    {?y rdfs:subClassOf ns:Person .
     ?individuals a ?y} .
     ?individuals ?p ?properties 
  }
  ''', initNs={"rdfs": RDFS, "ns": NS})
for ind, props in g.query(q1):
    print(ind, props)

print("With RDFLib:")
persons = [s for s, p, o in g.triples((None, RDF.type, NS.Person))]
person_subclasses = [s for s, p, o in g.triples((None, RDFS.subClassOf, NS.Person))]
persons.extend([s for subclass in person_subclasses for s, p, o in g.triples((None, RDF.type, subclass))])

for person in persons:
    for s, p, o in g.triples((person, None, None)):
        print(person, o)
