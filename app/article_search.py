import eventregistry
from eventregistry import *
from bs4 import BeautifulSoup

import requests

# Get articles for Shillary
er = EventRegistry()
q = QueryArticles(lang=["eng"])
q.addConcept(er.getConceptUri("Hillary Clinton"))   
q.addRequestedResult(RequestArticlesInfo(sortBy = "date", count=10))   # return event details for last 100 events
results = er.execQuery(q)

for result in results:
	url = result["url"]
	r = requests.get(url)
	data = r.text
	print data


# Get articles for Frump
er = EventRegistry()
q = QueryArticles(lang=["eng"])
q.addConcept(er.getConceptUri("Donald Trump"))   
q.addRequestedResult(RequestArticlesInfo(sortBy = "date", count=10))   # return event details for last 100 events
print er.execQuery(q)