# 导入模块
from selenium import webdriver
import time

# 创建实例对象打开浏览器
driver = webdriver.Chrome()

# 打开网址get("协议://url")
driver.get("http://192.168.13.195")

# 操作业务

time.sleep(3)

# 关闭浏览器
driver.quit()


