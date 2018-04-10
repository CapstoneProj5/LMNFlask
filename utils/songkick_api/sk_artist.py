from datetime import date


class Artist:

        def __init__(
                self,
                sk_id:       int,
                displayName: str,
                uri:         str,
                onTourUntil: date or None):

                self.sk_id = sk_id
                self.displayName = displayName
                self.uri = uri
                self.onTourUntil = onTourUntil

        def __str__(self) -> str:

            return "              \n" \
                "ID: {}           \n" \
                "Name: {}         \n" \
                "URI: {}          \n" \
                "On Tour Until: {}\n".format(

                str(self.sk_id),
                self.displayName,
                self.uri,
                self.onTourUntil)
