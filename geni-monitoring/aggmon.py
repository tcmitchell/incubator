#!/usr/bin/env python

# Monitoring API: http://groups.geni.net/geni/wiki/GENIMonitoring/API

import urllib2
import json
import datetime
import time
import pprint

BASE_URL = 'http://genimondev.uky.edu/API'
INFO_URL = '%s/info/' % (BASE_URL)
DATA_URL = '%s/data/' % (BASE_URL)

# TODO: Still need to HTTP encode the resulting query
def buildMonQuery(**kwargs):
    return json.dumps(kwargs, separators=(',', ':'))

def getIsAvailableEvents(agg_list):
    # http://genimondev.uky.edu/API/data/?q={"eventType":["is_available"],"obj":{"id":["max-ig"],"type":"aggregate"},"output":"xml","ts":{"gte":1456345005000,"lt":1456348605000}}
    end = datetime.datetime.utcnow()
    end = datetime.datetime.now()
    start = end - datetime.timedelta(minutes=60)
    end_ts = int(time.mktime(end.timetuple()) * 1000)
    start_ts = int(time.mktime(start.timetuple()) * 1000)
    query = buildMonQuery(eventType=['is_available'],
                          obj={'id':agg_list,
                               'type': 'aggregate'},
                          output='json',
                          ts={'gte':start_ts,
                              'lt':end_ts})
    url = DATA_URL + '?q=' + query
    print url
    f = urllib2.urlopen(url)
    all = f.read()
    try:
        return json.loads(all)
    except:
        raise


# Get a list of aggregates from the monitoring server
url = INFO_URL + '?q={"obj":{"type":"aggregate"},"output":"json","infoType":"simple"}'
f = urllib2.urlopen(url)
all = f.read()
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
    agg_urn = getMonVal(a, "urn")
    # Getting is_available events by URN does not appear to work
    # by_urn = getIsAvailableEvents([agg_urn])
    agg_id = getMonVal(a, "id")
    by_id = getIsAvailableEvents([agg_id])
    #print "By ID:"
    #pprint.pprint(by_id)
    # Data is wrapped in an extra list
    by_id = by_id[0]
    if not by_id:
        print agg_urn
        print "\tNo Data"
        continue
    agg_data = by_id[0]
    ts_data = agg_data['tsdata']
    #print ts_data
    available = False
    available_ts = 0
    for ts in ts_data:
        if ts['ts'] > available_ts:
            available_ts = ts['ts']
            available = ts['v']
    print agg_urn
    pretty_time = time.strftime('%c', time.localtime(available_ts/1000))
    print "\t%s: %r" % (pretty_time, available)

for a in x:
    break
    agg_id = getMonVal(a, "id")
    agg_urn = getMonVal(a, "urn")
    ts = getMonTS(a, "ts")
    polled = getMonTS(a, "last_polled_by_collector")
    mapped = getMonTS(a, "last_mapped_by_collector")
    print "id: %s" % (agg_id)
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
