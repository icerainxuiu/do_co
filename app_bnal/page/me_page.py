from selenium.webdriver.common.by import By

from base.base_action import Action


class MePage(Action):
    me_text = By.ID, "com.yunmall.lc:id/tv_user_nikename"
    setting_button = By.ID, 'com.yunmall.lc:id/ymtitlebar_left_btn_image'

    def get_me_text_view(self):
        return self.find_element(self.me_text).text

    def click_setting_button(self):
        self.click_element(self.setting_button)