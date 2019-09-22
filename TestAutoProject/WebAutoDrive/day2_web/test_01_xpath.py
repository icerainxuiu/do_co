# # # 1.导包
# # from selenium import webdriver
# # import time
# # # 2.创建谷歌浏览器实例
# #
# # driver = webdriver.Chrome()
# # # 3.打开页面
# # driver.get("file:///C:/Users/icerain/Desktop/page/%E6%B3%A8%E5%86%8CA.html")
# # # 4.定位元素
# # elements = driver.find_elements_by_tag_name("input")
# # # 5.操作元素
# # elements[0].send_keys("admin")
# # time.sleep(2)
# # # 6.暂停3秒
# # elements[1].send_keys("123456")
# # time.sleep(3)
# # # 7.关闭浏览器
# # driver.quit()
# #
# # #
# # 需求：打开注册A.html页面，完成以下操作
# # 1).使用绝对路径定位用户名输入框，并输入：admin
# # 2).暂停2秒
# # 3).使用相对路径定位用户名输入框，并输入：123
# # 1.导包
# from selenium import webdriver
# import time
# # 2.创建谷歌浏览器实例
#
# driver = webdriver.Chrome()
# # 3.打开页面
# # driver.get("file:///C:/Users/icerain/Desktop/page/%E6%B3%A8%E5%86%8CA.html")
# driver.get("https://www.baidu/com")
# # 4.定位元素
# # elements = driver.find_elements_by_tag_name("input")
# # driver.find_element_by_xpath("/html/body/div/fieldset/form/p[1]/input").send_keys("admin")
# # time.sleep(3)
# # driver.find_element_by_xpath("/html/body/div/fieldset/form/p[2]/input").send_keys("123456")
# # driver.find_element_by_xpath("//*[@name='user' and @class='login']").send_keys("admin")
# # time.sleep(3)
# # driver.find_element_by_xpath("//*[@name='user-test' and @class='login-test']").send_keys("123")
# driver.find_element_by_css_selector("[type='password']").send_keys("admin")
#
# # # 5.操作元素
# # elements[0].send_keys("admin")
# # time.sleep(2)
# # # 6.暂停3秒
# # elements[1].send_keys("123456")
# time.sleep(3)
# # 7.关闭浏览器
# driver.quit()
#
# from bs4 import BeautifulSoup
# import requests
# import re
#
# if __name__ == '__main__':
#     target = "http://www.xbiquge.la/10/10489/4535761.html"
#     req = requests.get(url=target)
#     html = req.text
#     # bf = BeautifulSoup(html)
#     # texts = bf.find_all("body", class_="nodata")
#     pat = re.compile(r'[\u4e00-\u9fa5]+')
#     result = pat.findall(html)
#     result = str(result).replace("宋体", " ")
#     result = result.replace("','", "\t")
#     result = result.replace(",", "\n")
#     result = result.replace("' '", "")
#     result = result.replace("\n", " ")
#     result = result.replace(" ", "")
#     result = result.replace('"', "\n")
#     result = result.replace("'", "\n")
#     with open("1.txt", "w") as f:
#         f.write(str(result))
# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import requests
from  selenium import webdriver

if __name__ == "__main__":
    # driver = webdriver.Chrome()
    # driver.get('http://www.biqukan.com/1_1094/5403177.html')
    # target = 'http://www.biqukan.com/1_1094/5403177.html'
    # req = requests.get(url=target)
    # html = req.text
    # bf = BeautifulSoup(html)
    # texts = bf.find_all('div', class_='showtxt')
    print(texts[0].text.replace('\xa0' * 8, '\n\n'))
