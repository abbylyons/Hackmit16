import eventregistry
from eventregistry import *
from bs4 import BeautifulSoup
import json
import requests
from datetime import date
from datetime import timedelta

##### Hillary/Trump/Query related articles #####

start = unicode(date.today() + timedelta(-3))
end = unicode(date.today())

# Get articles for Shillary
def hillaryArticles(query):
	er = EventRegistry()
	q = QueryArticles(lang=["eng"], dateStart = unicode(start), dateEnd = unicode(end))
	q.addConcept(er.getConceptUri("Hillary Clinton"))   
	q.addRequestedResult(RequestArticlesInfo(count=20))
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
		if text.find(query):
			queryCount += 1

	return queryCount

# Get articles for Frump
def trumpArticles(query):
	er = EventRegistry()
	q = QueryArticles(lang=["eng"], dateStart = unicode(start), dateEnd = unicode(end))
	q.addConcept(er.getConceptUri("Donald Trump"))   
	q.addRequestedResult(RequestArticlesInfo(count=20))
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
		if text.find(query):
			queryCount += 1

	return queryCount

####################

# Determine occurrence of Hillary or Trump in news of period of time

start = unicode(date.today() + timedelta(-30))

def hillaryViews():
	er = EventRegistry()
	q = GetCounts(er.getConceptUri("Clinton"),
	              source = "news",
	              startDate = start, endDate = end)
	counts = []
	results = (er.execQuery(q))['http://en.wikipedia.org/wiki/Hillary_Rodham_Clinton']
	for res in results:
		counts.append(res['count'])
	return counts

def trumpViews():
	er = EventRegistry()
	q = GetCounts(er.getConceptUri("Trump"),
	              source = "news",
	              startDate = start, endDate = end)
	counts = []
	results = (er.execQuery(q))['http://en.wikipedia.org/wiki/Donald_Trump']
	for res in results:
		counts.append(res['count'])
	return counts


if __name__ == "__main__":
    print hillaryArticles("candidate")
    print trumpArticles("candidate")
    print hillaryViews()
    print trumpViews()

