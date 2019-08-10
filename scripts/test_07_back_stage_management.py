"""
后台管理系统---测试用例

编写人:黎洪伟
"""

import time
import unittest
from page.login_page import LoginPage
from page.back_stage_management_page import BackStageManagement,url
from common.base import open_browser

from common.constructdata import Constructdata

class TestBackStage(unittest.TestCase):
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
    def test_back_stage_01(self):
        """测试用例1:后台管理-添加新商品-添加一个新商品的测试"""
        # 1,实例化对象
        back_stage = BackStageManagement(self.driver)
        # 2.后台账号登录
        back_stage.login_success("admin","admin123")
        time.sleep(3)
        # 3.点击商品管理
        back_stage.click_goods_management()
        time.sleep(3)
        # 4.点击添加新商品
        back_stage.click_add_new_goods()
        time.sleep(3)
        # 5.在商品名称输入框中输入名称
        back_stage.input_goods_name(self.cons.random_goods_name())
        time.sleep(1)
        # 6.选择商品的分类
        back_stage.choose_goods_classfiy(4)
        time.sleep(1)
        # 7.点击扩展分类中的添加按钮
        back_stage.click_classify_add()
        time.sleep(1)
        # 选择扩展分类中的分离
        back_stage.choose_classify_add_choose(5)
        # 8.选择商品的品牌5
        back_stage.choose_goods_brand(4)
        time.sleep(1)
        # 9.选择供货商---北京供货商
        back_stage.choose_supplier(1)
        time.sleep(3)
        # 10.输入本店售价
        back_stage.input_sales(self.cons.random_sales())
        time.sleep(3)
        # 11.点击详细描述页面
        back_stage.click_goods_details()
        # 13.在详细描述输入框输入文字描述
        back_stage.input_details_text(self.cons.random_answer())
        time.sleep(3)
        # 14.点击其他信息
        back_stage.click_goods_others()
        time.sleep(3)
        # 15.在商品重量输入框输入商品重量
        back_stage.input_goods_weight(self.cons.random_weight())
        time.sleep(3)
        # 16.选择商品重量单位下拉框---克
        back_stage.choose_weight_unit(1)
        time.sleep(3)
        # 17.输入商品库存数量
        back_stage.input_stock_num(200)
        time.sleep(3)
        # 18.输入库存警告数量
        back_stage.input_stock_warn(2)
        time.sleep(3)
        # 19.点击新品
        back_stage.click_is_new_goods()
        time.sleep(3)
        # 20.输入商品关键字----homeway推荐
        back_stage.input_goods_key_words("周杰伦强力推荐")
        time.sleep(3)
        # 21.输入商品简单描述----随机生成
        back_stage.input_goods_simple_descr(self.cons.random_answer())
        time.sleep(3)
        # 22.点击商品属性
        back_stage.click_goods_property()
        time.sleep(3)
        # 23.选择商品类型---
        back_stage.choose_goods_property(4)
        time.sleep(3)
        # 24.点击商品相册
        back_stage.click_goods_gallery()
        time.sleep(5)
        # 25.图片描述输入文字
        back_stage.input_gallery_descrip("蔡徐坤")
        time.sleep(3)
        # 26.上传文件
        back_stage.update_gallery_file(r"D:\test\ECshop_第三组\image\周杰伦昆凌.jpg")
        time.sleep(2)
        # 27.点击确定按钮
        back_stage.click_goods_confirm()
        time.sleep(20)

if __name__ == '__main__':
    unittest.main()














