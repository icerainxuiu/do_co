from logging import log

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Action:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, feature, timeout=10, poll=0.5):
        by_feature, value = feature
        # element = self.driver.find_element(by_feature, value)
        return WebDriverWait(
            self.driver,
            timeout,
            poll_frequency=poll).until(
            lambda x: x.find_element(
                by_feature,
                value))

    def click_element(self, feature):
        self.find_element(feature).click()

    def input_text(self, feature, content):
        self.find_element(feature).send_keys(content)

    def toast_is_exist(self, message):
        """
        判定输入的部分toast信息是否存在，存在返回True，不然返回False
        :param message:输入的部分toast信息
        :return:True 和 False
        """
        message_path = By.XPATH, "//*[contains(@text,'{}')]".format(message)
        try:
            self.find_element(message_path, timeout=5, poll=0.1)
            return True
        except BaseException as e:
            log(str(e))
            return False

    def get_toast(self, message):
        """

        :param message:
        :return:
        """
        if self.toast_is_exist(message):
            message_path = By.XPATH, "//*[contains(@text,'{}')]".format(message)
            return self.find_element(message_path, timeout=5, poll=0.1).text
        else:
            raise Exception("toast未出现，请检查参数是否正确，或toast是否出现在屏幕上")

    def scroll_one_time(self, direction="up"):
        width = self.driver.get_window_size()["width"]
        height = self.driver.get_window_size()["height"]
        center_x = width / 2
        center_y = height / 2

        top_x = center_x
        top_y = height / 4 * 1

        bottom_x = center_x
        bottom_y = height / 4 * 3

        left_x = center_y
        left_y = width / 4 * 1

        right_x = center_y
        right_y = width / 4 * 3
        if direction == "up":
            self.driver.swipe(bottom_x, bottom_y, top_x, top_y, duration=3000)

        elif direction == "down":
            self.driver.swipe(top_x, top_y, bottom_x, bottom_y, duration=3000)

        elif direction == "left":
            self.driver.swipe(right_x, right_y, left_x, left_y, duration=3000)

        elif direction == "right":
            self.driver.swipe(left_x, left_y, right_x, right_y, duration=3000)

        else:
            raise Exception("请检查参数是否正确，up/down/right/left")

    def scroll_find_element(self, feature, direction="up"):
        page_source_get = ""
        while True:
            try:
                return self.find_element(feature)
            except BaseException:
                self.scroll_one_time(direction=direction)
                if page_source_get == self.driver.page_source:
                    print("到底了，请查看需要查找的元素的信息是否正确")
                    break
                page_source_get = self.driver.page_source
