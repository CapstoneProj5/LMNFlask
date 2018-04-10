
from utils.bit_api_mgr.bit_venue import Venue
from utils.bit_api_mgr.bit_event import Event
from utils.bit_api_mgr.bit_artist import Artist

from json import JSONDecodeError
from logging import Logger

import requests


bid_base_url: str = 'https://rest.bandsintown.com'
bid_api_key: str = '13722599'
log = Logger

JDError = "JSONDecoderError No Match from API for Artist -> {} caused Error during parsing response."


def get_artist_data(artist: str) -> dict or bool(False):

    """
    :param str artist: String used to populate query of Bandsintown /Artist API
    :return: dict or False

    """
    
    url_suffix: str = '/artists/{}?app_id={}'.format(artist, bid_api_key)

    composite_url: str = bid_base_url + url_suffix

    try:
        return requests.get(composite_url).json()  # returns type dict

    except JSONDecodeError:
        log(JDError.format(artist))
        return False


def construct_artist(artist_data: dict) -> Artist or False:

    """
    :param dict artist_data: JSON response from Bandsintown /Artist API
    :return Artist or False

    """

    if (artist_data['id'].replace(" ", "")).strip("") == '' \
    or (artist_data['name'].replace(" ", "")).strip("") == '':
        return False

    else:
        return Artist(artist_data['id'],
                      artist_data['name'],
                      artist_data['url'],
                      artist_data['image_url'],
                      artist_data['thumb_url'],
                      artist_data['facebook_page_url'],
                      artist_data['mbid'],
                      artist_data['tracker_count'],
                      artist_data['upcoming_event_count'])


# def parse_event_venue_data():


def get_events_data(artist: str) -> dict or bool(False):

    """
    :param str artist: String used for query of Bandsintown /Artist/Events API
    :return: dict or False or None

    """

    url_suffix: str = '/artists/{}/events?app_id={}'.format(artist, bid_api_key)
    composite_url: str = bid_base_url + url_suffix

    try:
        events_data: dict = requests.get(composite_url).json()

        if not events_data:
            return False
            # if (Artist) Found and not (Upcoming Event): returns [], as [] == False

        elif "errors" in events_data:
                if events_data['errors'] == ["Unknown Artist"]:
                    return False  # Artist Not Found, returns '{"errors":["Unknown Artist"]}'
        else:
            return events_data

    except JSONDecodeError:
        log(JDError.format(artist))
        return False


def parse_event_list_from_events(events_data: dict) -> [Event]:

    """
    :param dict events_data:
        dict JSON data parsed in to event instances, each stored in a list & list is returned
    :return: [Event]
    """

    return [construct_event(event) for event in events_data]


def parse_venue_list_from_events(events_data: dict) -> [Venue]:

    """
    :param dict events_data:
    :return: [Venue]
    """
    return [construct_venue(event['venue']) for event in events_data]


def construct_event(event_data: dict) -> Event:

    """
    :param  dict event_data:
        dict** of (1) event parsed from Bandsintown /Artist/Events API JSON response data
    :return Event

    """

    return Event(event_data['id'],
                 event_data['artist_id'],
                 event_data['url'],
                 event_data['on_sale_datetime'],
                 event_data['datetime'],
                 event_data['description'],
                 event_data['venue']['name'],
                 event_data['venue']['city'],
                 event_data['venue']['country'],
                 event_data['lineup'])


def construct_venue(venue_data: dict) -> Venue:

    """
    :param dict venue_data: dict of 1+ JSON objects to parse in to Venue objects; from Bandsintown API response
    :return: Venue

    """

    return Venue(venue_data['name'],
                 venue_data['latitude'],
                 venue_data['longitude'],
                 venue_data['city'],
                 venue_data['region'],
                 venue_data['country'])


def clean_venue_list(venue_list: [Venue]) -> [Venue]:

    attr_list = ['name', 'latitude', 'longitude', 'city', 'region', 'country']

    for venue in venue_list:
        for attr in attr_list:
            if venue.__getattribute__(attr).replace(' ', '').strip('') == '':
                    venue.__setattr__(attr, 'N/A')

    return venue_list


def clean_event_list(event_list: [Event]) -> [Event]:

    attr_list = ['event_id', 'artist_id', 'url', 'on_sale_datetime', 'show_time', 'description', 'venue', 'city', 'country', 'lineup']

    for event in event_list:
        for attr in attr_list:
            if attr == 'venue' or attr == 'lineup':
                if not event.__getattribute__(attr):
                    event.__setattr__(attr, 'N/A')
            else:
                if event.__getattribute__(attr).replace(' ', '').strip('') == '':
                    event.__setattr__(attr, 'N/A')

    return event_list


def test_get_artist():

    test_data: dict = get_artist_data('between the buried and me')
    construct_artist(test_data)


def test_get_venues_for_artist():

    for artist in ['muse', 'veil of maya', 'kevin gates', 'larry and his flask']:

        test_event_data = get_events_data(artist)

        for x in clean_event_list(parse_event_list_from_events(test_event_data)):
            print(str(x))

        for x in clean_venue_list(parse_venue_list_from_events(test_event_data)):
            print(str(x))


test_get_venues_for_artist()
