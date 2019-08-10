
"""
浏览所有商品模块----测试用例
编写人:钟华龙

"""


import time
import unittest
from page.browse_page import HomePageBrowse,url
from common.base import open_browser

class TestBrowsePage(unittest.TestCase):
    """定义一个浏览所有商品类"""
    def setUp(self):
        """打开浏览器,打开被测网址"""
        self.driver = open_browser()
        self.login = HomePageBrowse(self.driver)
        self.login.open_url(url)

    def tearDown(self):
        """关闭浏览器"""
        self.login.close()

    """编写测试用例"""
    def test_browse_page_01(self):
        """测试用例01---成功浏览所有商品分类中的所有商品"""
        # 1.实例化对象
        hpg = HomePageBrowse(self.driver)
        # 2.浏览所有商品分类中的所有商品
        hpg.click_all_goods_01()


if __name__ == '__main__':
    unittest.main()





