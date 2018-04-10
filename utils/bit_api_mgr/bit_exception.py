
class ArtistConstructorError(Exception):
    def __init__(self):
        self.message = 'Arguments of _name and/or _bit_id != ""'

    def __str__(self):
        return self.message
