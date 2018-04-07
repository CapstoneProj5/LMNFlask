from LMNFlask.utils.songkick_api import sk_city


class Venue:

    def __init__(
            self,
            sk_id:       int,
            name:        str,
            uri:         str,
            metroArea:   dict,
            city:        sk_city,
            street:      str,
            zip_code:    str,
            lat:         float = None,
            lng:         float = None,
            phone:       str = None,
            website:     str = None,
            capacity:    int = None,
            description: str = None):

            self.id = sk_id
            self.name = name
            self.uri = uri
            self.metroArea = metroArea
            self.city = city
            self.street = street
            self.zip_code = zip_code
            self.lat = lat
            self.lng = lng
            self.phone = phone
            self.website = website
            self.capacity = capacity
            self.description = description

    def __str__(self) -> str:

        return "            \n" \
           "ID: {}          \n" \
           "Name: {}        \n" \
           "URI: {}         \n" \
           "City: {}        \n" \
           "Street: {}      \n" \
           "Zip: {}         \n" \
           "Lat: {}         \n" \
           "Lng: {}         \n" \
           "Phone: {}       \n" \
           "Website: {}     \n" \
           "Capacity: {}    \n" \
           "Description: {} \n".format(

            str(self.id),
            self.name,
            self.uri,
            self.city.__str__(),
            self.street,
            self.zip_code,
            str(self.lat),
            str(self.lng),
            self.phone,
            self.website,
            str(self.capacity),
            self.description)
