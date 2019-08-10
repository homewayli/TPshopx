
"""
个人收货中心--收货地址--测试用例

编写人:梁书辉

"""

import ddt as ddt


import time
import unittest
from page.login_page import LoginPage,url
from common.base import open_browser
from common.operationexcel import OperationExcel
from page.shop_address_page import ShopAddress


class TestAddress(unittest.TestCase):
    def setUp(self) -> None:
        """打开浏览器,打开被测网址"""
        driver = open_browser()
        self.login = LoginPage(driver)
        self.login.open_url(url)
        self.login.input_username("user1")
        self.login.input_password("123456")
        self.login.submit()
        self.shopaddress=ShopAddress(driver)
    #     实例化


    def tearDown(self) -> None:
        """关闭浏览器"""
        self.login.close()

        '''编写测试用例'''
    def test_shop_address(self):
        """成功新增收货地址"""
        self.shopaddress.click_shipping_address()
        time.sleep(3)
        # self.shopaddress.click_button()
        # self.shopaddress.operation_alert()
        # time.sleep(3)
        self.shopaddress.choice_country(1)
        time.sleep(3)
        self.shopaddress.choice_province(1)
        time.sleep(3)
        self.shopaddress.choice_city(1)
        time.sleep(3)
        self.shopaddress.choice_region(1)
        time.sleep(3)
        self.shopaddress.input_consignee('1234')
        self.shopaddress.input_address('万人小区')
        self.shopaddress.input_mobile('13712345678')
        self.shopaddress.input_phone('13712345678')
        self.shopaddress.click_submit()
        time.sleep(5)
        result_loc = ("id", "consignee_0")
        result = self.shopaddress.get_attribute(result_loc,"value")
        print(result)
        now = time.strftime("%Y_%m_%d %H_%M_%S")
        file_path = f"../image/{now}.jpg"
        try:
            self.assertEqual(result,"1234")
        except AssertionError:
            self.login.screenshot(file_path)
            raise AssertionError





    # driver = open_browser()
    # driver.get(url)
    # shop = ShopAddress(driver)
    # login = Login(driver)
    # login.input_username('user1')
    # login.input_password('123456')
    # login.remember_password()
    # login.submit()
    # shop.click_shipping_address()
    # shop.choice_country(1)
    # shop.choice_province(1)
    # shop.choice_city(1)
    # shop.choice_region(1)
    # shop.input_consignee('1234')
    # shop.input_address('万人小区')
    # shop.input_mobile('13712345678')

if __name__ == '__main__':
    unittest.main()