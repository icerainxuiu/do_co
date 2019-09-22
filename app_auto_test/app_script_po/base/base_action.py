


class Actions:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, feature):
        by_feature, content = feature
        return self.driver.find_element(by_feature, content)

    def click_btn(self, feature):
        self.find_element(feature).click()

    def send_message(self, feature, content):
        self.find_element(feature).send_keys(content)

    def find_elements(self, feature):
        by_feature, content = feature
        return self.driver.find_elements(by_feature, content)


