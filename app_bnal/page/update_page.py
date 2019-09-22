from selenium.webdriver.common.by import By

from base.base_action import Action


class UpdatePage(Action):
    update_button = By.XPATH, "//*[@text='版本更新']"

    def click_update_button(self):
        self.find_element(self.update_button).click()


