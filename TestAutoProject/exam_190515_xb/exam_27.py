"""
需求：对《注册实例.html》进行信息注册
账号：admin,
密码：123456，
电话：18600000000，
电子邮件：123@qq.com
要求：
1. 对注册《主界面、注册A、注册B》三个注册信息进行注册信息填写
2. 定位方式不限
3. 暂停3秒钟关闭浏览器
"""
# 导包
import time

from selenium import webdriver

# 初始化浏览器驱动对象
driver = webdriver.Chrome()
# 最大化窗口
driver.maximize_window()
# 设置隐士等待20秒
driver.implicitly_wait(20)
# 打开目标网页注册实例.html
driver.get("file:///C:/Users/icerain/Desktop/dc73be1f6e4741adb027a0320635b9f2/注册实例.html")
# 查找主界面并输入相应注册信息
element = driver.find_element_by_id('user')
element.clear()
element.send_keys('admin')

element = driver.find_element_by_id('password')
element.clear()
element.send_keys('123456')

element = driver.find_element_by_id('tel')
element.clear()
element.send_keys('18600000000')

element = driver.find_element_by_id('email')
element.clear()
element.send_keys('123@qq.com')
# 切换至注册A页面 并输入注册信息
driver.switch_to.frame('idframe1')
element = driver.find_element_by_id('userA')
element.clear()
element.send_keys('admin')

element = driver.find_element_by_id('passwordA')
element.clear()
element.send_keys('123456')

element = driver.find_element_by_id('telA')
element.clear()
element.send_keys('18600000000')

element = driver.find_element_by_id('emailA')
element.clear()
element.send_keys('123@qq.com')
# 切换回主页面
driver.switch_to.default_content()
# 切换至注册B页面并输入注册信息
driver.switch_to.frame(driver.find_element_by_name("myframe2"))
element = driver.find_element_by_id('userB')
element.clear()
element.send_keys('admin')

element = driver.find_element_by_id('passwordB')
element.clear()
element.send_keys('123456')

element = driver.find_element_by_id('telB')
element.clear()
element.send_keys('18600000000')

element = driver.find_element_by_id('emailB')
element.clear()
element.send_keys('123@qq.com')
# 切换回主页面
driver.switch_to.default_content()
# 等待3秒
time.sleep(3)
# 退出浏览器驱动
driver.quit()