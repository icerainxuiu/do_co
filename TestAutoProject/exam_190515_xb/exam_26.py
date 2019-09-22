# 需求：对《注册A.html》进行信息注册
# 账号：admin,
# 密码：123456，
# 电话：18600000000，
# 电子邮件：123@qq.com
# 要求： 1. 定位方式统一使用CSS定位
# 2. 暂停2秒钟点击注册用户A按钮
# 3. 暂停3秒钟后关闭浏览器

# 导包
import time

from selenium import webdriver

# 创建浏览器驱动对象
driver = webdriver.Chrome()
# 打开目标网页
driver.get("file:///C:/Users/icerain/Desktop/dc73be1f6e4741adb027a0320635b9f2/注册A.html")
# 最大化窗口
driver.maximize_window()
# 设置隐士等待20秒
driver.implicitly_wait(20)
# 查找帐号输入框并输入admin
element_user = driver.find_element_by_css_selector("#userA")
element_user.clear()
element_user.send_keys('admin')
# 查找密码输入框并输入123456
element_password = driver.find_element_by_css_selector("#passwordA")
element_password.clear()
element_password.send_keys('123456')
# 查找电话输入框并输入18600000000
element_tel = driver.find_element_by_css_selector("#telA")
element_tel.clear()
element_tel.send_keys('18600000000')
# 查找邮箱输入框并输入123@qq.com
element_email = driver.find_element_by_css_selector('#emailA')
element_email.clear()
element_email.send_keys('123@qq.com')
# 等待2秒
time.sleep(2)
# 点击注册用户A按钮
driver.find_element_by_css_selector('button[value="注册A"]').click()
# 等待3秒
time.sleep(3)
# 退出浏览器驱动
driver.quit()