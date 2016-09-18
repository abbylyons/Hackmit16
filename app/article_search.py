import eventregistry
from eventregistry import *
from bs4 import BeautifulSoup
from json import dumps
import requests
from datetime import date
from datetime import timedelta

# Get articles for Shillary
er = EventRegistry()
q = QueryArticles(lang=["eng"])
q.addConcept(er.getConceptUri("Hillary Clinton"))   
q.addRequestedResult(RequestArticlesInfo(sortBy = "date", count=10))   # return event details for last 100 events
results = er.execQuery(q)

#for result in results:
#	url = result["url"]
#	r = requests.get(url)
#	data = r.text
#	print data


# Get articles for Frump
er = EventRegistry()
q = QueryArticles(lang=["eng"])
q.addConcept(er.getConceptUri("Donald Trump"))   
q.addRequestedResult(RequestArticlesInfo(sortBy = "date", count=10))   # return event details for last 100 events
print er.execQuery(q)


####################

start = unicode(date.today() + timedelta(-30))
end = unicode(date.today())

# Determine occurrence of Hillary or Trump in news of period of time
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
