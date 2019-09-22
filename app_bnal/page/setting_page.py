from selenium.webdriver.common.by import By

from base.base_action import Action


class SettingPage(Action):
    about_button = By.XPATH, "//*[@text='关于百年奥莱']"

    def click_about_button(self):
        self.scroll_find_element(self.about_button).click()
    