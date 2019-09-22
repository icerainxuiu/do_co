import requests

from data_for_test import CHANNELS_URL


class Channels:

    def __init__(self):
        self.channels_url = CHANNELS_URL

    def get_channels(self):
        return requests.get(self.channels_url)