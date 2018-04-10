

class Artist:

    def __init__(
            self,
            bit_id:               str,   # db.int
            name:                 str,   # db.str
            url:                  str,   # db.url
            image_url:            str,   # db.url
            thumb_url:            str,   # db.url
            facebook_page_url:    str,   # db.url
            mbid:                 str,   # db.int
            tracker_count:        int,   # db.int
            upcoming_event_count: int):  # db.int

            self.bit_id = bit_id
            self.name = name
            self.url = url
            self.image_url = image_url
            self.thumb_url = thumb_url
            self.facebook_page_url = facebook_page_url
            self.mbid = mbid
            self.tracker_count = tracker_count
            self.upcoming_event_count = upcoming_event_count

    def __str__(self) -> str:

        return "                    \n" \
           "ID: {}                  \n" \
           "ame: {}                 \n" \
           "URL: {}                 \n" \
           "Image URL: {}           \n" \
           "Thumb URL: {}           \n" \
           "Facebook URL: {}        \n" \
           "MbID: {}                \n" \
           "Tracker Count: {}       \n" \
           "Upcoming Event Count: {}\n".format(

            self.bit_id,
            self.name,
            self.url,
            self.image_url,
            self.thumb_url,
            self.facebook_page_url,
            self.mbid,
            self.tracker_count,
            self.upcoming_event_count)




