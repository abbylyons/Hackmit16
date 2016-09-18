import eventregistry

from eventregistry import *
er = EventRegistry()
q = QueryEvents()
q.addConcept(er.getConceptUri("Hillary Clinton"))   
q.addRequestedResult(RequestEventsInfo(sortBy = "date", count=100))   # return event details for last 100 events
print er.execQuery(q)