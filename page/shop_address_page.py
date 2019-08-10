
"""
个人中心--收货地址页面
编写人:梁书辉

"""

from common.base import Base,open_browser
from page.login_page import LoginPage,url
import time


class ShopAddress(Base):
    country_loc = ('id', 'selCountries_0')  # 配送区域-国家
    # country_selector_china_value = '1'  # 配送区域-国家-中国
    province_loc = ('id', 'selProvinces_0')  # 配送区域-省份
    # province_selector_sichuan_value = '24'  # 配送区域-省份-四川省
    city_loc = ('id', 'selCities_0')  # 配送区域-城市
    # city_selector_chengdu_value = '271'  # 配送区域-城市-成都市
    region_loc = ('id', 'selDistricts_0')  # 配送区域-区
    # region_selector_wuhou_value = '2716'  # 配送区域-区-武侯区
    consignee_loc = ('id', 'consignee_0')  # 收货人姓名输入框
    email_loc=('id','email_0')#电子邮件地址
    address_loc = ('id', 'address_0')  # 详细地址输入框
    zip_code_loc=('id','zipcode_0')#邮政编码
    phone_loc = ('id', 'tel_0')  # 电话输入框
    mobile_loc=('id','mobile_0')#手机输入框
    shipping_address_loc=('link text','收货地址')#收货地址点击
    # 配送至这个地址按钮
    to_address_btn_loc = ('css selector', 'input[value="配送至这个地址"]')
    submit_loc=('name','submit')#点击新增收货地址
    button_loc=('name','button')

    """选择国家"""
    def choice_country(self, index):
        self.selector_by_index(self.country_loc, index)

    """选择省份"""
    def choice_province(self, index):
        self.selector_by_index(self.province_loc, index)

    '''选择城市'''
    def choice_city(self, index):
        self.selector_by_index(self.city_loc, index)

    '''选择区县'''
    def choice_region(self, index):
        self.selector_by_index(self.region_loc, index)

    '''输入收货人姓名'''
    def input_consignee(self, text):
        self.send_keys(self.consignee_loc, text)

    '''输入详细地址'''
    def input_address(self, address):
        self.send_keys(self.address_loc, address)

    '''输入电话'''
    def input_mobile(self,mobile):
        self.send_keys(self.mobile_loc,mobile)

    '''输入手机'''
    def input_phone(self, phone):
        self.send_keys(self.phone_loc, phone)

    '''点击配送至这个地址'''
    def click_address_btn(self):
        self.click_element(self.to_address_btn_loc)

        '''收货地址'''
    def click_shipping_address(self):
        self.click_element(self.shipping_address_loc)

        '''新增收货地址'''
    def click_submit(self):
        self.click_element(self.submit_loc)

        '''删除'''
    def click_button(self):
        self.click_element(self.button_loc)

        '''点击弹窗确认删除'''
    def click_accept(self):
        self.click_accept()


if __name__ == '__main__':
    driver=open_browser()
    driver.get(url)
    shop=ShopAddress(driver)
    login = LoginPage(driver)
    login.input_username('user1')
    login.input_password('123456')
    login.remmenber_password()
    login.submit()
    shop.click_shipping_address()
    time.sleep(3)
    shop.click_button()
    shop.operation_alert()
    time.sleep(3)
    shop.choice_country(1)
    time.sleep(3)
    shop.choice_province(1)
    time.sleep(3)
    shop.choice_city(1)
    time.sleep(3)
    shop.choice_region(1)
    time.sleep(3)
    shop.input_consignee('1234')
    shop.input_address('万人小区')
    shop.input_mobile('13712345678')
    shop.input_phone('13712345678')
    shop.click_submit()


    # shop.click_address_btn()