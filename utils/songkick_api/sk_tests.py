from flask import Flask
from flask_testing import TestCase
import urllib3
import unittest
import json
from flask import jsonify
from sk_artist import Artist
from sk_venue import Venue
from sk_event import Event
from sk_constructor import build_artist, build_venue, build_event

class skTest(unittest.TestCase):

    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        return app

    def test_build_artist(self):
        example_artist_data = '{"id": 253846, "displayName": "Radiohead","uri": "http://www.songkick.com/artists/253846-radiohead?utm_source=45852&utm_medium=partner","identifier": [{"href": "http://api.songkick.com/api/3.0/artists/mbid:a74b1b7f-71a5-4011-9441-d0b5e4122711.json","mbid": "a74b1b7f-71a5-4011-9441-d0b5e4122711"}],"onTourUntil": "2018-04-25"}'
        exjl = json.loads(example_artist_data)
        expected_artist = Artist(253846, 'Radiohead')
        print('EA: ', expected_artist)
        artist_created = build_artist(exjl)
        print('AC: ', artist_created)
        self.assertTrue(expected_artist, artist_created)

    def test_build_venue(self):
        example_venue_data = '''{
        "id":17522,
        "displayName":"O2 Academy Brixton",
        "uri":"http://www.songkick.com/venues/17522-o2-academy-brixton",
        "city": {
          "id":24426,
          "uri":"http://www.songkick.com/metro_areas/24426-uk-london",
          "displayName":"London",
          "country": {"displayName":"UK"}
        },
        "street":"211 Stockwell Road",
        "zip":"SW9 9SL",
        "lat":51.4651268,
        "lng":-0.115187,
        "phone":"020 7771 3000",
        "website":"http://www.brixton-academy.co.uk",
        "capacity":4921,
        "description": "Brixton Academy is an award winning music venue situated in the heart of Brixton, South London.",
        "metroArea": {
          "id":24426,
          "uri":"http://www.songkick.com/metro_areas/24426-uk-london",
          "displayName":"London","country":{"displayName":"UK"}
        }
      }'''

        example_location_data = '''{
        "city":"San Francisco, CA, US",
        "lat":37.7842398,
        "lng":-122.4332937
        }'''
        exvd = json.loads(example_venue_data)
        exld = json.loads(example_location_data)
        expected_venue = Venue(17522, "O2 Academy Brixton", "San Francisco", "CA")
        print('EV: ', expected_venue)
        venue_created = build_venue(exvd, exld)
        print('VC: ', venue_created)
        self.assertTrue(expected_venue, venue_created)

    def test_build_event(self):
        example_event_data = '''{
        "id":11129128,
        "type":"Concert",
        "uri":"http://www.songkick.com/concerts/11129128-wild-flag-at-fillmore?utm_source=PARTNER_ID&utm_medium=partner",
        "displayName":"Wild Flag at The Fillmore (April 18, 2012)",
        "start": {
          "time":"20:00:00",
          "date":"2012-04-18",
          "datetime":"2012-04-18T20:00:00-0800"
        },
        "performance": [
          {
            "artist":{
              "uri":"http://www.songkick.com/artists/29835-wild-flag?utm_source=PARTNER_ID&utm_medium=partner",
              "displayName":"Wild Flag",
              "id":29835,
              "identifier":[]
            },
            "id":21579303,
            "displayName":"Wild Flag",
            "billingIndex":1,
            "billing":"headline"
          }
        ],
        "location": {
          "city":"San Francisco, CA, US",
          "lng":-122.4332937,
          "lat":37.7842398
        },
        "venue": {
          "id":6239,
          "displayName":"The Fillmore",
          "uri":"http://www.songkick.com/venues/6239-fillmore?utm_source=PARTNER_ID&utm_medium=partner",
          "lng":-122.4332937,
          "lat":37.7842398,
          "metroArea": {
            "uri":"http://www.songkick.com/metro_areas/26330-us-sf-bay-area?utm_source=PARTNER_ID&utm_medium=partner",
            "displayName":"SF Bay Area",
            "country": { "displayName":"US" },
            "id":26330,
            "state": { "displayName":"CA" }
          }
        },
        "status":"ok",
        "popularity":0.012763
      }'''

        exed = json.loads(example_event_data)
        expected_event = Event(11129128, "2012-04-18T20:00:00-0800", "Wild Flag", "The Fillmore")
        # print('EE: ',expected_event)
        event_created = build_event(exed)
        # print('EvC: ',event_created)
        self.assertEqual(expected_event, event_created)

if __name__ == '__main__':
    unittest.main()


# def test_build_venue(self):
#   example_venue_data = { 'name': 'first avenue', 'address': '700 first avenue'}   # or whatever structure the API returns
#   example_location_data = # whatever this is
#   expected_venue = Venue( # create expected venue object )
#   venue = build_venue(example_venue_data, example_location_data)
#   assertEqual(expected_venue, venue)
#
#
# def test_fail_build_venue(self):
#   example_invalid_venue = { "error" : "404" } # or example fail message from API
#
#   example_location_data = # whatever this is
#   venue = build_venue(example_venue_data, example_location_data)
#   assertFalse(venue)
