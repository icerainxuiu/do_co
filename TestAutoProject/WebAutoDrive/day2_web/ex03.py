import time

from selenium import webdriver



"""
3. 打开TPshop网站首页，完成登录操作，具体步骤如下：
    1. 点击页面顶部的‘登录’链接，进入登录页面
    2. 输入用户名：13012345678
    3. 输入密码：123456
    4. 输入错误的验证码：0000
    5. 点击登录按钮
    6. 获取提示框中的消息内容
    7. 点击提示框的确定按钮
    8. 重新输入正确的验证码：8888
    9. 点击登录按钮
    10. 暂停5秒
    11. 打印当前页面的标题
    要求：只能使用Xpath和CSS定位方式，在浏览器窗口最大化的状态下操作
"""
driver = webdriver.Chrome()
driver.get("http://localhost")
driver.maximize_window()
driver.find_element_by_css_selector(".red").click()
driver.find_element_by_xpath("//*[@id='username']").send_keys("13012345678")
driver.find_element_by_xpath("//*[@id='password']").send_keys("123456")
element = driver.find_element_by_xpath("//*[@id='verify_code']")
element.send_keys("0000")
driver.find_element_by_xpath("//a[contains(text(),'登')]").click()
time.sleep(3)
text = driver.find_element_by_css_selector("#layui-layer1 > div.layui-layer-content.layui-layer-padding").text
print('text', text)
driver.find_element_by_xpath("//*[@id='layui-layer1']/div[3]/a").click()
time.sleep(5)
element.clear()
element.send_keys("8888")
time.sleep(5)

driver.find_element_by_xpath("//a[contains(text(),'登')]").click()
time.sleep(5)
title = driver.title
print('title', title)
driver.quit()