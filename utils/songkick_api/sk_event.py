
import datetime
from sk_artist import Artist
from sk_venue import Venue
# from utils.songkick_api.sk_venue import Venue
# from utils.songkick_api.sk_artist import Artist


class Event(object):

    def __init__(

            self,
            sk_id:  int,
            date:   datetime.date,
            artist: Artist,
            venue:  Venue):

            self.sk_id = sk_id
            self.date = date
            self.artist = artist
            self.venue = venue

    def __str__(self):

        return "      \n" \
           "ID: {}    \n" \
           "Date: {}  \n" \
           "Artist: {}\n" \
           "Venue: {} \n".format(

            str(self.sk_id),
            self.date,
            self.artist,
            self.venue)

    def __dict__(self):

        return {
            'sk_id':  self.sk_id,
            'date':   self.date,
            'artist': self.artist,
            'venue':  self.venue}

    def __eq__(self, other):

        return self.sk_id == other.sk_id and self.date == other.date and self.artist == other.artist and self.venue == other.venue
