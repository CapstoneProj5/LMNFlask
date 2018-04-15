# from logging import Logger
import requests
# from LMNFlask import log
import utils.songkick_api.sk_constructor as Constructor
from utils.songkick_api.sk_event import Event
from utils.database import db_manager as db

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


def parse_api(call=None):
    api_artists = []
    api_venues = []
    api_shows = []
    if call is not None:
        call = search_local_events_for_ip()
    for event in call:
        for artist in event["performance"]:
            name = artist["artist"]["displayName"]
            sk_id = artist["artist"]["id"]
            api_artists.append({"name": name, "sk_id": sk_id})

    print(api_artists)

    for venue in call:
        name = venue["venue"]["displayName"]
        city = venue["venue"]["metroArea"]["displayName"]
        state = venue["venue"]["metroArea"]["state"]["displayName"]
        sk_id = venue["venue"]["id"]
        api_venues.append({"name": name, "city": city, "state": state, "sk_id": sk_id})

    print(api_venues)

    for show in call:
        # print(show)
        time = show["start"]["time"]
        # print(time)
        date = show["start"]["date"]
        # print(date)

        venue_sk_id = show["venue"]["id"]
        # print(venue_sk_id)

        for artist in show["performance"]:
            if artist["billingIndex"] == 1:
                # print("headliner")
                # print(artist["displayName"])
                artist_sk_id = artist["id"]
                # print(artist_sk_id)

        print("show[id]")
        print(show["id"])

        show_sk_id = show["id"]

        api_shows.append({"time": time, "date": date, "venue": venue_sk_id,
                          "artist": artist_sk_id, "show_sk_id": show_sk_id})

    print(api_shows)

    for a in api_artists:
        db.insert_atrist(a)

    for v in api_venues:
        db.insert_venue(v)

    for s in api_shows:
        db.insert_show(s)


if __name__ == '__main__':
    # print(get_external_ip())
    # print(search_local_events_for_ip())
    # print(instantiate_events_from_list(search_local_events_for_ip()))
    parse_api(search_local_events_for_ip())
