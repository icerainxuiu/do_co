import time

from selenium import webdriver

"""
2. 对TPshop网站，使用cookie方式跳过验证码登录系统。[了解]
	关键cookie  "PHPSESSID"  "user_id"  "uname"
"""

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("http://localhost")
#
# driver.find_element_by_xpath("//a[contains(text(),'登录')]").click()
# time.sleep(2)
# driver.find_element_by_id("username").send_keys("18828828888")
# driver.find_element_by_id("password").send_keys("123456")
# driver.find_element_by_id("verify_code").send_keys("8888")
# driver.find_element_by_name("sbtbutton").click()
# time.sleep(2)
# time.sleep(2)
driver.add_cookie({"name":"uname","value":"18828828888"})
driver.add_cookie({"name":"user_id","value":"2593"})
driver.add_cookie({"name":"PHPSESSID","value":"7vg9a3lkugv6mfs7cculo6q5v3"})
time.sleep(2)
driver.refresh()
time.sleep(2)
driver.find_element_by_xpath("//a[contains(text(),'我的订单')]").click()
time.sleep(8)
print(driver.get_cookies())
driver.quit()