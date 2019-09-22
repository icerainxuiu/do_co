# 1.导包
from selenium import webdriver
import time
# 2.创建浏览器驱动对象
# driver = webdriver.Firefox()
driver = webdriver.Chrome()

# 3.打开目标网页
driver.get("file:///C:/Users/icerain/Desktop/page/%E6%B3%A8%E5%86%8CA.html")

# driver.get("https://mail.qq.com")
# 4.业务操作
# 找到元素，操作元素，超链接文本
driver.find_element_by_partial_link_text("网站").click()
# driver.find_element_by_link_text("网站").click()
windows = driver.window_handles
driver.switch_to.window(windows[-1])
try:
    # 跳转至云计算登录页面，并输入账号密码点击登录
    driver.find_element_by_id("userName").send_keys("ruanjianceshi01")
    driver.find_element_by_id("userPasswd").send_keys("19879164")
    driver.find_element_by_name("configSubmit").click()
except:

    # 6.退出驱动
    # driver.quit()
    # 5.暂停3秒
    time.sleep(3)
    driver.get("https://mail.qq.com")

    windows = driver.window_handles
    driver.switch_to.window(windows[-1])
    # element = driver.find_element_by_id("kw")
    # element.click()
    # time.sleep(3)
    # element.send_keys("qq邮箱")
    # time.sleep(10)
    element = driver.find_element_by_id("u")
    element.click()

    element = driver.find_element_by_id("p")
    element.click()

    driver.find_element_by_id("login_button").click()
    time.sleep(5)

# 6.退出驱动
# driver.quit()

    # 6.退出驱动
    driver.quit()
# 5.暂停3秒
time.sleep(3)
driver.get("https://mail.qq.com")

# element = driver.find_element_by_id("kw")
# element.click()
# time.sleep(3)
# element.send_keys("qq邮箱")

windows = driver.window_handles
driver.switch_to.window(windows[-1])
# time.sleep(10)
element = driver.find_element_by_id("u")
element.click()

element = driver.find_element_by_id("p")
element.click()

driver.find_element_by_id("login_button").click()
time.sleep(5)

# 6.退出驱动
driver.quit()
