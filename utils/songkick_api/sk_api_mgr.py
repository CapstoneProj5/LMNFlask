
import utils.songkick_api.sk_constructor as constructor
import utils.songkick_api.sk_query_mgr as query_mgr
from utils.songkick_api.sk_artist import Artist
from utils.songkick_api.sk_event import Event
from utils.songkick_api.sk_venue import Venue

api_key = "io09K9l3ebJxmxe2"

test_venue_name = 'First Avenue and 7th St Entry - Mainroom'
test_artist_id_1 = 1091625  # btbam
test_artist_id_2 = 391106  # Larry and His Flask
test_venue_id_1 = 28708  # First Avenue and 7th St Entry - Mainroom
test_venue_id_2 = 1901833  # Icehouse
test_artist_name_1 = 'third'


def search_for_artist(artist_name: str) -> [Artist]:

    matching_artist_dict_list = query_mgr.search_artists_by_name(artist_name)
    if len(matching_artist_dict_list) == 0:
        return []
    else:
        artist_list = instantiate_artists_from_list(matching_artist_dict_list)
        return artist_list

        # TODO as multiple artists may be returned: let user select from response
        #   ***this counter-point functionality should be placed in the web-app***
        #
        #   TL;DR: if len(list) != 0 and len(list) > 0: present each Artist.name to user for selecting target Artist
        #
        # 1) create dictionary keys = Artist.displayName
        # 2) create dictionary values = {'id': Artist.sk_id, 'uri': Artist.uri}
        #
        #         **uri added in the case of wanting to present user with artist page to verify correct Artist
        #         example: Artist.displayName: {'id': Artist.sk_id, 'uri': Artist.uri}
        #
        # 3) create a list of each dictionary
        #
        #  Artist_Choices =
        #    [{Artist.displayName: {'id': Artist.sk_id, 'uri': Artist.uri}}, Artist.displayName: {'id': Artist.sk_id, 'uri': Artist.uri}]
        #
        # 4) For each index, present Artist choice ('user_choice -1 = index' to start option_list at 1)
        #
        #          example:
        #               '1: 'Artist.displayName'
        #               '2: 'Artist.displayName'
        #               '3: 'Artist.displayName'
        #
        # 5) Use validated user choice (e.g. 1, 2, or 3) to get target Artist.sk_id
        #
        #       target_artist_id = Artist_Choices[user_choice - 1]['Artist.displayName']['id']
        #
        # OR -----
        # for Artist in Artist_list:
        #   if Artist.displayName = user_selection:
        #       return Artist.sk_id
        #


def search_venues(venue_name: str) -> [Venue]:

    venue_dict_list = query_mgr.search_venues_by_name(venue_name)
    if len(venue_dict_list) == 0:
        return []
    else:
        venue_list = instantiate_venues_from_list(venue_dict_list)
        return venue_list


def search_artist_id_for_upcoming_events(artist_id: int) -> [Event]:

    event_dict_list = query_mgr.search_artist_upcoming_events(artist_id)
    if len(event_dict_list) == 0:
        return []
    else:
        events_list = instantiate_events_from_list(event_dict_list)
        return events_list


def search_venue_id_for_upcoming_events(venue_id: int) -> [Event]:

    event_dict_list = query_mgr.search_venue_upcoming_events(venue_id)
    if len(event_dict_list) == 0:
        return []
    else:
        events_list = instantiate_events_from_list(event_dict_list)
        return events_list


def search_events_near_ip() -> [Event]:

    event_dict_list = query_mgr.search_events_by_ip_location()
    if len(event_dict_list) == 0:
        return []
    else:
        events_list = instantiate_events_from_list(event_dict_list)
        return events_list


def instantiate_events_from_list(event_list: [{}]) -> [Event]:

    if len(event_list) == 0:
        return []
    else:
        events_list = []
        for event in event_list:
            try:
                new_event = constructor.build_event(event)
                events_list.append(new_event)
            except KeyError:
                # log.-m
                continue
        return events_list


def instantiate_venues_from_list(venue_list: [{}]) -> [Venue]:

    if len(venue_list) == 0:
        return []
    else:
        venues_list = []
        for venue in venue_list:
            new_venue = constructor.build_venue(venue)
            venues_list.append(new_venue)
        return venues_list


def instantiate_artists_from_list(artist_list: [{}]) -> [Artist]:

    if not bool(len(artist_list)):
        return []
    else:
        artists_list = []
        for artist in artist_list:
            new_artist = constructor.build_artist(artist)
            artists_list.append(new_artist)
        return artists_list


def proof_search_artist():
    artists = search_for_artist(test_artist_name_1)
    count = 1
    selection_list = []
    for artist in artists:
        selection_list.append({'name': artist.displayName, 'id': artist.sk_id})
        print(str(count) + ': ' + artist.displayName)
        count += 1
    selection = ''
    while not selection:
        selection = input('Enter # to select Artist.')
    selected_artist = selection_list[int(selection) - 1]['name']
    for artist in artists:
        if artist.displayName == selected_artist:
            print(artist.__str__())


def proof_foo_event_search(events: [Event]):

    for event in events:
        print('=================================\n'
              '=================================\n'
              '=================================\n')
        print(event.__str__())

def proofs():

    proof_search_artist()

    # events = search_events_near_ip()
    # events = search_artist_id_for_upcoming_events(test_artist_id_2)
    # events = search_venue_id_for_upcoming_events(test_venue_id_2)
    # proof_foo_event_search(events)


if __name__ == '__main__':
    proofs()
