from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://localhost")
driver.quit()