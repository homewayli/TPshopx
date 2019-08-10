"""封装注册页面业务层"""
import time

from page.register_page import Logonpage
import unittest
from common.base import open_browser

from common.constructdata import Constructdata
construdata=Constructdata()





"""
注册模块---测试用例
编写人:廖松林

"""

class Test_logon(unittest.TestCase):
    def setUp(self):
        driver=open_browser()#打开浏览器
        self.logonpage=Logonpage(driver)#实例化类
        self.logonpage.open_url("http://ecshop.itsoso.cn/user.php?act=register")#打开网页


    def tearDown(self):
        self.logonpage.close()#关闭浏览器
    def test(self):
        """随即生成数据注册成功"""
        name = Constructdata.random_username()  # 将随机生成的名字保存
        self.logonpage.input_username(name)#将保存好的随机名字填入
        time.sleep(5)
        self.logonpage.input_email(construdata.random_email())#随机生成邮箱
        time.sleep(5)
        password = construdata.random_password()  # 将随机生成的密码保存
        self.logonpage.input_password(password)
        time.sleep(3)
        self.logonpage.input_conform_password(password)#确认密码
        time.sleep(3)
        self.logonpage.input_phone(construdata.random_mobile())#输入手机号
        self.logonpage.tishimima(construdata.random_question())#选择密码提示问题
        self.logonpage.input_answer(construdata.random_answer())#输入密码问题答案
        time.sleep(3)
        self.logonpage.click_radio()  # 选着单选框
        self.logonpage.click_logon()  # 点击立即注册
        time.sleep(5)
        try:
            self.assertEqual(name,self.logonpage.get_now_name(),msg="注册名和登录名不一致" )  # 断言登录是否成功
        except AssertionError:
            print("注册未成功")
            raise AssertionError




if __name__ == '__main__':
    unittest.main()





