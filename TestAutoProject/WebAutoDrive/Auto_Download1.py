# encoding:utf-8
"""
使用单元测试方式自动化下载小说
"""
import unittest
import time
import ddt
from selenium import webdriver


@ddt.ddt
class AutoDownload(unittest.TestCase):
    """
    导入单元测试模块
    """

    @classmethod
    def setUpClass(cls) -> None:
        pass

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        time.sleep(1)
    # 打开需要下载的网页
    @ddt.file_data(".\\test_data_list.json")
    def test_auto(self, value):
        self.driver.get(value)
        title = self.driver.title
        self.url_list = list()
        self.name_list = list()
        self.elements = self.driver.find_elements_by_xpath(
            '//*[@id="list"]/dl/dd')
        self.len_elements = len(self.elements)
        for i in range(1, self.len_elements + 1):
            element = self.driver.find_element_by_xpath(
                '//*[@id="list"]/dl/dd[%s]/a' % i)
            self.url_list.append(element.get_attribute("href"))
            self.name_list.append(element.text)
        i = 0
        name = str(title.split("小说")[0])
        print("[%s]正在下载" % str)
        for url1 in self.url_list:
            self.driver.get(url1)
            element2 = self.driver.find_element_by_xpath("//*[@id='content']")
            down_text = element2.text
            down_text = down_text.replace('\xa0' * 4, '\n\n')
            with open('.\\%s.txt' % name, 'a+') as file_open:
                file_open.write(self.name_list[i] + '\n' + down_text + '\n')
                i += 1
            print("...已下载%.3f%%" % float(i / self.len_elements) + '\r', end='')
        print("【%s】已下载完" % name)

    def tearDown(self) -> None:
        self.driver.quit()

    @classmethod
    def tearDownClass(cls) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
