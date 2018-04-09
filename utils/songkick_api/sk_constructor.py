from datetime import date

from LMNFlask.utils.songkick_api.sk_artist import Artist
from LMNFlask.utils.songkick_api.sk_city import City
from LMNFlask.utils.songkick_api.sk_event import Event
from LMNFlask.utils.songkick_api.sk_location import Location
from LMNFlask.utils.songkick_api.sk_performance import Performance
from LMNFlask.utils.songkick_api.sk_venue import Venue


def build_artist(artist_data: dict) -> Artist:

    return Artist(

        artist_data['id'],
        artist_data['displayName'],
        str(artist_data['uri']),
        artist_data['identifier'][0]['mbid'],
        artist_data['onTourUntil'])



def build_location(location_data: dict) -> Location:

    return Location(

        location_data['city'],
        location_data['lat'],
        location_data['lng'])



def build_performance(performance_data: dict) -> Performance:

    return Performance(

        [build_artist(act) for act in performance_data],
        performance_data['displayName'],
        performance_data['billingIndex'],
        performance_data['id'],
        performance_data['billing'])



def build_city(city_data: dict) -> City:

    return City(

        city_data['id'],
        city_data['displayName'],
        str(city_data['uri']),
        city_data['country']['displayName'])



def build_event(event_data: dict) -> Event:

    return Event(

        event_data['id'],
        event_data['type'],
        str(event_data['uri']),
        event_data['displayName'],
        event_data['start'],
        build_performance(event_data['performance']),
        build_location(event_data['location']),
        build_venue(event_data['venue']),
        event_data['status'],
        event_data['popularity'])



def build_venue(venue_data: dict) -> Venue:
    """

    :param dict venue_data:
    :return:
    """

    return Venue(

        venue_data['id'],
        venue_data['displayName'],
        str(venue_data['uri']),
        venue_data['metroArea'],
        build_city(venue_data['city']),
        venue_data['street'],
        venue_data['zip'],
        venue_data['lat'],
        venue_data['lng'],
        venue_data['phone'],
        venue_data['website'],
        venue_data['capacity'],
        venue_data['description'])
