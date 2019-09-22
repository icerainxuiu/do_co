# 自动下载文件
import time
import unittest

from selenium import webdriver


class TestDemo(unittest.TestCase):
    def setUp(self) -> None:
        # 创建一个实例，用于存放自定义配置
        profile = webdriver.FirefoxProfile()
        # 指定下载路径
        profile.set_preference('browser.download.dir', '\\d:iDownload')
        # 设置成2标识使用自定义下载路径
        profile.set_preference('browser.download.folderList', 2)
        profile.set_preference('browser.helpApps.alwaysAsk.force', False)
        profile.set_preference('browser.download.manager.showWhenStarting', False)
        profile.set_preference('browser.download.manager.useWindow', False)
        profile.set_preference('browser.download.manager.focusWhenStarting', False)
        profile.set_preference('browser.download.manager.alertOnEXEOpen', False)

