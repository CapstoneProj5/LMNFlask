
from utils.songkick_api_v1.sk_location import Location
from utils.songkick_api_v1.sk_performance import Performance
from utils.songkick_api_v1.sk_venue import Venue


class Event:

    def __init__(
            self,
            sk_id:       int,
            event_type:  str,
            uri:         str,
            displayName: str,
            start:       dict,
            performances:  [Performance] or [dict],
            location:    Location or dict,
            venue:       Venue or dict,
            status:      str,
            popularity:  float):

            self.sk_id = sk_id
            self.event_type = event_type
            self.uri = uri
            self.event_name = displayName
            self.start = start
            self.performances = performances
            self.location = location
            self.venue = venue
            self.status = status
            self.popularity = popularity

    def __str__(self) -> str:

        return "           \n" \
           "ID: {}         \n" \
           "Type: {}       \n" \
           "URI: {}        \n" \
           "Name: {}       \n" \
           "Date: {}       \n" \
           "Time: {}       \n" \
           "Performers: {} \n" \
           "Location: {}   \n" \
           "Venue: {}      \n" \
           "Status: {}     \n" \
           "Popularity: {} \n".format(

            str(self.sk_id),
            self.event_type,
            self.uri,
            self.event_name,
            self.start['date'],
            self.start['time'],
            ', \n'.join([performance.__str__() for performance in self.performances]),
            self.location.__str__(),
            self.venue.__str__(),
            self.status,
            str(self.popularity))
