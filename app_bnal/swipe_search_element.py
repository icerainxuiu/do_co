
from appium import webdriver
import time


desired_caps = dict()
desired_caps['platformName'] = 'android'
desired_caps['platformVersion'] = '5'
desired_caps['deviceName'] = '1'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'
desired_caps['automationName'] = 'Uiautomator2'
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

# 在三次内找到才行
# for i in range(4):
#     try:
#         driver.find_element_by_xpath("//*[@text='关于手机']").click()
#         break
#     except BaseException as e:
#         driver.swipe(100, 2000, 100, 1000, duration=500)
#         print(e)


time.sleep(3)
driver.quit()
