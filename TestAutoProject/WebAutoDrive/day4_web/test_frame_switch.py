import time
import unittest

from selenium import webdriver


class TestFrameSwitch(unittest.TestCase):
    def test_switch(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("file:///C:/Users/icerain/Desktop/page/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html")
        self.driver.find_element_by_id("user").send_keys("admin")
        time.sleep(2)
        # element = driver.find_element_by_id("idframe1")
        # driver.switch_to.frame(element)
        self.driver.switch_to.frame("idframe1")
        self.driver.find_element_by_id("userA").send_keys("admin1")
        time.sleep(2)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("myframe2")
        self.driver.find_element_by_id("userB").send_keys("admim2")
        time.sleep(2)

        self.driver.quit()