import time

from appium import webdriver
from selenium.webdriver.common.by import By


"""
day2 exercises
"""
class Utils:

    def __init__(self, platformName, platformVersion, deviceName, appPackage, appActivity):
        self.desired_caps = dict()
        self.desired_caps["platformName"] = platformName
        self.desired_caps["platformVersion"] = platformVersion
        self.desired_caps['deviceName'] = deviceName
        self.desired_caps['appPackage'] = appPackage
        self.desired_caps['appActivity'] = appActivity
        self.desired_caps["unicodeKeyboard"] = True
        self.desired_caps["resetKeyboard"] = True
        self.driver = None

    def get_driver(self, interface):
        if self.driver is None:
            self.driver = webdriver.Remote(interface, desired_capabilities=self.desired_caps)
        return self.driver

    def find_search_button(self):
        return self.driver.find_element(By.ID, 'com.android.settings:id/search')

    def find_input_text(self):
        return self.driver.find_element(By.ID, 'android:id/search_src_text')

    def find_back_button(self):
        return self.driver.find_element(By.CLASS_NAME, 'android.widget.ImageButton')

    def find_element_title(self):
        return self.driver.find_elements(By.ID, 'com.android.settings:id/title')

    def find_element_more(self):
        return self.driver.find_element(By.XPATH, '//*[@text="更多"]')

    def find_element_switch(self):
        return self.driver.find_element(By.ID, 'android:id/switchWidget')

    def find_element_mobile_net(self):
        return self.driver.find_element(By.XPATH, '//*[@text="移动网络"]')

    def find_element_first_net(self):
        return self.driver.find_element(By.XPATH, '//*[@text="首选网络类型"]')

    def find_element_2G(self):
        return self.driver.find_element(By.XPATH, '//*[@text="2G"]')


if __name__ == '__main__':
    util = Utils("android", '5.1', '1', "com.android.settings", '.Settings')
    driver = util.get_driver("http://localhost:4723/wd/hub")
    input_text_list = ["123abc", "你好", "qwertyuiop"]
    for item in input_text_list:
        util.find_search_button().click()
        util.find_input_text().send_keys(item)
        util.find_back_button().click()

    str_wlan = 'WLAN'
    eles = util.find_element_title()
    text_list = list()
    for ele in eles:
        text_list.append(ele.text)
    if str_wlan in text_list:
        print("True")
    else:
        print("False")

    util.find_element_more().click()
    util.find_element_switch().click()
    util.find_element_switch().click()
    util.find_element_mobile_net().click()
    util.find_element_first_net().click()
    time.sleep(1)
    util.find_element_2G().click()
    time.sleep(5)
    driver.quit()

