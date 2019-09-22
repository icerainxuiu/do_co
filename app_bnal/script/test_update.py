from base.base_driver import get_driver
from page.page import Page

class TestUpdate:
    def setup(self):
        self.driver = get_driver(no_reset=False)
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    def test_update(self):

        self.page.home.login_if_not(self.page)
        self.page.me.click_setting_button()
        self.page.setting.click_about_button()
        self.page.update.click_update_button()
        print("是否找到toast信息最新版本：", self.page.update.toast_is_exist("当前已是最新版本"))
        assert self.page.update.toast_is_exist("当前已是最新版本")