#!/usr/bin/env python

import urllib2
url = 'http://genimondev.uky.edu/API/info/?q={"obj":{"type":"aggregate"},"output":"json","infoType":"simple"}'
f = urllib2.urlopen(url)
all = f.read()
import json

x = json.loads(all)

def getMonVal(obj, field):
    if field in obj:
        return obj[field]
    else:
        return None

def getMonTS(obj, field):
    if field in obj:
        return obj[field] / 1000
    else:
        return 0

for a in x:
    agg_id = getMonVal(a, "id")
    agg_urn = getMonVal(a, "urn")
    ts = getMonTS(a, "ts")
    polled = getMonTS(a, "last_polled_by_collector")
    mapped = getMonTS(a, "last_mapped_by_collector")
    print "\tid: %s" % (agg_id)
    print "\tts: %d" % (ts)
    print "\tpolled: %d" % (polled)
    print "\tmapped: %d" % (mapped)
    print "\tpoll gap: %s" % (abs(ts - polled))
    print "\tmapped gap: %s" % (abs(ts - mapped))


# a = x[10]
# print json.dumps(a, indent=4)

# {
#     "last_polled_by_collector": 1456335973000, 
#     "selfRef": "https://www.geni.uchicago.edu:5001/info/aggregate/uchicago-ig", 
#     "amtype": "instageni", 
#     "urn": "urn:publicid:IDN+geni.uchicago.edu+authority+cm", 
#     "amwikipage": "http://groups.geni.net/geni/wiki/GeniAggregate/ChicagoInstaGENI", 
#     "measRef": "https://www.geni.uchicago.edu:5001/data/", 
#     "ts": 1456335983000, 
#     "schemaVersion": "http://www.gpolab.bbn.com/monitoring/schema/20140828/aggregate#", 
#     "monitoringVersion": "v2.0", 
#     "last_mapped_by_collector": 1456336101000, 
#     "opsConfig": {
#         "collector_internal_id": "2117c661-d7a3-41b4-9291-908eb5efb417", 
#         "href": "https://opsconfigdatastore.gpolab.bbn.com/info/opsconfig/geni-prod", 
#         "id": "geni-prod"
#     }, 
#     "collector_internal_id": "1877c03f-0965-4ff2-966a-d0d6d73f8bbc", 
#     "stitching_am": true, 
#     "id": "uchicago-ig", 
#     "operationalStatus": "Development"
# }
