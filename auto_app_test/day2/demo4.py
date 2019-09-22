import os

from appium import webdriver

desired_caps = dict()

desired_caps['platformName'] = 'android'
desired_caps['platformVersion'] = '5.1'

desired_caps['deviceName'] = '1'

desired_caps['appPackage'] = 'com.android.settings'

desired_caps['appActivity'] = '.Settings'

desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

print(os.getcwd())

print(os.sep)