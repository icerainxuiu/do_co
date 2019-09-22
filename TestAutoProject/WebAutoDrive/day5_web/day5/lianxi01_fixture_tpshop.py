import unittest

from selenium import webdriver


# 定义一个测试类，继承自TestCase
class TestTPShop(unittest.TestCase):

    def test_msg(self):
        # 初始化浏览器对象
        driver = webdriver.Chrome()
        # 最大化窗口
        driver.maximize_window()
        # 设置隐式等待30秒
        driver.implicitly_wait(30)
        # 打开目标网页
        driver.get("http://localhost")
        # 点击登录按钮
        driver.find_element_by_css_selector(".red").click()
        # 输入登录账号和密码，不输入验证码，点击登录按钮
        driver.find_element_by_id("username").send_keys("18828828888")
        driver.find_element_by_id("password").send_keys("123456")
        driver.find_element_by_name("sbtbutton").click()
        # 获取弹窗的提示信息
        text = driver.find_element_by_xpath("//div[contains(text(),'验证码')]").text
        print("text:", text)

        driver.quit()
