import ipgetter
import requests
import os


sk_api_key = os.getenv('SK_API_KEY')
search_venues_endpoint = "http://bit_api_mgr.songkick.com/bit_api_mgr/3.0/search/venues.json?query={}&apikey={}"
search_artists_endpoint = "http://bit_api_mgr.songkick.com/bit_api_mgr/3.0/search/artists.json?apikey={}&query={}"
search_artist_events_endpoint = "http://bit_api_mgr.songkick.com/bit_api_mgr/3.0/artists/{}/calendar.json?apikey={}"
search_venue_events_endpoint = "http://bit_api_mgr.songkick.com/bit_api_mgr/3.0/venues/{}/calendar.json?apikey={}"
search_events_loc_ip_endpoint = "http://bit_api_mgr.songkick.com/bit_api_mgr/3.0/events.json?apikey={}&location=ip:{}"


def search_events_by_ip_location():

    ip = ipgetter.myip()

    response = requests.get(search_events_loc_ip_endpoint.format(sk_api_key, ip)).json()
    event_dict_list = response['resultsPage']['results']['event']
    return event_dict_list


def search_venues_by_name(venue_name: str) -> list:

    response = requests.get(search_venues_endpoint.format(venue_name, sk_api_key)).json()
    venue_dict_list = response['resultsPage']['results']['venue']  # list of dict objects, each dict can be used to build a Venue instance.
    return venue_dict_list


def search_artists_by_name(artist_name: str) -> list:

    response = requests.get(search_artists_endpoint.format(sk_api_key, artist_name)).json()
    artist_dict_list = response['resultsPage']['results']['artist']
    return artist_dict_list


def search_artist_upcoming_events(artist_id: int) -> list:

    response = requests.get(search_artist_events_endpoint.format(artist_id, sk_api_key)).json()
    event_dict_list = response['resultsPage']['results']['event']
    return event_dict_list


def search_venue_upcoming_events(venue_id: int) -> list:

    response = requests.get(search_venue_events_endpoint.format(venue_id, sk_api_key)).json()
    event_dict_list = response['resultsPage']['results']['event']
    return event_dict_list


def get_venue_city_from_venue_data(venue_dict: dict) -> dict:
    city_data = venue_dict['city']
    return city_data


# search_venues_by_name('first avenue and 7th st entry - mainroom')
