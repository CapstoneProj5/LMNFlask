from logging import Logger

import requests
from LMNFlask import log
import utils.songkick_api.sk_constructor as Constructor
from utils.songkick_api.sk_event import Event


search_ip_endpoint = "http://api.songkick.com/api/3.0/events.json?apikey={}&location=ip:{}"
sk_api_key = 'XFK6hX8iZ4LjPg6l'


def search_local_events_for_ip():

    ip = get_external_ip()
    response = requests.get(search_ip_endpoint.format(sk_api_key, ip)).json()
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
        events_list = []
        for event in event_list:
            try:
                new_event = Constructor.build_event(event)
                events_list.append(new_event)
            except KeyError:
                log.info('Key not present in event(dict): ' + str(KeyError))
                pass
        return events_list