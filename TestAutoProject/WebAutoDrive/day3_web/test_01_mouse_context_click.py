# selenium webdriver
# -*- coding:utf-8 -*-
import time

# 0.导入自动化测试工具
from selenium import webdriver

# 1.打开浏览器
# 实例化浏览器驱动对象
# obj = 类名()
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()

# 2.输入网址
# 驱动对象调用get("协议://URL")
driver.get("file:///C:/Users/icerain/Desktop/page/%E6%B3%A8%E5%86%8CA.html")

# 3.业务操作
# 找到元素,操作元素
# 右键点击操作
# 实例化动作链的对象-- obj = 类名()
# ActionChains类需要导入
# 实例化时需要填入一个参数----浏览器驱动对象
# action = ActionChains(driver)
# action.context_click(driver.find_element_by_id("userA"))
# action.perform()
ActionChains(driver).context_click(driver.find_element_by_id("userA")).perform()

# 使用动作链对象调用动作方法--右键点击--context_click(目标元素对象)
# 调用--动作链对象的方法
# 参数--目标元素对象
# 返回--动作链对象


# 执行动作链动作--动作链对象调用perform()
# 动作链上的动作一定要执行perform才会起效



# 连写
# ActionChains(driver).context_click(target_element).perform()

# 4.关闭浏览器
# 驱动对象调用quit()
time.sleep(2)
driver.quit()
