import unittest

from api.collections_api import Collections
from api.login_api import Login


class TestCollections(unittest.TestCase):

    def setUp(self) -> None:
        self.collections = Collections()
        # self.login = Login()

    def test_collections(self):
        data = {
            "target":1
        }
        response = self.collections.get_collections(data)
        print(response.text)
