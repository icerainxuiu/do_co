import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
cookie_dict = {"name":"BDUSS","value":"lBvV1lQdX42aWtCQm82fkRyZ0lib0xTVzktbEJmZy1Xdm5CTHg3RVNZdTBMZlZjSUFBQUFBJCQAAAAAAAAAAAEAAAAiOKTqdGVzdGl0Y2FzdAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALSgzVy0oM1cY"}
driver.add_cookie(cookie_dict)
driver.refresh()
time.sleep(12)

