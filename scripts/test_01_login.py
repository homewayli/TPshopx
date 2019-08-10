
"""
登录模块---测试用例
编写人:廖松林

"""
import time
import unittest
import ddt
from page.login_page import LoginPage,url
from common.base import open_browser
from common.operationexcel import OperationExcel
oper_excel=OperationExcel(r"D:\test\ECshop_第三组\data\testdata01.xlsx")
test_data=oper_excel.get_data_for_dict()


@ddt.ddt
class TestLogin(unittest.TestCase):
    def setUp(self):
        """打开浏览器,打开被测网址"""
        driver=open_browser()
        self.login=LoginPage(driver)
        self.login.open_url(url)
    def tearDown(self):
        """关闭浏览器"""
        self.login.close()

    """编写测试用例"""
    @ddt.data(*test_data)
    def test_login_01(self,data:dict):
        """参数化不记录账号登录"""
        self.login.input_username(data["username"])#参数化账号
        time.sleep(2)
        self.login.input_password(data["password"])#参数化密码
        time.sleep(2)
        self.login.submit()#点击登录
        time.sleep(2)
        result_loc = ("class name", "f4_b")#制作定位器
        result = self.login.check_text_in_element(result_loc, data["username"])#核对元素显示文本和账号名知否一直
        now = time.strftime("%Y_%m_%d %H_%M_%S")#时间格式化
        file_path = f"../image/{now}.jpg"#错误截图存放路径



        try:
            self.assertEqual(result, data["expect"])  # 断言登录是否成功
        except AssertionError:
            self.login.screenshot(file_path)
            raise AssertionError

if __name__ == '__main__':
    unittest.main()

