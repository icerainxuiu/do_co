import time

import pytest

from base.base_data_analyze import data_analyze
from base.base_driver import get_driver
from page.page import Page


class TestLogin:
    def setup(self):
        self.driver = get_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    # @pytest.mark.parametrize("args", data_analyze("data.yaml", "testlogin"))
    # def test_login(self, args):
    #     username = args["username"]
    #     password = args["password"]
    #     toast = args["toast"]
    #
    #     self.page.home.click_me_button()
    #     self.page.register.click_login_button()
    #     self.page.login.input_username(username)
    #     self.page.login.input_password(password)
    #     self.page.login.click_login_button()
    #
    #     if toast is None:
    #         assert self.page.me.get_me_text_view() == username, \
    #             "登录后的用户名和输入的用户名不一致"
    #     else:
    #         pass
    def test_login(self):
        self.page.home.click_me_button()
