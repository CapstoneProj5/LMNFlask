from utils.songkick_api_v1 import sk_city
from utils.songkick_api_v1.sk_city import City


class Venue:

    def __init__(
            self,
            sk_id: int,
            name: str,
            city: dict or City,
            metroArea: dict,
            uri: str,
            street: str,
            zip: str,
            lat: float,
            lng: float,
            phone: str,
            website: str,
            capacity: int,
            description: str):

            self.sk_id = sk_id
            self.name = name
            self.city = city
            self.metroArea = metroArea
            self.uri = uri
            self.street = street
            self.zip = zip
            self.lat = lat
            self.lng = lng
            self.phone = phone
            self.website = website
            self.capacity = capacity
            self.description = description

    def __str__(self):
        return "\n" \
           "ID: {}\n" \
           "Name: {}\n" \
           "City: {}\n" \
           "URI: {}\n" \
           "Street: {}\n" \
           "Zip: {}\n" \
           "Lat: {}\n" \
           "Lng: {}\n" \
           "Phone: {}\n" \
           "Website: {}\n" \
           "Capacity: {}\n" \
           "Description: {}\n".format(

            str(self.sk_id),
            self.name,
            self.city.__str__(),
            self.uri,
            self.street,
            self.zip,
            str(self.lat),
            str(self.lng),
            self.phone,
            self.website,
            str(self.capacity),
            self.description
        )

            # self,
            # sk_id:       int,
            # name:        str,
            # uri:         str,
            # metroArea:   dict,
            # city:        sk_city,
            # street:      str,
            # zip_code:    str,
            # lat:         float = None,
            # lng:         float = None,
            # phone:       str = None,
            # website:     str = None,
            # capacity:    int = None,
            # description: str = None):
            #
            # self.id = sk_id
            # self.name = name
            # self.uri = uri
            # self.metroArea = metroArea
            # self.city = city
            # self.street = street
            # self.zip_code = zip_code
            # self.lat = lat
            # self.lng = lng
            # self.phone = phone
            # self.website = website
            # self.capacity = capacity
            # self.description = description


    # def __str__(self) -> str:
    #
    #     return "            \n" \
    #        "ID: {}          \n" \
    #        "Name: {}        \n" \
    #        "URI: {}         \n" \
    #        "City: {}        \n" \
    #        "Street: {}      \n" \
    #        "Zip: {}         \n" \
    #        "Lat: {}         \n" \
    #        "Lng: {}         \n" \
    #        "Phone: {}       \n" \
    #        "Website: {}     \n" \
    #        "Capacity: {}    \n" \
    #        "Description: {} \n".format(
    #
    #         str(self.id),
    #         self.name,
    #         self.uri,
    #         self.city.__str__(),
    #         self.street,
    #         self.zip_code,
    #         str(self.lat),
    #         str(self.lng),
    #         self.phone,
    #         self.website,
    #         str(self.capacity),
    #         self.description)
