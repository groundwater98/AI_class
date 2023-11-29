
from rdflib.namespace import DC, DCTERMS, DOAP, FOAF, SKOS, OWL
from rdflib.namespace import RDF, RDFS, VOID, XMLNS, XSD
from rdflib import Graph, URIRef, Literal, Namespace
from rdflib.namespace import RDFS, XSD

g = Graph()

g.bind("foaf", FOAF)
g.bind("xsd", XSD)

ns = Namespace('http://ailab.inha.ac.kr/') #----

# subject = URIRef("http://ailab.inha.ac.kr/student/HongMD")
subject = URIRef("student/HongMD", ns) #----
g.add((subject, FOAF.givenName, Literal("HongMD", datatype=XSD.string)))
g.add((subject, RDF.type, FOAF.Person)) #----
g.add((subject, FOAF.nick, Literal("RedCarrot"))) #----
g.add((subject, FOAF.mbox, Literal("hong@gmail.com", datatype=XSD.anyURI))) #----
g.add((subject, URIRef("skill", ns), Literal("AI", datatype=XSD.string))) #----
g.add((subject, URIRef("skill", ns), Literal("DB", datatype=XSD.string))) #----

subject2 = URIRef("professor/JoGS", ns) #----
g.add((subject2, RDF.type, FOAF.Person)) #----

g.add((subject, FOAF.knows, subject2)) #----

g.serialize(destination="person.ttl") #----

print(g.serialize(format="turtle"))
