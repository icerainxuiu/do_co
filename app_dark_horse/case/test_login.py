import unittest

from parameterized import parameterized

from api.login_api import Login
from data_for_test import data_for_login


class TestLogin(unittest.TestCase):

    def setUp(self) -> None:
        self.login = Login()

    def test_message_code(self):
        response = self.login.get_message_code("13012345678")
        print(response.text)

    @parameterized.expand(data_for_login())
    def test_login(self, mobile, code, status_code, message):
        data = {
            "mobile": mobile,
            "code": code
        }
        response = self.login.get_login(data)
        print(response.text)
