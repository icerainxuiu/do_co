# 1.导包
# -*- coding:utf-8 -*-
from selenium import webdriver
import time
# 2.创建谷歌浏览器实例

driver = webdriver.Chrome()
# 3.打开页面,调用get获取("协议：url")
driver.get("file:///C:/Users/icerain/Desktop/page/%E6%B3%A8%E5%86%8CA.html")
# driver.get("http://192.168.13.195")
# 4.定位元素,绝对路径

# driver.find_element_by_xpath("/html/body/div/fieldset/form/p[1]/input").send_keys("admin")
# 5.操作元素
# time.sleep(2)
# # 6.暂停3秒
#
# # 相对路径，定位元素
# # driver.find_element_by_xpath('//*[@id="userA"]').send_keys("1234")
# # driver.find_element_by_xpath('//*[@placeholder="请输入用户名"]').send_keys("1234")
# # driver.find_element_by_xpath('//*[@name="userA"]').send_keys("1234")
# # driver.find_element_by_xpath("//*[@name='user' and @class='login']").send_keys("admin")
# # driver.find_element_by_xpath('//p[@id="p1"]/input[@name="user"]').send_keys("password")
# # driver.find_element_by_xpath("//a[text()='新浪']").click()
# # driver.find_element_by_xpath("//input[contains(@id,'user')]").send_keys("admin")
# # driver.find_element_by_xpath("//input[starts-with(@id,'user')]").send_keys("admin")
# # driver.find_element_by_css_selector("#userA").send_keys("admin")
# # time.sleep(2)
# # driver.find_element_by_css_selector(".telA").send_keys("18822222222")
# # time.sleep(2)
# # driver.find_element_by_css_selector("input[id='userA']").send_keys("admin")
# # time.sleep(2)
# # driver.find_element_by_css_selector("button").click()
# # driver.find_element_by_css_selector("p[id='pa']>input").send_keys("adminadmin")
# # driver.find_element_by_css_selector("p#pa input").send_keys("adm123")
# # driver.find_element_by_id("userA").send_keys("admin")
# # driver.find_element_by_id("passwordA").send_keys("123456")
# # driver.find_element_by_id("telA").send_keys("18811111111")
# # driver.find_element_by_name("emailA").send_keys("3432@qq.com")
# # element = driver.find_element_by_id("telA")
# # element.clear()
# # time.sleep(3)
# # element.send_keys("18800000000")
# # driver.find_element_by_tag_name("button").click()
# driver.maximize_window()
# time.sleep(2)
# # driver.set_window_position(300, 300)
# # time.sleep(2)
# # for i in range(600):
# #     for j in range(600):
# #         driver.set_window_position(i, j)
# #         time.sleep(0.01)
# driver.find_element_by_link_text("登录").click()
# time.sleep(2)
# driver.back()
# time.sleep(2)
# driver.forward()
# time.sleep(2)
# driver.refresh()
# time.sleep(2)
# 7.关闭浏览器
# title = driver.title
# print("title:", title)
# my_url = driver.current_url
# print("url:", my_url)
time.sleep(3)
size = driver.find_element_by_id("userA").size
print("size", size)
text = driver.find_element_by_tag_name("a").text
print("text:", text)
url = driver.find_element_by_tag_name("a").get_attribute("href")
print("url:", url)
is_displayed = driver.find_element_by_tag_name("span").is_displayed()
print("is_displayed:", is_displayed)
is_enable = driver.find_element_by_id("cancelA").is_enabled()
print("is_enable:", is_enable)
is_select = driver.find_element_by_id("lyA").is_selected()
print("is_select", is_select)
driver.quit()

#
