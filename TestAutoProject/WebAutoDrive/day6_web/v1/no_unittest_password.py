# 实例化驱动对象
import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)

# 打开目标网址
driver.get('http://localhost')
# 业务操作
driver.find_element_by_css_selector('.red').click()
driver.find_element_by_id('username').send_keys('18828828888')
driver.find_element_by_id('password').send_keys('1234567')
driver.find_element_by_id('verify_code').send_keys('8888')
driver.find_element_by_name('sbtbutton').click()
time.sleep(2)
msg_text = driver.find_element_by_class_name('layui-layer-content').text
print(msg_text)
time.sleep(2)
# 退出浏览器驱动
driver.quit()