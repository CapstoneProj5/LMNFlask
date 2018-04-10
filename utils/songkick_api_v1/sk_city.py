

class City:

    def __init__(
            self,
            sk_id:   int,
            name:    str,
            uri:     str,
            country: dict):

            self.sk_id = sk_id
            self.name = name
            self.uri = uri
            self.country = country

    def __str__(self) -> str:

        return "        \n" \
            "ID: {}     \n" \
            "Name: {}   \n" \
            "URI: {}    \n" \
            "Country: {}\n".format(

            self.sk_id,
            self.name,
            self.uri,
            self.country['displayName'])