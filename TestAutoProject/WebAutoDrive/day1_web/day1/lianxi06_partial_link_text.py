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
# partial_link_text --- 连续的部分超链接文本内容
# a.访问 新浪 网站 超链接  定位  点击


# 错误演示--不连续文本内容
# driver.find_element_by_partial_link_text("访问 网站").click()


# 5. 关闭浏览器--退出浏览器驱动对象   浏览器驱动对象调用quit()
time.sleep(2)
driver.quit()