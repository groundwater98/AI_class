
from rdflib.namespace import DC, DCTERMS, DOAP, FOAF, SKOS, OWL
from rdflib.namespace import RDF, RDFS, VOID, XMLNS, XSD
from rdflib import Graph, URIRef, Literal, Namespace
from rdflib.namespace import RDFS, XSD

g = Graph()

g.bind("foaf", FOAF)
g.bind("xsd", XSD)

g.add((
    URIRef("http://ailab.inha.ac.kr/student/HongMD"),
    FOAF.givenName,
    Literal("HongMD", datatype=XSD.string)
))

print(g.serialize(format="turtle"))
