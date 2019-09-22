import unittest

from api.cancel_api import Cancel


class TestCancel(unittest.TestCase):

    def setUp(self) -> None:
        self.cancel = Cancel()

    def test_cancel(self):

        response = self.cancel.get_cancel("1")
        print(response.text)
