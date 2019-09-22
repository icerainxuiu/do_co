import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://localhost")
time.sleep(1)
driver.maximize_window()

driver.find_element_by_css_selector(".red").click()
driver.find_element_by_id("username").send_keys("18828828888")
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_id("verify_code").send_keys("8888")
driver.find_element_by_xpath("//a[contains(text(),'登')]").click()
time.sleep(2)
driver.find_element_by_xpath("//a[contains(text(),'首')]").click()
time.sleep(2)
driver.find_element_by_xpath("//a[contains(text(),'我的订')]").click()
time.sleep(1)
windows = driver.window_handles
driver.switch_to.window(windows[-1])
driver.find_element_by_xpath("//a[contains(text(),'待付款')]").click()
driver.find_element_by_xpath("//a[contains(text(),'立即支')]").click()
windows = driver.window_handles
driver.switch_to.window(windows[-1])
time.sleep(1)
driver.find_element_by_xpath("//input[@id='input-ALIPAY-1' and @value='pay_code=cod']").click()
driver.find_element_by_xpath("//a[contains(text(),'确认支付方')]").click()
text = driver.find_element_by_xpath("//h3[contains(text(),'订单提交')]").text
print("text",text)
time.sleep(3)
driver.quit()