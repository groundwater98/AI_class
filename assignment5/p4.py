from rdflib import Graph

g = Graph()
g.parse("person.ttl")

print(len(g))

print(g.serialize(format="turtle"))
