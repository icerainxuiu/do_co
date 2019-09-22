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
# find_elements_by_xxx
# 定位页面上的第二个输入框input标签  密码A  123456

# a.定位到页面上所有的input标签

# b.从中选出第二个,索引为1的元素对象

# c.输入操作


# 5. 关闭浏览器--退出浏览器驱动对象   浏览器驱动对象调用quit()
time.sleep(2)
driver.quit()