from appium import webdriver


def get_driver():

    desired_caps = dict()

    desired_caps['platformName'] = 'android'
    desired_caps["platformVersion"] = '5.1'

    desired_caps['deviceName'] = '1'

    desired_caps['appPackage'] = 'com.android.contacts'
    desired_caps['appActivity'] = '.activities.PeopleActivity'
    desired_caps['noReset'] = True
    desired_caps['automationName'] = 'Uiautomator2'

    return webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)