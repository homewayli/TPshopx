
"""
 购物车模块---测试用例

 编写人:陆兴雷

"""

import time
import ddt
import unittest
from common.base import open_browser
from common.operationexcel import OperationExcel
from page.shopping_page import Additive,url



oper_excel=OperationExcel(r"D:\test\ECshop_第三组\data\testda.xls")  #文件路径
test_data=oper_excel.get_data_for_dict() #转为字典
# print(test_data)


@ddt.ddt
class TestCart(unittest.TestCase):
    def setUp(self) -> None:
        """打开浏览器,打开被测地址"""
        driver=open_browser()
        # self.cart=LoginPage(driver)
        self.add=Additive(driver)
        self.add.open_url(url)

    def tearDown(self) -> None:
        """关闭浏览器"""
        self.add.close()

        #用例编写
    @ddt.data(*test_data)
    def test_cart(self,data:dict):
        """购物车添加商品成功"""
        self.add.add()  #立即购买
        time.sleep(1)
        num_1 = str(data["number"]) #转化为str类型
        print(num_1)
        self.add.input_amend(num_1) #修改数量
        time.sleep(2)
        self.add.update() #更新购物车
        time.sleep(2)

       # self.add.homepage()#回首页
       #  time.sleep(3)
        #self.add.add() #立即购买
        # time.sleep(3)
        #self.add.empty() #清空购物车
        # self.add.remove()#删除
        # time.sleep(3)
        # self.add.operation_alert()
        #
        # time.sleep(3)
        number_loc=("css selector","input[id *='goods_number_']")#定位修改后的数

        time.sleep(1)
        result=self.add.get_element_value(number_loc,num_1)
        print(result)
        time.sleep(1)
        now = time.strftime("%Y_%m_%d %H_%M_%S")
        time.sleep(1)
        file_path=f"../image/{now}.jpg"
        time.sleep(1)





if __name__ == '__main__':
    unittest.main()
