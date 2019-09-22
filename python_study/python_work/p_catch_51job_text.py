from selenium import webdriver

driver = webdriver.Chrome()

driver.maximize_window()
driver.implicitly_wait(10)
url = ""
driver.get(url=url)

elements = driver.find_elements_by_xpath("//")

list_text = list()
for element in elements:
    list_text.append(element.text)

with open("./a.txt", 'w') as f:
    f.write(str(list_text))


