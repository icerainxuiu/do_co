"""
v1 不适用unittest 框架 编写测试用例，一个py文件就是一个测试用例
01. 测试TPshop的登录模块，账号不存在的情况
"""
from selenium import webdriver

# 初始化浏览器驱动对象，最大化浏览器窗口，设置隐式等待30秒
# 打开目标网页
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("http://localhost")
# 点击页面左上角的登录按钮，进入登录页面
# 输入不存在的账号密码及正确的万能验证码
driver.find_element_by_css_selector(".red").click()
driver.find_element_by_id("username").send_keys("14423331234")
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_name("verify_code").send_keys("8888")
# 点击登录按钮，获取错误提示信息
driver.find_element_by_xpath("//a[contains(text(), '登')]").click()
msg = driver.find_element_by_xpath("//div[contains(text(), '账号')]").text
print(msg)

# 推出浏览器驱动
driver.quit()