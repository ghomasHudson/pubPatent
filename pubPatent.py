from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("http://gov.tso.co.uk/patents/sparql")
sparql.setQuery("""
    PREFIX research: <http://research.data.gov.uk/def/project/>
PREFIX geo: <http://www.w3.org/2003/01/geo/wgs84_pos#>
PREFIX patents: <http://patents.data.gov.uk/def/patents/>
PREFIX dcterms: <http://purl.org/dc/terms/>
SELECT ?patents  ?filingDate ?postcode ?long ?lat ?subject WHERE {
 	  ?patents patents:applicant ?applicant ;
	   dcterms:subject ?subject ;
	   patents:filingDate ?filingDate .
	   ?applicant research:location ?location .
	   ?location research:postcode ?postcode ;
	   geo:long ?long ;
	   geo:lat ?lat .
}
""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

latLongs = []

for result in results["results"]["bindings"]:
    latLongs.append((result["lat"]["value"],result["long"]["value"]))

print(latLongs)