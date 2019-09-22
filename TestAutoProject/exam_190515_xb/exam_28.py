"""
需求：对TPshop/iweb_shop项目进行前台登录设计脚本
要求：
1. 使用unittest框架
2. 使用Fixture(setup、tearDown)
3. 浏览器最大化、隐式等待30秒
4. 使用断言判断登录用户是否为admin，不是则截屏保存图片
5. 图片命名格式为脚本执行时间
"""
# 导包
import time
import unittest

from selenium import webdriver


# 设置测试用例类，继承自unittest.TestCase类
class TestLogin(unittest.TestCase):
    # 设置类属性driver 用来保存浏览器驱动对象
    driver = None
    @classmethod
    def setUpClass(cls) -> None:
        # 测试登录模块需要的共同操作有：浏览器驱动对象，
        # 最大化窗口，设置30秒隐士等待，打开主页
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(30)
        cls.driver.get("http://localhost")

    # 在所有测试用例执行完成后退出浏览器驱动对象
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    # 测试登录之前的共同操作，点击登录按钮进入登录页面
    def setUp(self) -> None:
        self.driver.find_element_by_class_name('red').click()

    # 测试用例执行完，等待5秒用来查看测试用例执行情况
    def tearDown(self) -> None:
        time.sleep(5)

    # 登录测试用例
    def test_01_login(self):
        # 设置一个属性用来保存弹出框元素，初始设为None
        self.element = None
        # 查找输入框并输入相应的数据
        self.driver.find_element_by_id('username').send_keys('188288888')
        self.driver.find_element_by_id('password').send_keys('123456')
        self.driver.find_element_by_id('verify_code').send_keys('8888')
        # 点击登录按钮
        self.driver.find_element_by_name('sbtbutton').click()
        # 获取登录不成功的弹出框
        try:
            self.element = self.driver.find_element_by_class_name('layui-layer-content')
            # 如果有弹出框就打印弹出框信息，并截图保存
            print(self.element.text)
            self.driver.get_screenshot_as_file('./{}.png'.format(time.strftime("%Y%m%d%H%M%S")))
        except:
            pass
        # 判断是否有弹出框，如果没有，就说明登录成功
        if self.element is None:
            # 获取登录成功后的我的主页信息页登录的账号名
            home_name = self.driver.find_element_by_xpath(
                '//div[@class="mu-midd fl"]/a[@href="/Home/User/index.html"]').text
            try:
                # 判断登录的账号名是否等于admin
                self.assertEqual('admin', home_name)
            except Exception as e:
                # 不相等，截图保存，以用例执行的当前时间作为截图名称
                self.driver.get_screenshot_as_file(
                    './{}.png'.format(time.strftime("%Y%m%d%H%M%S")))
                # 继续抛出断言异常
                raise e
