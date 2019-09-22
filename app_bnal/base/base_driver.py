import time

from appium import webdriver


def get_driver(no_reset=True):
    desired_caps = dict()

    desired_caps['platformName'] = 'android'
    desired_caps["platformVersion"] = '8'

    desired_caps['deviceName'] = '1'

    desired_caps['appPackage'] = 'com.suning.mobile.msd'
    desired_caps['appActivity'] = '.MainActivity'
    desired_caps['noReset'] = no_reset
    # desired_caps['automationName'] = 'Uiautomator2'
    # desired_caps['noReset'] = True
    # 支持中文
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    return driver


if __name__ == '__main__':
    driver = get_driver()
    time.sleep(4)