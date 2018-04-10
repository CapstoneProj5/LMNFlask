

class Venue:

    def __init__(
            self,
            name:      str,   # db.str
            latitude:  str,   # db.double
            longitude: str,   # db.double
            city:      str,   # db.str
            region:    str,   # db.str
            country:   str):  # db.str

            self.name = name
            self.latitude = latitude
            self.longitude = longitude
            self.city = city
            self.region = region
            self.country = country

    def __str__(self) -> str:

        return "         \n" \
           "Venue: {}    \n" \
           "Latitude: {} \n" \
           "Longitude: {}\n" \
           "City: {}     \n" \
           "Region: {}   \n" \
           "Country: {}  \n".format(

            self.name,
            self.latitude,
            self.longitude,
            self.city,
            self.region,
            self.country)

    def get_attr(self, attr):
        return self.__getattribute__(attr)

    def set_attr(self, attr, var):
        self.__setattr__(attr, var)
