import requests

from data_for_test import LOGIN_URL, MESSAGE_URL


class Login:

    def __init__(self):
        self.login_url = LOGIN_URL
        self.message_url = MESSAGE_URL

    def get_login(self, data):

        return requests.post(self.login_url, json=data)

    def get_message_code(self, mobile):
        return requests.get(self.message_url + mobile)

