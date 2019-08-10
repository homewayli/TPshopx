
"""
下单支付模块----测试用例

编写人:黎洪伟

"""

import time
import unittest
from page.login_page import LoginPage
from page.order_payment_page import OrderPayment,url
from common.base import open_browser
from common.constructdata import Constructdata


class TestOrderPayment(unittest.TestCase):
    def setUp(self):
        """打开浏览器,打开被测网址"""
        self.driver = open_browser()
        self.login = LoginPage(self.driver)
        self.login.open_url(url)
        self.cons = Constructdata()
    def tearDown(self):
        """关闭浏览器"""
        self.login.close()

    """编写测试用例"""

    def test_order_01(self):
        """用例1:不登录用户名直接购买商品下单支付成功"""
        # 1.实例化对象
        order_payment_1 = OrderPayment(self.driver)
        # 2.点击立即购买商品
        order_payment_1.click_buy()
        # 3.点击去结算
        order_payment_1.click_go_to_pay()
        # 4.点击不打算登录,直接购买
        order_payment_1.click_direct_buy()
        # 5.选择省份
        order_payment_1.choose_provice(4)
        time.sleep(1)
        # 6.选择市
        order_payment_1.choose_city(4)
        time.sleep(1)
        # 7.选择区
        order_payment_1.choose_district(3)
        time.sleep(1)
        # 8.填写收货人姓名
        order_payment_1.input_consignee(self.cons.random_username())
        time.sleep(1)
        # 9.填写电子邮件
        order_payment_1.input_email(self.cons.random_email())
        time.sleep(1)
        # 10.填写详细地址
        order_payment_1.input_details_address("成都市锦江区牛市口")
        time.sleep(1)
        # 11.填写邮政编码
        order_payment_1.input_zip_code(self.cons.random_mobile())
        time.sleep(1)
        # 12.填写电话号码
        order_payment_1.input_tel(self.cons.random_mobile())
        time.sleep(3)
        # 13.填写手机号码
        order_payment_1.input_mobile(self.cons.random_mobile())
        time.sleep(4)
        # 14.点击配送至这个地址
        order_payment_1.click_delivery_address()
        time.sleep(2)
        # 15.选择申通快递
        order_payment_1.click_ST()
        time.sleep(3)
        # 16.选择天工收银
        order_payment_1.click_TianGong()
        time.sleep(3)
        # 17.选择微信支付
        order_payment_1.click_Wechat_pay()
        time.sleep(3)
        # 18.选择不要包装
        order_payment_1.click_no_package()
        time.sleep(2)
        # 19.选择不要贺卡
        order_payment_1.click_no_card()
        time.sleep(5)
        # 20.点击提交订单
        order_payment_1.click_submit_order()
        time.sleep(2)
        # 21.获取并打印订单
        order_num =  order_payment_1.get_order_num()
        time.sleep(2)
        try:
            self.assertEqual(order_num,order_num)
        except AssertionError:
            raise AssertionError

    def test_order_02(self):
        """点开商品后,用户直接登录后购买商品下单支付成功"""
        # 1.实例化对象
        order_payment_2 = OrderPayment(self.driver)
        time.sleep(3)
        # 2.会员登录点击请登录
        order_payment_2.click_login_submit()
        time.sleep(4)
        # 3.输入用户名
        order_payment_2.input_username("周杰伦_1")
        # 4.输入密码
        order_payment_2.input_password("Test123456")
        # 5.点击立即登录
        order_payment_2.click_login_now()
        # 6.点击立即购买
        order_payment_2.click_buy()
        #7.点击去结算
        order_payment_2.click_go_to_pay()
        # 8.点击邮费到付
        order_payment_2.click_YouFei()
        time.sleep(3)
        # 9.选择天工收银
        order_payment_2.click_TianGong()
        time.sleep(3)
        # 10.选择微信支付
        order_payment_2.click_Ali_pay()
        time.sleep(3)
        # 11.选择不要包装
        order_payment_2.click_package()
        time.sleep(2)
        # 12.选择不要贺卡
        order_payment_2.click_nedd_card()
        time.sleep(5)
        # 13.点击提交订单
        order_payment_2.click_submit_order()
        time.sleep(2)
        # 14.获取并打印订单
        order_num = order_payment_2.get_order_num()
        time.sleep(2)
        try:
            self.assertEqual(order_num, order_num)
        except AssertionError:
            raise AssertionError


if __name__ == '__main__':
    unittest.main()








