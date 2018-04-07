from LMNFlask.utils.songkick_api import sk_performance, sk_location, sk_venue


class Event:

    def __init__(
            self,
            sk_id:       int,
            event_type:  str,
            uri:         str,
            displayName: str,
            start:       dict,
            performers:  sk_performance,
            location:    sk_location,
            venue:       sk_venue,
            status:      str,
            popularity:  float):

            self.sk_id = sk_id
            self.event_type = event_type
            self.uri = uri
            self.event_name = displayName
            self.start = start
            self.performances = performers
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
            self.performances.__str__(),
            self.location.__str__(),
            self.venue.__str__(),
            self.status,
            str(self.popularity))