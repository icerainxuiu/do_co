import unittest

from api.channels_api import Channels


class TestChannels(unittest.TestCase):

    def setUp(self) -> None:
        self.channels = Channels()

    def test_channels(self):
        response = self.channels.get_channels()
        print(response.text)
