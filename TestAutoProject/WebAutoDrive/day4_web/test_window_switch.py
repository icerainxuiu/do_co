import time

from selenium import webdriver

# ʵ����������������󣬲��������󻯺�������ʽ�ȴ�10��
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
# ��ע��ʵ��ҳ�� �ҵ�ע��Aҳ�沢���
driver.get("file:///C:/Users/icerain/Desktop/page/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html")
driver.find_element_by_id("ZCA").click()
# ��ȡ�򿪺����������ھ�������л����´��ں��ҵ��˺����������admin1
handle_window = driver.window_handles
driver.switch_to.window(handle_window[-1])
driver.find_element_by_id("userA").send_keys("admin1")
time.sleep(2)
# �л���ԭ���ڲ��ҵ������˺����������admin
driver.switch_to.window(handle_window[0])
driver.find_element_by_id("user").send_keys("admin")
time.sleep(2)
# �л����´��ڲ��رյ�ǰ����
driver.switch_to.window(handle_window[-1])
driver.close()
# �ر������
time.sleep(2)
driver.quit()
