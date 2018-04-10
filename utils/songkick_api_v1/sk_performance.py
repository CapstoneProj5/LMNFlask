from utils.songkick_api_v1.sk_artist import Artist


class Performance:

    def __init__(
            self,
            artist:    Artist,
            name:         str,
            billingIndex: int,
            sk_id:        int,
            billing:      str):

            self.artist = artist
            self.name = name
            self.billingIndex = billingIndex
            self.sk_id = sk_id
            self.billing = billing

    def __str__(self) -> str:

        return "       \n" \
           "\tName: {}   \n" \
           "\tSlot: {}   \n" \
           "\tPerformance_ID: {}     \n" \
           "\tBilling: {}\n".format(

            self.name,
            str(self.billingIndex),
            str(self.sk_id),
            self.billing)
