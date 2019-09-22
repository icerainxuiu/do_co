import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3)
driver.get("file:///C:/Users/icerain/Desktop/page/注册A.html")
# driver.find_element_by_id("alerta").click()
# driver.find_element_by_id("confirma").click()
driver.find_element_by_id("prompta").click()
time.sleep(3)
alert = driver.switch_to.alert
# alert.accept()
alert.dismiss()
time.sleep(2)
driver.quit()