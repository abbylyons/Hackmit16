import eventregistry
from eventregistry import *
from bs4 import BeautifulSoup
from json import dumps
import requests
from datetime import date
from datetime import timedelta

##### Hillary/Trump/Query related articles #####

def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif re.match('<!--.*-->', str(element)):
        return False
    return True

start = unicode(date.today() + timedelta(-2))
end = unicode(date.today())

# Get articles for Shillary
def hillaryArticles(query):
	er = EventRegistry()
	q = QueryArticles(lang=["eng"], dateStart = unicode(start), dateEnd = unicode(end))
	q.addConcept(er.getConceptUri("Hillary Clinton"))   
	q.addRequestedResult(RequestArticlesInfo(count=200))
	results = er.execQuery(q)
	for result in results:
		url = result["url"]
		r = urllib.urlopen(url).read()
		soup = BeautifulSoup(r)
		texts = soup.findAll(text=True)
		visible_texts = filter(visible, texts)
		return visible_texts

# Get articles for Frump
def hillaryArticles(query):
	er = EventRegistry()
	q = QueryArticles(lang=["eng"], dateStart = unicode(start), dateEnd = unicode(end))
	q.addConcept(er.getConceptUri("Donald Trump"))   
	q.addRequestedResult(RequestArticlesInfo(count=200))
	results = er.execQuery(q)
	for result in results:
		url = result["url"]
		r = urllib.urlopen(url).read()
		soup = BeautifulSoup(r)
		texts = soup.findAll(text=True)
		visible_texts = filter(visible, texts)
		return visible_texts

if __name__ == "__main__":
    print hillaryArticles("girl scout")
    print trumpArticles("girl scout")

####################

er = EventRegistry()
q = GetCounts(er.getConceptUri("Clinton"),
              source = "news",
              startDate = start, endDate = end)
#print er.execQuery(q)

# Determine occurrence of Hillary or Trump in news of period of time
er = EventRegistry()
q = GetCounts(er.getConceptUri("Trump"),
              source = "news",
              startDate = start, endDate = end)
print er.execQuery(q)


start = unicode(date.today() + timedelta(-3))

# Get most recent articles
er = EventRegistry()
q = QueryEvents(lang=["eng"],dateStart=start,dateEnd=end)
q.addConcept(er.getConceptUri("Hillary Clinton"))
q.addConcept(er.getConceptUri("Donald Trump"))
# return event details for largest 50 events
q.addRequestedResult(RequestEventsInfo(count = 50, sortBy = "size", sortByAsc = False))   
     
# execute the query
print er.execQuery(q)
