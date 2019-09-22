import requests

from api.login_api import Login
from data_for_test import COLLECTION_URL, LOGIN_URL


class Collections:
    def __init__(self):

        self.collections_url = COLLECTION_URL
        self.login = Login()

    def get_collections(self, data):
        json_data = {"mobile":"13012345678","code":"888888"}
        token = self.login.get_login\
            (json_data).json().get("data").get("token")

        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + token
        }

        return requests.post(self.collections_url, json=data, headers=headers)