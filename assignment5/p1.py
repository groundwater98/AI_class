from rdflib import Graph
g = Graph()
g.parse('https://dbpedia.org/resource/Incheon')

print(f"Graph g has {len(g)} statements.")

for s, p, o in g:
    print(s, p, o)
# print(g.serialize(format="turtle"))


# https://dbpedia.org/page/Incheon

# https://dbpedia.org/page/Semantic_Web
# http://dbpedia.org/resource/Semantic_Web

