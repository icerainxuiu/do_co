import time


from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("http://localhost")
driver.maximize_window()
driver.implicitly_wait(3)

# driver.find_element_by_css_selector(".red").click()
# time.sleep(3)
# driver.find_element_by_xpath("//span[contains(text(), '立即')]").click()
# # driver.find_element_by_xpath("").click()
# time.sleep(2)
# driver.find_element_by_xpath("//input[@placeholder='图像验证码']").send_keys("8888")
# time.sleep(2)
#
# driver.find_element_by_id("password").send_keys("123456")
# driver.find_element_by_id("password2").send_keys("123456")
# driver.find_element_by_xpath("//a[contains(text(),'同意协议')]").click()
# time.sleep(10)
#
#
driver.find_element_by_css_selector(".red").click()
driver.find_element_by_id("username").send_keys("18828828888")
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_id("verify_code").send_keys("8888")
driver.find_element_by_xpath("//a[contains(text(),'登')]").click()
driver.find_element_by_xpath("//a[contains(text(),'首')]").click()
driver.find_element_by_id("q").send_keys("小米")
driver.find_element_by_xpath("//button[contains(text(),'搜')]").click()
element = driver.find_element_by_xpath("//a[contains(text(),'小米手机')]")
print(element.text)
element.click()
driver.find_element_by_id("join_cart").click()
# driver.switch_to.frame("layui-layer2")
driver.switch_to.frame("layui-layer-iframe1")
# text = driver.find_element_by_css_selector("#addCartBox > div.colect-top
# > div > span").text
text = driver.find_element_by_xpath("//span[contains(text(),'添加成')]").text
print("text:", text)
driver.find_element_by_xpath("//a[contains(text(),'去购物车')]").click()
driver.find_element_by_xpath("//a[contains(text(),'去结')]").click()

driver.switch_to.default_content()
# driver.find_element_by_css_selector("#layui-layer1 > span > a").click()
try:
    driver.switch_to.frame(driver.find_element_by_xpath("//*[@id='layui-layer-iframe1']"))
    driver.find_element_by_xpath("//input[@name='consignee']").send_keys("张三三")
    select = Select(driver.find_element_by_id("province"))
    select.select_by_value("1")
    select = Select(driver.find_element_by_id("city"))
    select.select_by_value("2")
    select = Select(driver.find_element_by_id("district"))
    select.select_by_value("3")
    select = Select(driver.find_element_by_id("twon"))
    select.select_by_value("4")
    driver.find_element_by_id("address").send_keys("123街道")
    driver.find_element_by_xpath("//*[@name='mobile']").send_keys("18828828888")
    driver.find_element_by_xpath("//span[contains(text(),'保存收货')]").click()
except:
    pass
finally:
    driver.find_element_by_xpath("//span[contains(text(),'提交订')]").click()

    driver.switch_to.default_content()
    time.sleep(3)
    driver.quit()
