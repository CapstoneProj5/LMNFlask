from flask import Flask
from flask_testing import TestCase
import urllib3
import unittest
import json
from flask import jsonify
from sk_artist import Artist
from sk_constructor import build_artist

class skTest(TestCase):

    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        return app

    def test_build_artist(self):
        example_artist_data = ({"id": 253846, "displayName": "Radiohead","uri": "http://www.songkick.com/artists/253846-radiohead?utm_source=45852&utm_medium=partner","identifier": [{"href": "http://api.songkick.com/api/3.0/artists/mbid:a74b1b7f-71a5-4011-9441-d0b5e4122711.json","mbid": "a74b1b7f-71a5-4011-9441-d0b5e4122711"}],"onTourUntil": "2018-04-25"})
        exjd = json.dumps(example_artist_data)
        exjl = json.loads(exjd)
        # json_artist_data = (example_artist_data)
        print ('json: ',exjl)
        expected_artist = '''Artist("sk_id": 253846, "displayName":"Radiohead" )'''
        print ('expected_artist: ', expected_artist)
        artist = build_artist(exjl)
        print('artist: ', artist)

        self.assertEqual(expected_artist, exjl)


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
