import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://localhost")
driver.maximize_window()
cookies = driver.get_cookies()
print(cookies)
time.sleep(2)
driver.add_cookie({"name":"PHPSESSID","value":"a1fjs5nberdbcd76ng3shi1ie6","uname":"18828828888","user_id":"2593"})
driver.refresh()
time.sleep(5)
driver.quit()