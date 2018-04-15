from utils.scheduler.tasks import scheduler
from flask import render_template, Flask, current_app, jsonify
from flask_app import app
from utils.songkick_api.sk_api_mgr import search_local_events_for_ip

# log = app.logger  # log.info(), log.warn(), log.err


@app.route('/')
def hello_world():
    return "hello"


@app.route('/goodbye')
def goodbye_world():
    return render_template("goodbye.html")


@app.route('/test/api')
def test_api():
    call = search_local_events_for_ip()

    parse_api(call)

    return jsonify({"results": call})


def factory():
    app = Flask(__name__)
    return app


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

        show_sk_id = show["id"]
        print(show_sk_id)

        for artist in show["performance"]:
            if artist["billingIndex"] == 1:
                # print("headliner")
                # print(artist["displayName"])
                artist_sk_id = artist["id"]
                # print(artist_sk_id)
        api_shows.append({"time": time, "date": date, "venue": venue_sk_id, "artist": artist_sk_id})

    print(api_shows)



if __name__ == '__main__':
    # app.debug = False
    # scheduler.start()
    app.run()
