from selenium.webdriver.common.by import By

from base.base_action import Action


class RegisterPage(Action):
    login_button = By.XPATH, "//*[@text='已有账号，去登录']"
    register_button = By.ID, "com.yunmall.lc:id/registerContent"

    def click_register_button(self):
        self.click_element(self.register_button)

    def click_login_button(self):
        self.click_element(self.login_button)