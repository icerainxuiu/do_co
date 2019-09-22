import unittest
import logging

from selenium import webdriver

logging.basicConfig(level=logging.INFO,filename='./log.txt',filemode='a',
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s:%(message)s')


class TestSoGouSearch(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def testSoGouSearch(self):
        logging.info(u"===========搜索===========")
        url = "http://www.sogou.com"
        self.driver.get(url)
        logging.info(u"访问sogou首页")
        self.driver.find_element_by_id("query").send_keys(u"光荣之路自动化测试")
        logging.info(u"在输入框中输入内容关键字串'光荣之路自动化测试'")
        self.driver.find_element_by_id("stb").click()
        logging.info(u"单机搜索按钮")
        logging.info(u"==========测试用例执行完成===========")

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
