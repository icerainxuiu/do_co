# 1. 工具导进来--导包操作 webdriver
from selenium import  webdriver
import time
# 2. 打开浏览器--实例化一个浏览器驱动对象
# 谷歌浏览器
driver = webdriver.Chrome()
# driver = webdriver.Firefox()


# 3. 输入网址--浏览器驱动对象调用get("完整的网址字符串")
driver.get("注册A页面")

# 4. 业务操作--元素定位和元素操作
# class_name
# a.电话号码 18611111111


# b.电子邮箱中   123@qq.com
# 只能填写一个类名


# 错误演示 输入多个类名
# driver.find_element_by_class_name("emailA dzyxA").send_keys("123@qq.com")

# 5. 关闭浏览器--退出浏览器驱动对象   浏览器驱动对象调用quit()
time.sleep(2)
driver.quit()