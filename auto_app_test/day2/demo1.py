import time

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

desired_cap = dict()

# 平台名字
desired_cap["platformName"] = 'android'

# 平台版本
desired_cap["platformVersion"] = '5.1'

# 设备名字
desired_cap["deviceName"] = '1'

# 要打开的应用程序
desired_cap["appPackage"] = 'com.android.settings'

# 要打开的界面
desired_cap["appActivity"] = '.Settings'
# 创建驱动对象
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)

driver.implicitly_wait(10)

# # 找到搜索放大镜并点击
# driver.find_element_by_id("com.android.settings:id/search").click()
#
# # 找到输入框并输入文本
# driver.find_element_by_class_name("android.widget.EditText").send_keys("hello")
#
# # 点击后退
# driver.find_element_by_xpath("//*[@content-desc='收起']").click()
# WebDriverWait(driver, 30, poll_frequency=3).until(lambda x: x.find_element_by_xpath("//*[contains(@text, '设')]"))
texts = driver.find_elements_by_xpath("//*[contains(@text,'设')]")
print(len(texts))
for text in texts:
    print(text.text)

time.sleep(5)

driver.quit()
