import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

url = 'http://www.xbiquge.la/10/10489/'
driver.get(url)
elements = driver.find_elements_by_xpath("//*[@id='list']/dl/dd")
len_url = len(elements)
list_url = list()
list_text = list()
for i in range(1, len_url):
    element = driver.find_element_by_xpath('//*[@id="list"]/dl/dd[%s]/a' % i)
    # print(element.get_attribute("href"))
    list_url.append(element.get_attribute("href"))
    list_text.append(element.text)

i = 0
for url1 in list_url:
    driver.get(url1)
    element2 = driver.find_element_by_xpath("//*[@id='content']")
    down_text = element2.text
    down_text = down_text.replace('\xa0'*4, '\n\n')
    with open('.\\down_load_txt\\%s%s.txt' % (i, list_text[i]), 'a+') as file_open:
        file_open.write(list_text[i] + '\n' + down_text + '\n')
        i += 1
    time.sleep(1)


driver.quit()
