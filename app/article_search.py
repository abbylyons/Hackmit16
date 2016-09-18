import eventregistry
from eventregistry import *
from bs4 import BeautifulSoup
import lxml
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

start = unicode(date.today() + timedelta(-3))
end = unicode(date.today())

# Get articles for Shillary
def hillaryArticles():
	er = EventRegistry()
	q = QueryArticles(lang=["eng"], dateStart = unicode(start), dateEnd = unicode(end))
	q.addConcept(er.getConceptUri("Hillary Clinton"))   
	q.addRequestedResult(RequestArticlesInfo())
	results = (er.execQuery(q))['articles']['results']
	return results

def searchHillaryArticles(query,results):
	iteration = 0
	queryCount = 0
	for result in results:
		if iteration > 50
			break
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

		++iteration

		# look for query
		if query in text:
			++queryCount
	return queryCount

# Get articles for Frump
def trumpArticles():
	er = EventRegistry()
	q = QueryArticles(lang=["eng"], dateStart = unicode(start), dateEnd = unicode(end))
	q.addConcept(er.getConceptUri("Donald Trump"))   
	q.addRequestedResult(RequestArticlesInfo())
	results = (er.execQuery(q))['articles']['results']
	return results

def searchTrumpArticles(query,results):
	iteration = 0
	queryCount = 0
	for result in results:
		if iteration > 50
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

		++iteration

		# look for query
		if query in text:
			++queryCount
	return queryCount

if __name__ == "__main__":
	hillary_articles = hillaryArticles()
	trump_articles = trumpArticles()
    print searchHillaryArticles("gun",hillary_articles)
    print searchTrumpArticles("gun",trump_articles)

    # prints number of articles in past 3 days about both presidential candidates
    print len(hillary_articles)
    print len(trump_articles)

####################


start = unicode(date.today() + timedelta(-30))

er = EventRegistry()
q = GetCounts(er.getConceptUri("Clinton"),
              source = "news",
              startDate = start, endDate = end)
results = er.execQuery(q)

# Determine occurrence of Hillary or Trump in news of period of time
er = EventRegistry()
q = GetCounts(er.getConceptUri("Trump"),
              source = "news",
              startDate = start, endDate = end)
results = er.execQuery(q)



