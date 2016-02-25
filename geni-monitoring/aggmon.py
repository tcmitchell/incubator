#!/usr/bin/env python

# Monitoring API: http://groups.geni.net/geni/wiki/GENIMonitoring/API

import urllib
import urllib2
import json
import datetime
import time
import pprint

BASE_URL = 'http://genimondev.uky.edu/API'
INFO_URL = '%s/info/' % (BASE_URL)
DATA_URL = '%s/data/' % (BASE_URL)

class Aggregate(object):
    """A representation of an aggregate from monitoring data"""
    def __init__(self, data):
        self.data = data

    @property
    def urn(self):
        if 'urn' in self.data:
            return self.data['urn']
        else:
            return None

    @property
    def id(self):
        if 'id' in self.data:
            return self.data['id']
        else:
            return None

    
    
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
    query = urllib.urlencode({'q': query})
    url = DATA_URL + '?' + query
    # print url
    f = urllib2.urlopen(url)
    all = f.read()
    f.close()
    try:
        return json.loads(all)
    except:
        raise


# Get a list of aggregates from the monitoring server
url = INFO_URL + '?q={"obj":{"type":"aggregate"},"output":"json","infoType":"simple"}'
f = urllib2.urlopen(url)
all = f.read()
x = json.loads(all)
f.close()

all_aggs = [Aggregate(agg_data) for agg_data in x]

#print all_aggs

for a in all_aggs:
    event_data = getIsAvailableEvents([a.urn])
    # pprint.pprint(by_urn)

    # Data is wrapped in an extra list
    event_data = event_data[0]
    print a.urn
    if not event_data:
        print "\tNo Data"
        continue
    agg_data = event_data[0]
    ts_data = agg_data['tsdata']
    #print ts_data
    available = False
    available_ts = 0
    for ts in ts_data:
        if ts['ts'] > available_ts:
            available_ts = ts['ts']
            available = ts['v']
    pretty_time = time.strftime('%c', time.localtime(available_ts/1000))
    print "\t%s: %r" % (pretty_time, available)