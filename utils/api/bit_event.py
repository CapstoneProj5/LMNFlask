

class Event:

    def __init__(
            self,
            event_id:         str,
            artist_id:        str,
            url:              str,
            on_sale_datetime: str,
            show_time:        str,
            description:      str,
            venue:            list,
            city:             str,
            country:          str,
            lineup:           list):

            self.event_id = event_id
            self.artist_id = artist_id
            self.url = url
            self.on_sale_datetime = on_sale_datetime
            self.show_time = show_time
            self.description = description
            self.venue = venue
            self.city = city
            self.country = country
            self.lineup = lineup

    def __str__(self):

        return "             \n" \
           "Event ID: {}     \n" \
           "Artist ID: {}    \n" \
           "URL: {}          \n" \
           "On-Sale Date: {} \n" \
           "Doors @ {}       \n" \
           "Description: {}  \n" \
           "Venue: {}        \n" \
           "City: {}         \n" \
           "Country: {}      \n" \
           "Lineup: {}       \n".format(

            self.event_id,
            self.artist_id,
            self.url,
            self.on_sale_datetime,
            self.show_time,
            self.description,
            # ' '.join(self.venue),
            self.venue,
            self.city,
            self.country,
            ', '.join(self.lineup))
