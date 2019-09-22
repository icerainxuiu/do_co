import requests
import unittest

from parameterized import parameterized

from data_for_session_8 import VERIFY_URL, LOGIN_URL, ORDER_URL, data_json


class TestApi(unittest.TestCase):
    session = None

    @classmethod
    def setUp(cls) -> None:
        if cls.session is None:
            cls.session = requests.Session()
        cls.verify_url = VERIFY_URL
        cls.login_url = LOGIN_URL
        cls.order_url = ORDER_URL

    @classmethod
    def tearDown(cls) -> None:
        cls.session.close()

    def test01_verify(self):
        response = self.session.get(self.verify_url)
        print(response.status_code)
        self.assertEqual("image/png", response.headers.get("content-type"))

    @parameterized.expand(data_json())
    def test02_login(self, my_data):
        self.test01_verify()
        print(my_data)
        response = self.session.post(self.login_url, data=my_data)
        print(response.status_code)
        self.assertIn("登陆成功", response.json().get('msg'))

    def test03_order(self):
        response = self.session.get(self.order_url)
        print(response.status_code)
        self.assertIn("我的订单", response.text)
