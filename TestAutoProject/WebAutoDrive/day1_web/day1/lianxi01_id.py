# 1. 工具导进来--导包操作 webdriver
from selenium import  webdriver
import time
# 2. 打开浏览器--实例化一个浏览器驱动对象
# 谷歌浏览器
driver = webdriver.Chrome()
# driver = webdriver.Firefox()


# 3. 输入网址--浏览器驱动对象调用get("完整的网址字符串")
driver.get("file:///c:/user/Desktop/page/注册实例A.html")
driver.get("http://www.baidu.com")
# 4. 业务操作--元素定位和元素操作
# id 定位
# a.定位账号A,输入用户名:admin
driver.find_element_by_id("userA").send_keys("admin")


# b.定位密码A,输入密码:123456
driver.find_element_by_id("passwordA").send_keys("123456")

# 5. 关闭浏览器--退出浏览器驱动对象   浏览器驱动对象调用quit()
time.sleep(2)
driver.quit()