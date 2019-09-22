import time

import pytest

from base.base_driver import init_driver
from page.page import Page


class TestSetting:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):

        self.driver.quit()

    @pytest.mark.parametrize(("phone, content"), [("18828828888", "hello"), ("15170540861", 'hhhhh')])
    def test_message(self, phone, content):
        self.page.message_page.click_write_btn()
        self.page.message_page.send_content(phone)
        self.page.message_page.send_msg(content)
        self.page.message_page.click_send()
        time.sleep(3)
