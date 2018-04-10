

class Location:

    def __init__(
            self,
            city: str,
            lat: float = None,
            lng: float = None):

            self.city = city
            self.lat = lat
            self.lng = lng

    def __str__(self) -> str:

        return "         \n" \
           "City: {}     \n" \
           "Latitude: {} \n" \
           "Longitude: {}\n".format(

            self.city,
            str(self.lat),
            str(self.lng))
