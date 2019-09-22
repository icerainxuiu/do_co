import time

from selenium import webdriver

# 实例化浏览器驱动对象，并浏览器最大化和设置隐式等待10秒
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
# 打开注册实例页面 找到注册A页面并点击
driver.get("file:///C:/Users/icerain/Desktop/page/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html")
driver.find_element_by_id("ZCA").click()
# 获取打开后的浏览器窗口句柄，并切换至新窗口后找到账号输入框输入admin1
handle_window = driver.window_handles
driver.switch_to.window(handle_window[-1])
driver.find_element_by_id("userA").send_keys("admin1")
time.sleep(2)
# 切换回原窗口并找到输入账号输入框输入admin
driver.switch_to.window(handle_window[0])
driver.find_element_by_id("user").send_keys("admin")
time.sleep(2)
# 切换回新窗口并关闭当前窗口
driver.switch_to.window(handle_window[-1])
driver.close()
# 关闭浏览器
time.sleep(2)
driver.quit()
