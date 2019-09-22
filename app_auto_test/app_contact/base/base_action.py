from selenium.webdriver.support.wait import WebDriverWait


class Action:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, feature, timeout=10, poll=0.5):
        by_feature, value = feature
        # element = self.driver.find_element(by_feature, value)
        return WebDriverWait(self.driver, timeout, poll_frequency=poll).until(lambda x: x.find_element(by_feature, value))

    def click_element(self, feature):
        self.find_element(feature).click()

    def input_text(self, feature, content):
        self.find_element(feature).send_keys(content)