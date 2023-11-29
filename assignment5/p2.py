from rdflib import Graph
g = Graph().parse('https://dbpedia.org/resource/Incheon')

q = """
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX dc: <http://purl.org/dc/elements/1.1/>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    PREFIX foaf: <http://xmlns.com/foaf/0.1/>    
    PREFIX dbo: <http://dbpedia.org/ontology/>
    PREFIX dbr: <http://dbpedia.org/resource/>
    
    SELECT ?s ?p ?o
    WHERE {
        ?s ?p ?o.
    }
    LIMIT 100
"""

for r in g.query(q):
    print(r["p"], r["o"])

# dbo:subdivision 