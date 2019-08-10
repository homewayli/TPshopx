
"""
下单支付页面
编写人:黎洪伟

"""

import time
from common.base import Base
from page.login_page import LoginPage
from common.base import open_browser


url="http://ecshop.itsoso.cn/goods.php?id=85"


class OrderPayment(Base):  # 继承base类
    """封装表现层--制作定位器"""
    # 立即购买按钮
    buy_loc = ("css selector", "#ECS_FORMBUY>ul>li.padd>table>tbody>tr>td.td1>a>img")
    # 去结算按钮
    go_to_pay_loc = ("xpath", "/html/body/div[6]/div[1]/table/tbody/tr/td[2]/a/img")
    # 配送方式--申通快递按钮
    ST_loc = ("xpath", "//*[@id='shippingTable']/tbody/tr[2]/td[1]/input")
    # 配送方式--邮局平邮按钮
    YouJu_loc = ("xpath", "//*[@id='shippingTable']/tbody/tr[3]/td[1]/input")
    # 配送方式--运费到付按钮
    YunFei_loc = ("xpath","//*[@id='shippingTable']/tbody/tr[4]/td[1]/input")
    # 支付方式-天宫收银按钮
    TianGong_loc = ("css selector", "#yunqi_payment")
    # 支付方式-天宫收银-支付宝按钮
    Ali_pay_loc = ("css selector", "#alipay")
    # 支付方式-天宫收银-微信按钮
    Wechat_pay_loc = ("css selector", "#wxpay")
    # 支付方式--余额支付
    balance_pay_loc = ("xpath", "//*[@id='paymentTable']/tbody/tr[4]/td[1]/input")
    # 支付方式--银行汇款/转账
    Bank_pay_loc = ("xpath", "//*[@id='paymentTable']/tbody/tr[5]/td[1]/input")
    # 商品包装--不要包装
    no_package_loc = ("xpath", "//*[@id='packTable']/tbody/tr[2]/td[1]/input")
    # 商品包装--要包装
    package_loc = ("xpath", "//*[@id='packTable']/tbody/tr[3]/td[1]/input")
    # 祝福贺卡--不要贺卡
    no_card_loc = ("xpath", "//*[@id='cardTable']/tbody/tr[2]/td[1]/input")
    # 祝福贺卡--祝福贺卡
    need_card_loc = ("xpath", "//*[@id='cardTable']/tbody/tr[3]/td[1]/input")
    # 提交订单按钮
    submit_order_loc = ("xpath", "//*[@id='theForm']/div[15]/div[2]/input[1]")
    # 收货人信息--省份
    provice_loc = ("id", "selProvinces_0")
    # 收货人信息--市
    city_loc = ("id", "selCities_0")
    # 收货人信息--区
    district_loc = ("id","selDistricts_0")
    # 收货人信息--收货人姓名
    consignee_loc = ("id", "consignee_0")
    # 收货人信息--电子邮箱地址
    email_loc = ("id", "email_0")
    # 收货人信息--详细地址
    details_address_loc = ("id", "address_0")
    # 收货人信息--邮政编码
    zip_code_loc = ("id", "zipcode_0")
    # 收货人信息--电话
    tel_loc = ("id", "tel_0")
    # 收货人信息--手机
    mobile_loc = ("id", "mobile_0")
    # 配送至这个地址
    deliver_address_loc = ("css selector", "td[colspan='4']>input")
    # 不打算登录直接购买
    direct_buy_loc = ("class name","bnt_blue_2")
    # 生产订单号的定位器
    order_num_loc = ("css selector","body>div:nth-child(7)>div>h6>font")
    # 商品页面---请登录按钮
    login_submit_loc = ("css selector","#ECS_MEMBERZONE>a:nth-child(2)")
    # 会员登录---用户名输入框
    username_loc = ("xpath","/html/body/div[6]/div[1]/form/table/tbody/tr[1]/td[2]/input")
    # 会员登录---密码输入框
    password_loc = ("xpath","/html/body/div[6]/div[1]/form/table/tbody/tr[2]/td[2]/input")
    # 会员登录---立即登录
    login_now_loc = ("css selector","body>div.usBox.clearfix>div.usBox_1.f_l>form>table>tbody>tr:nth-child(4)>td:nth-child(2)>input.us_Submit")





    """封装操作层"""
    def click_buy(self):
        """点击立即购买"""
        self.click_element(self.buy_loc)

    def click_go_to_pay(self):
        """点击去结算"""
        self.click_element(self.go_to_pay_loc)

    def choose_provice(self,index):
        """选择省份"""
        self.selector_by_index(self.provice_loc,index)

    def choose_city(self,index):
        """选择市区"""
        self.selector_by_index(self.city_loc,index)

    def choose_district(self,index):
        """选择区"""
        self.selector_by_index(self.district_loc,index)

    def input_consignee(self,text):
        """填写收货人姓名"""
        self.send_keys(self.consignee_loc,text)

    def input_email(self,text):
        """填写电子邮件地址"""
        self.send_keys(self.email_loc,text)

    def input_details_address(self,text):
        """填写详细地址"""
        self.send_keys(self.details_address_loc,text)

    def input_zip_code(self,text):
        """填写邮政编码"""
        self.send_keys(self.zip_code_loc,text)

    def input_tel(self,text):
        """填写电话号码"""
        self.send_keys(self.tel_loc,text)

    def input_mobile(self,text):
        """填写手机号码"""
        self.send_keys(self.mobile_loc,text)

    def click_delivery_address(self):
        """点击配送至该地址"""
        self.click_element(self.deliver_address_loc)


    def click_ST(self):
        """点击申通"""
        self.click_element(self.ST_loc)

    def click_YouJu(self):
        """点击邮局"""
        self.click_element(self.YouJu_loc)

    def click_YouFei(self):
        """点击邮费到付"""
        self.click_element(self.YunFei_loc)

    def click_TianGong(self):
        """点击天工收银"""
        self.click_element(self.TianGong_loc)

    def click_Ali_pay(self):
        """点击支付宝支付"""
        self.click_element(self.Ali_pay_loc)

    def click_Wechat_pay(self):
        """点击微信支付"""
        self.click_element(self.Wechat_pay_loc)

    def click_balance_pay(self):
        """点击余额支付"""
        self.click_element(self.balance_pay_loc)

    def click_bank_pay(self):
        """点击银行汇款/转账"""
        self.click_element(self.Bank_pay_loc)

    def click_no_package(self):
        """点击不要包装"""
        self.click_element(self.no_package_loc)

    def click_package(self):
        """点击精品包装"""
        self.click_element(self.package_loc)

    def click_no_card(self):
        """点击不要贺卡"""
        self.click_element(self.no_card_loc)

    def click_nedd_card(self):
        """点击要贺卡"""
        self.click_element(self.need_card_loc)

    def click_submit_order(self):
        """点击提交订单"""
        self.click_element(self.submit_order_loc)

    def click_direct_buy(self):
        """不登录点击直接购买"""
        self.click_element(self.direct_buy_loc)
    def get_order_num(self):
        """获取订单号"""
        self.order_num = self.get_tag_text(self.order_num_loc)
        print(self.order_num)
        return self.order_num
    def click_login_submit(self):
        """点击请登录按钮"""
        self.click_element(self.login_submit_loc)

    def input_username(self,text):
        """输入用户名"""
        self.send_keys(self.username_loc,text)

    def input_password(self,text):
        """输入密码"""
        self.send_keys(self.password_loc,text)

    def click_login_now(self):
        """点击立即登录"""
        self.click_element(self.login_now_loc)
        time.sleep(5)




if __name__ == '__main__':

    # driver = open_browser()
    # order_payment = OrderPayment(driver)
    # order_payment.open_url(url)
    # order_payment.click_buy()
    # order_payment.click_go_to_pay()
    # order_payment.click_direct_buy()
    # time.sleep(2)
    # order_payment.choose_provice(5)
    # time.sleep(2)
    # order_payment.choose_city(3)
    # time.sleep(2)
    # order_payment.choose_district(4)
    # time.sleep(2)
    # order_payment.input_consignee("刘德华")
    # time.sleep(2)
    # order_payment.input_email("liai@163.com")
    # time.sleep(2)
    # order_payment.input_details_address("成都市")
    # time.sleep(2)
    # order_payment.input_zip_code("98098")
    # time.sleep(2)
    # order_payment.input_tel("020-290139201")
    # time.sleep(2)
    # order_payment.input_mobile("109304329033")
    # order_payment.click_delivery_address()
    # time.sleep(2)
    # order_payment.click_ST()
    # time.sleep(2)
    # order_payment.click_YouJu()
    # time.sleep(2)
    # order_payment.click_YouFei()
    # time.sleep(2)
    # order_payment.click_TianGong()
    # time.sleep(2)
    # order_payment.click_Ali_pay()
    # time.sleep(2)
    # order_payment.click_Wechat_pay()
    # time.sleep(2)
    # order_payment.click_no_package()
    # time.sleep(2)
    # order_payment.click_package()
    # time.sleep(2)
    # order_payment.click_no_card()
    # time.sleep(2)
    # order_payment.click_nedd_card()
    # time.sleep(2)
    # order_payment.click_submit_order()
    # time.sleep(2)
    # order_payment.get_order_num()
    #
    # order_payment.close()
    driver = open_browser()
    order_payment = OrderPayment(driver)
    order_payment.open_url(url)
    order_payment.click_login_submit()
    order_payment.input_username("诸葛亮_9")
    order_payment.input_password("Test123456")
    order_payment.click_login_now()
    order_payment.click_buy()
    order_payment.click_go_to_pay()
    # order_payment.click_direct_buy()

    # order_payment.choose_provice(5)
    # time.sleep(2)
    # order_payment.choose_city(3)
    # time.sleep(2)
    # order_payment.choose_district(4)
    # time.sleep(2)
    # order_payment.input_consignee("刘德华")
    # time.sleep(2)
    # order_payment.input_email("liai@163.com")
    # time.sleep(2)
    # order_payment.input_details_address("成都市")
    # time.sleep(2)
    # order_payment.input_zip_code("98098")
    # time.sleep(2)
    # order_payment.input_tel("020-290139201")
    # time.sleep(2)
    # order_payment.input_mobile("109304329033")
    # order_payment.click_delivery_address()
    time.sleep(3)
    order_payment.click_ST()
    time.sleep(4)
    order_payment.click_YouJu()
    time.sleep(4)
    order_payment.click_YouFei()
    time.sleep(4)
    order_payment.click_TianGong()
    time.sleep(4)
    order_payment.click_Ali_pay()
    time.sleep(4)
    order_payment.click_Wechat_pay()
    time.sleep(4)
    order_payment.click_no_package()
    time.sleep(4)
    order_payment.click_package()
    time.sleep(4)
    order_payment.click_no_card()
    time.sleep(4)
    order_payment.click_nedd_card()
    time.sleep(4)
    order_payment.click_submit_order()
    time.sleep(4)
    order_payment.get_order_num()
    order_payment.close()







