from LMNFlask.utils.songkick_api import sk_artist
from LMNFlask.utils.songkick_api.sk_artist import Artist


class Performance:

    def __init__(
            self,
            performers:   list,
            name:         str,
            billingIndex: int,
            sk_id:        int,
            billing:      str):

            self.performers = performers
            self.name = name
            self.billingIndex = billingIndex
            self.sk_id = sk_id
            self.billing = billing

    def __str__(self) -> str:

        return "       \n" \
           "Artists: {} \n" \
           "Name: {}   \n" \
           "Slot: {}   \n" \
           "ID: {}     \n" \
           "Billing: {}\n".format(

            ', '.join([act.displayName for act in self.performers]),
            self.name,
            str(self.billingIndex),
            str(self.sk_id),
            self.billing)