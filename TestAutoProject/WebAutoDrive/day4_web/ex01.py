import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

"""
1. 打开TPshop网站首页，完成以下操作：
    1. 点击‘登录’跳转到登录页面
    2. 输入用户名、密码和万能验证码，点击登录按钮进入后台管理页面
    3. 选择‘账户设置’下的‘收货地址’选项
    4. 点击地址管理下的‘增加新地址’按钮
    5. 输入地址信息，收货地址选择‘上海市-市辖区-浦东新区-三林镇’，其他选项任意输入
    6. 点击‘保存收货地址’按钮
    7. 关闭当前窗口
    要求：
        1. 每执行一个操作暂停2秒，方便观看效果
        2. 在浏览器窗口最大化的状态下操作，设置隐式等待为30秒
"""
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("http://localhost")
driver.find_element_by_xpath("//a[contains(text(),'登录')]").click()
time.sleep(2)
driver.find_element_by_id("username").send_keys("18828828888")
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_id("verify_code").send_keys("8888")
driver.find_element_by_name("sbtbutton").click()
time.sleep(2)
ActionChains(driver).move_to_element(driver.find_element_by_xpath("//span[contains(text(),'账户设置')]")).perform()
driver.find_element_by_xpath("//a[contains(text(),'收货地址')]").click()
time.sleep(2)
driver.find_element_by_xpath("//span[contains(text(),'增加新地址')]").click()
time.sleep(2)
driver.switch_to.frame("layui-layer-iframe100001")
driver.find_element_by_name("consignee").send_keys("李四四")
select = Select(driver.find_element_by_id("province"))
select.select_by_value("10543")

select = Select(driver.find_element_by_id("city"))
select.select_by_value("10544")
# cookies = driver.get_cookies()
select = Select(driver.find_element_by_id("district"))
select.select_by_value("10678")

select = Select(driver.find_element_by_id("twon"))
select.select_by_value("10701")

driver.find_element_by_id("address").send_keys("很好5号")
driver.find_element_by_name("mobile").send_keys("18828828888")
time.sleep(2)
driver.find_element_by_xpath("//span[contains(text(),'保存收货地址')]").click()
# print(cookies)
# time.sleep(2)
# driver.add_cookie({"name": "PHPSESSID","value": "hgc65ghn1gb1v3dm4b5c2cb631"})
# print(driver.get_cookies())

time.sleep(2)
driver.close()
time.sleep(2)
driver.quit()
