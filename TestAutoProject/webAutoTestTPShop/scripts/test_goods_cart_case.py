import time
import unittest

from parameterized import parameterized

from page.goods_detail_page import GoodsDetailProxy
from page.goods_search_page import GoodsProxy
from page.index_page import IndexProxy
from utils.data_list import data_goods_join_cart
from utils.utils import DriverUtil, switch_iframe


# 测试商品加入购物车功能
class TestGoodsCart(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # 实例化驱动 对象
        cls.driver = DriverUtil.get_driver()
        # 实例化首页业务操作对象
        cls.index_proxy = IndexProxy()
        # 实例化商品搜索页对象
        cls.goods_proxy = GoodsProxy()
        # 实例化商品详情页对象
        cls.goods_detail_proxy = GoodsDetailProxy()

    @classmethod
    def tearDownClass(cls) -> None:
        DriverUtil.quit_driver()

    def setUp(self) -> None:
        self.driver.get('http://localhost')

    def tearDown(self) -> None:
        time.sleep(2)

    # 数据驱动测试商品添加至购物车
    @parameterized.expand(data_goods_join_cart())
    def test_goods_join_cart_result(self, goods_name, expect):
        # 首页业务对象调用输入商品名称点击搜索业务
        self.index_proxy.go_click_search(goods_name)
        # 商品搜索页对象查找商品并点击进入详情页业务
        self.goods_proxy.search_proxy(goods_name)
        # 商品详情页点击加入购物车
        self.goods_detail_proxy.join_cart_proxy()
        # 调用封装的切换frame方法
        switch_iframe()
        # 调用商品详情页判断是否添加成功业务
        result = self.goods_detail_proxy.is_success_result(expect)
        # 断言实际和实际是否相符
        self.assertTrue(result)

