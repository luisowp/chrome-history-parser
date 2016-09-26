#!/usr/bin/env python
#
# Sources:
#   JSON    - http://stackoverflow.com/questions/7771011/parse-json-in-python/17493365#17493365
#   Header  - http://stackoverflow.com/questions/3128669/python-script-header
#   Print   - http://stackoverflow.com/questions/15286401/print-multiple-arguments-in-python
#   Unicdoe - http://stackoverflow.com/questions/9942594/unicodeencodeerror-ascii-codec-cant-encode-character-u-xa0-in-position-20
#   pytz    - http://stackoverflow.com/questions/12589952/convert-microsecond-timestamp-to-datetime-in-python
#           - http://pytz.sourceforge.net/
#   SQLite  - http://sqlitebrowser.org/
#
import json
from pprint import pprint
import pytz
from datetime import datetime, timedelta
from pytz import timezone

device_id = 's1+nCTh9mpzPKzWqPcIxmw\u003d\u003d'
device_id = 's1+nCTh9mpzPKzWqPcIxmw=='
json_file='BrowserHistory.json'
#json_file='BH.json'

with open(json_file) as data_file:
  data = json.load(data_file)

browser_history = data['Browser History']

fmt = '%Y-%m-%d %H:%M'

epoch = datetime(1601, 1, 1)
epoch = datetime(1970, 1, 1)
#epoch = datetime(1970, 1, 1, tzinfo=pytz.UTC)
#epoch = datetime(1970, 1, 1, tzinfo=pytz.timezone('US/Central'))
#microseconds_since_epoch = 13022344559000000
#url_datetime = epoch + timedelta(microseconds=microseconds_since_epoch)
#print url_datetime
central =  timezone('US/Central')

tabs = dict()

for entry in browser_history:
  #if entry['page_transition'] != "LINK":
  if entry['client_id'] == device_id:
    #title = entry['title'].encode('utf-8')
    title = entry['url'].encode('utf-8')
    if title in tabs:
      tabs[title] = tabs[title] + 1
    else:
      tabs[title] = 1
    #print(entry['title'] + '\t' + entry['url'])
    #print entry['time_usec'],
#    url_datetime = epoch + timedelta(microseconds=entry['time_usec'])
    #print url_datetime.as_timezone(timezone('US/Central')),
    #print central.localize(url_datetime),
#    print((url_datetime + timedelta(hours=-5)).strftime(fmt)),
    #print str(url_datetime + timedelta(hours=-5)),
#    print entry['title'].encode('utf-8')
    #print entry['url'].encode('utf-8')

#print tabs

for title, count in tabs.items():
  if count > 1:
    print count,
    print title

#print browser_history

#for entry in data:
#  print entry

#pprint(data)
#print data
