# 创建一个空字典存放平台版本设备名等信息
import time

from appium import webdriver

desired_cap = dict()

# 平台
desired_cap["platformName"] = 'android'
# 版本
desired_cap["platformVersion"] = '5.1'
# 设备名
desired_cap["deviceName"] = '1'
# 包名
desired_cap["appPackage"] = 'cn.goapk.market'
# 启动名
desired_cap["appActivity"] = 'com.anzhi.market.ui.MainActivity'
# 设置中文输入
desired_cap["unicodeKeyboard"] = True
desired_cap["resetKeyboard"] = True

# 创建驱动对象
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities=desired_cap)

driver.implicitly_wait(10)
driver.start_activity("com.android.settings", ".Settings")
# driver.find_element_by_id("com.android.settings:id/search").click()
# element = driver.find_element_by_id("android:id/search_src_text")
#
# element.send_keys("hello")
# time.sleep(3)
# element.clear()
# element.send_keys("张丽莎你是不是太美了")

# elements = driver.find_elements_by_id("com.android.settings:id/title")
# for element in elements:
#     print(element.get_attribute("name"))
#     print(element.get_attribute("text"))
#     print(element.get_attribute("className"))
#     print(element.get_attribute("enabled"))
#     print(element.get_attribute("resourceId"))
#     print("*" * 50)
# driver.swipe(100, 2000, 100, 100, 500)
# time.sleep(3)
# driver.swipe(100, 1000, 100, 2000, 500)

save_button = driver.find_element_by_xpath("//*[@text='存储']")
more_button = driver.find_element_by_xpath("//*[@text='更多']")

# driver.scroll(save_button, more_button)
driver.drag_and_drop(save_button, more_button)

time.sleep(5)
driver.quit()
