from selenium.webdriver.common.by import By

from base.base_action import Action


class LoginPage(Action):

    username = By.ID, "com.yunmall.lc:id/logon_account_textview"
    password = By.ID, "com.yunmall.lc:id/logon_password_textview"
    login_button = By.ID, "com.yunmall.lc:id/logon_button"

    def input_username(self, username):
        self.input_text(self.username, username)

    def input_password(self, password):
        self.input_text(self.password, password)

    def click_login_button(self):
        self.click_element(self.login_button)