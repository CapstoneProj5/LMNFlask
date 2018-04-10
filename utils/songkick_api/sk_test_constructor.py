from utils.songkick_api.sk_artist import Artist
from utils.songkick_api.sk_city import City
from utils.songkick_api.sk_event import Event
from utils.songkick_api.sk_location import Location
from utils.songkick_api.sk_performance import Performance
from utils.songkick_api.sk_venue import Venue
# x

def print_event_arguments(event_data: dict):

    print('\nid: ' + str(event_data['id']))
    print('type: ' + event_data['type'])
    print('URI: ' + str(event_data['uri']))
    print('Name: ' + event_data['displayName'])
    print('date: ' + str(event_data['start']['date']))
    print('\nperformance list: ' + str((event_data['performance'])))
    print('\n location data: ')
    print('\tlocation city: ' + event_data['location']['city'])
    print('\tlocation lng: ' + str(event_data['location']['lng']))
    print('\tlocation lat: ' + str(event_data['location']['lat']))
    print('\nvenue data:')
    print('\tvenue id: ' + str(event_data['venue']['id']))
    print('\tvenue displayName: ' + event_data['venue']['displayName'])
    print('\tvenue uri: ' + str(event_data['venue']['uri']))
    print('\tvenue lng: ' + str(event_data['venue']['lng']))
    print('\tvenue lat: ' + str(event_data['venue']['lat']))
    print('\tvenue metroArea.keys(): ' + ', '.join([key for key in event_data['venue']['metroArea'].keys()]))
    print('\nevent status: ' + event_data['status'])
    print('event popularity: ' + str(event_data['popularity']))

