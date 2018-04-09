import requests
from flask import json
import LMNFlask.utils.songkick_api.sk_constructor as constructor



api_key = "io09K9l3ebJxmxe2"

btbam_id = "391106"



test_response = requests.get("http://api.songkick.com/api/3.0/artists/{}/calendar.json?apikey={}".format(btbam_id, api_key)).json()

count = 0


count_2 = 0
event_data = test_response['resultsPage']['results']['event']

#
#
#
# for event in event_data:
#     print(event_data[count_2])
#     print(event_data[count_2]['uri'])
#     count_2 += 1



#print(test_response.keys()) # resultsPage

#print(test_response['resultsPage'].keys()) # status, results, perPage, page, totalEntries

key_list = [key for key in test_response['resultsPage'].keys()]

for key in key_list:
    print (test_response['resultsPage'][key])

print(test_response['resultsPage']['results'].keys())  # event

events_list = test_response['resultsPage']['results']['event'] #

print(events_list[0].keys()) # type, popularity, displayName, status, performance, ageRestriction, start, end, series, uri, id, show
print(events_list[0]['uri'])

for key in events_list[0].keys():
    print('\n')
    print(key)
    print(events_list[0][key])
    print('\n')

new_events_list = []
for event in events_list:
     new_event = constructor.build_event(event)
     new_events_list.append(new_event)

for Event in new_events_list:
     print(Event.__str__())



