# 1.导包
from selenium import webdriver
import time
# 2.创建浏览器驱动对象
driver = webdriver.Chrome()
# 3.打开网页
driver.get("file:///C:/Users/icerain/Desktop/page/%E6%B3%A8%E5%86%8CA.html")
# 4.业务操作
# 找到元素，操作元素,使用id查找元素
driver.find_element_by_id("userA").send_keys("admin")
time.sleep(3)
driver.find_element_by_id("passwordA").send_keys("123456")


# 5.暂停3秒
time.sleep(3)
# 6.退出驱动
driver.quit()
