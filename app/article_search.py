import eventregistry
from eventregistry import *
from bs4 import BeautifulSoup
import json
import requests
from datetime import date
from datetime import timedelta

##### Hillary/Trump/Query related articles #####

def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif isinstance(element, Comment):
        return False
    return True

start = unicode(date.today() + timedelta(-2))
end = unicode(date.today())

# Get articles for Shillary
def hillaryArticles(query):
	er = EventRegistry()
	q = QueryArticles(lang=["eng"], dateStart = unicode(start), dateEnd = unicode(end))
	q.addConcept(er.getConceptUri("Hillary Clinton"))   
	q.addRequestedResult(RequestArticlesInfo(count=50))
	results = (er.execQuery(q))['articles']['results']
	queryCount = 0
	for result in results:
		# get all the text from the articles
		url = result["url"]
		r = urllib.urlopen(url).read()
		soup = BeautifulSoup(r, "lxml")
		for script in soup(["script", "style"]): 		# kill all script and style elements
			script.extract()
		text = soup.get_text()
		lines = (line.strip() for line in text.splitlines())
		chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
		text = '\n'.join(chunk for chunk in chunks if chunk)

		# look for query
		if query in text:
			++queryCount
	return queryCount

# Get articles for Frump
def trumpArticles(query):
	er = EventRegistry()
	q = QueryArticles(lang=["eng"], dateStart = unicode(start), dateEnd = unicode(end))
	q.addConcept(er.getConceptUri("Donald Trump"))   
	q.addRequestedResult(RequestArticlesInfo(count=50))
	results = (er.execQuery(q))['articles']['results']
	queryCount = 0
	for result in results:
		# get all the text from the articles
		url = result["url"]
		r = urllib.urlopen(url).read()
		soup = BeautifulSoup(r, "lxml")
		for script in soup(["script", "style"]): 		# kill all script and style elements
			script.extract()
		text = soup.get_text()
		lines = (line.strip() for line in text.splitlines())
		chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
		text = '\n'.join(chunk for chunk in chunks if chunk)

		# look for query
		if query in text:
			++queryCount
	return queryCount

if __name__ == "__main__":
    print hillaryArticles("gun")
    print trumpArticles("gun")

####################

er = EventRegistry()
q = GetCounts(er.getConceptUri("Clinton"),
              source = "news",
              startDate = start, endDate = end)
print er.execQuery(q)

# Determine occurrence of Hillary or Trump in news of period of time
er = EventRegistry()
q = GetCounts(er.getConceptUri("Trump"),
              source = "news",
              startDate = start, endDate = end)
print er.execQuery(q)

# Get most recent articles
er = EventRegistry()
q = QueryArticles(lang=["eng"], dateStart = unicode(start), dateEnd = unicode(end))
q.addRequestedResult(RequestArticlesInfo(count=50))   # return event details for last 100 events
results = er.execQuery(q)
print results

query = QueryArticles(keywords = "Hillary Clinton")
corr.loadInputDataWithQuery(query)

conceptInfo = corr.getTopConceptCorrelations(
    conceptType = ["person", "org"],
    exactCount = 10,
    approxCount = 100)
print conceptInfo
