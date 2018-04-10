from datetime import date

db = None


class ArtistDataModel(db.model):

    __tablename__ = 'artist data'

    sk_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    displayName = db.Column(db.String, nullable=False)
    uri = db.Column(db.String, nullable=False)
    onTourUntil = db.Column(db.Date, nullable=True)

    def __init__(self, Artist):
        self.sk_id = Artist.sk_id
        self.displayName = Artist.displayName
        self.uri = Artist.uri
        self.onTourUntil = Artist.onTourUntil
