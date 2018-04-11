
class Artist(object):

    def __init__(
            self,
            sk_id: int,
            displayName: str):

            self.sk_id = sk_id
            self.displayName = displayName

    def __str__(self):
            return " \n" \
            "ID: {}  \n" \
            "Name: {}\n".format(

            self.sk_id,
            self.displayName)
