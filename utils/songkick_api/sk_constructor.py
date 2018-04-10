from utils.songkick_api import sk_query_mgr
from utils.songkick_api.sk_artist import Artist
from utils.songkick_api.sk_city import City
from utils.songkick_api.sk_event import Event
from utils.songkick_api.sk_location import Location
from utils.songkick_api.sk_performance import Performance
from utils.songkick_api.sk_venue import Venue
from LMNFlask import log


def build_artist(artist_data: dict) -> Artist or False:

    try:
        new_artist = Artist(
            artist_data['id'],
            artist_data['displayName'],
            artist_data['uri'],
            artist_data['onTourUntil'])
        return new_artist

    except KeyError:
        log.info('Key not present during Artist instantiation')
        return False


def build_location(location_data: dict) -> Location or False:

    try:
        new_location = Location(
            location_data['city'],
            location_data['lat'],
            location_data['lng'])
        return new_location

    except KeyError:
        log.info('Key not present during Location instantiation')
        return False


def build_event_performance_artist(artist_name: str) -> Artist or False:
    '''
    json from events for artist as event.performance.artist does not have
    a key for onTourUntil (as json from search artist does) so this function takes the provided artist.displayName to query the artist and provide the full data needed to instantiate an Artist.
    '''

    artists_list = sk_query_mgr.search_artists_by_name(artist_name)
    new_artist = build_artist(artists_list[0])
    return new_artist


def build_performance(performance_data: dict) -> Performance or False:

    try:
        new_performance =  Performance(
            build_event_performance_artist(performance_data['artist']['displayName']),
            performance_data['displayName'],
            performance_data['billingIndex'],
            performance_data['id'],
            performance_data['billing'])
        return new_performance

    except KeyError:
        log.info('Key not present during Performance instantiation')
        return False


def build_city(city_data: dict) -> City or False:

    try:
        new_city = City(
            city_data['id'],
            city_data['displayName'],
            str(city_data['uri']),
            city_data['country'])
        return new_city

    except KeyError:
        log.info('Key not present during City instantiation')
        return False


def build_event(event_data: dict) -> Event or False:

    try:
        new_event = Event(
            event_data['id'],
            event_data['type'],
            str(event_data['uri']),
            event_data['displayName'],
            event_data['start'],
            build_event_performances(event_data['performance']),
            build_location(event_data['location']),
            build_artist_event_venue(event_data['venue']['displayName']),
            event_data['status'],
            event_data['popularity'])
        return new_event

    except KeyError:
        log.info('Key not present during Event instantiation')
        return False


def build_artist_event_venue(venue_name: str) -> Venue or False:

    '''
    When searching for upcoming events for an artist, the 'venue' portion of the JSON response is only a portion of what is returned when searchng for a venue by name. This function takes the venue.displayName in the response, calls the API with it, and instantiates a Venue with the response.

    :param venue_name:
    :return:
    '''

    venue_data = sk_query_mgr.search_venues_by_name(venue_name)
    new_venue = build_venue(venue_data[0])
    return new_venue


def build_event_performances(performance_list: list) -> list:
    event_performances = []
    for performance in performance_list:
        new_performance = build_performance(performance)
        event_performances.append(new_performance)

    return event_performances


def build_venue(venue_data: dict) -> Venue or False:
    """

    :param dict venue_data:
    :return:
    """

    try:
        new_venue = Venue(
            venue_data['id'],
            venue_data['displayName'],
            venue_data['city'],
            venue_data['metroArea'],
            venue_data['uri'],
            venue_data['street'],
            venue_data['zip'],
            venue_data['lat'],
            venue_data['lng'],
            venue_data['phone'],
            venue_data['website'],
            venue_data['capacity'],
            venue_data['description'])
        return new_venue

    except KeyError:
        log.info('Key not present during Venue instantiation')
        return False
