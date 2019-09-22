from appium import webdriver

def init_driver():
    desired_caps = dict()
    # 平台的名字，大小写无所谓，不能乱写
    desired_caps['platformName'] = 'android'
    # 平台的版本，（5.4.3 可以写 5.4.3，5.4，5）
    desired_caps['platformVersion'] = '5.1'
    # 设备的名字，随便写，不能乱写(android和ios的区别)
    desired_caps['deviceName'] = '1'
    # 要打开的应用程序
    desired_caps['appPackage'] = 'com.android.mms'
    # 要打开的界面
    desired_caps['appActivity'] = '.ui.ConversationList'

    return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)