from selenium.webdriver.common.by import By

from base.base_action import Action


class HomePage(Action):
    # 主页我的按钮
    me_button = By.ID, "com.suning.mobile.epa:id/tab_name"
    home_page_activity = ".launcher.LauncherActivity"

    def click_me_button(self):
        self.click_element(self.me_button)

    def login_if_not(self, page):
        self.click_me_button()
        if self.driver.current_activity != self.home_page_activity:
            return
        else:
            pass
