from logging import Logger

import requests
import os
import utils.songkick_api.sk_constructor as Constructor
from utils.songkick_api.sk_event import Event

log = Logger
search_ip_endpoint = "http://api.songkick.com/api/3.0/events.json?apikey={}&location=ip:{}"
sk_api_key = os.getenv('SK_API_KEY')


def search_local_events_for_ip(ip_addr: str) -> [dict]:

    response = requests.get(search_ip_endpoint.format(sk_api_key, ip_addr)).json()
    event_dict_list = response['resultsPage']['results']['event']
    return event_dict_list


def get_external_ip():

    ip_address = requests.get('https://api.ipify.org?format=json').json()
    ip = ip_address['ip']
    return ip


def instantiate_events_from_list(event_list: [dict]) -> [Event]:

    if len(event_list) == 0:
        return []
    else:
        events = []
        for event in event_list:
            try:
                new_event = Constructor.build_event(event)
                events.append(new_event)
            except KeyError:
                log('Key not present in event(dict): ' + str(KeyError))
                pass
        return events


def serialize_event_list(event_list):
    events_dict_list = []
    for event in event_list:
        events_dict_list.append(event.__dict__())
    return events_dict_list
