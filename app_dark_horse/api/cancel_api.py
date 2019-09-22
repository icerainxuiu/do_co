import requests

from data_for_test import CANCEL_COLLECTION_URL


class Cancel:

    def __init__(self):
        self.cancel_url = CANCEL_COLLECTION_URL

    def get_cancel(self, data):
        return requests.delete(self.cancel_url + data)