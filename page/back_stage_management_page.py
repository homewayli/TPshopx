
"""
后台管理--添加新商品页面
编写人:黎洪伟

"""


import time
from common.base import Base
from common.base import open_browser

url = "http://ecshop.itsoso.cn/admin/privilege.php?act=login"

class BackStageManagement(Base):  # 继承Base类
    """封装表现层--制作定位器"""
    # 账号框
    username_loc = ("xpath","//*[@id='loginPanel']/div[1]/input")
    # 密码框
    password_loc = ("xpath","//*[@id='loginPanel']/div[2]/input")
    # 登录框
    login_loc =("xpath","//*[@id='loginPanel']/div[3]/input")
    #商品管理按钮
    goods_management_loc = ("xpath","//*[@id='menu-ul']/li[2]")
    # 添加新商品按钮
    add_new_goods_loc = ("css selector","#sub-menu-02_goods_add>a")
    # 通用信息--商品名称
    goods_name_loc = ("xpath","//*[@id='general-table']/tbody/tr[1]/td[2]/input[1]")
    # 通用信息--商品分类下拉框
    goods_classify_loc = ("xpath","//*[@id='general-table']/tbody/tr[3]/td[2]/select")
    # 通用信息--扩展分类--添加
    classify_add_loc = ("xpath","//*[@id='general-table']/tbody/tr[4]/td[2]/input")
    # 通用信息--扩展分类--添加下拉框
    classify_add_choose_loc =("xpath","//*[@id='general-table']/tbody/tr[4]/td[2]/select")
    # 通用信息--商品品牌
    goods_brand_loc = ("xpath","//*[@id='general-table']/tbody/tr[5]/td[2]/select")
    # 通用信息--选择供应商
    supplier_loc = ("id","suppliers_id")
    # 通用信息--本店售价
    sales_loc = ("xpath","//*[@id='general-table']/tbody/tr[7]/td[2]/input[1]")
    # 详细描述按钮
    goods_details_loc = ("id","detail-tab")
    # 详细描述---输入文本框
    details_input_text_loc =("css selector","body[spellcheck='false']")
    # 其他信息按钮
    goods_others_loc = ("id","mix-tab")
    # 其他信息---商品重量输入框
    goods_weight_loc = ("xpath","//*[@id='mix-table']/tbody/tr[1]/td[2]/input")
    # 其他信息--商品重量单位框
    weight_unit_loc = ("xpath","//*[@id='mix-table']/tbody/tr[1]/td[2]/select")
    # 其他信息---库存数量输入框
    stock_num_loc = ("xpath","//*[@id='mix-table']/tbody/tr[2]/td[2]/input")
    # 其他信息---库存警告数量框
    stock_warn_loc = ("xpath","//*[@id='mix-table']/tbody/tr[3]/td[2]/input")
    # 其他信息---加入推荐--精品单选框
    is_best_goods_loc = ("xpath","//*[@id='mix-table']/tbody/tr[4]/td[2]/input[1]")
    # 其他信息---加入推荐--新品单选框
    is_new_goods_loc = ("xpath","//*[@id='mix-table']/tbody/tr[4]/td[2]/input[2]")
    # 其他信息---加入推荐--热销单选框
    is_hot_loc = ("xpath","//*[@id='mix-table']/tbody/tr[4]/td[2]/input[3]")
    # 其他信息---上架单选框
    is_on_sale_loc = ("xpath","//*[@id='alone_sale_3']/input")
    # 其他信息---能作为普通商品销售框
    is_alone_sale_loc = ("xpath","//*[@id='mix-table']/tbody/tr[7]/td[2]/input")
    # 其他信息---是否为免运费商品框
    is_shipping_loc = ("xpath","//*[@id='mix-table']/tbody/tr[7]/td[2]/input")
    # 其他信息---商品关键词输入框
    goods_key_words_loc = ("xpath","//*[@id='mix-table']/tbody/tr[8]/td[2]/input")
    # 其他信息---商品简单描述输入框
    goods_simple_descr_loc = ("xpath"," //*[@id='mix-table']/tbody/tr[9]/td[2]/textarea")
    # 商品属性按钮
    goods_property_loc = ("id","properties-tab")
    # 商品属性----商品类型下拉框
    goods_property_choose_loc = ("xpath","//*[@id='properties-table']/tbody/tr[1]/td[2]/select")
    # 商品相册按钮
    goods_gallery_loc = ("id","gallery-tab")
    # 商品相册---图片描述输入框
    gallery_descrip_loc = ("xpath","//*[@id='gallery-table']/tbody/tr[3]/td/input[1]")
    # 商品相册---选择文件框
    choose_gallery_file_loc = ("xpath","//*[@id='gallery-table']/tbody/tr[3]/td/input[2]")
    # 商品相册---外部图片输入框
    outer_http_loc = ("xpath","//*[@id='gallery-table']/tbody/tr[3]/td/input[3]")
    # 商品相册---确认按钮
    goods_confirm_loc = ("xpath","//*[@id='tabbody-div']/form/div/input[2]")
    # 详细描述第二次iframe定位器
    iframe_loc = ("css selector","#xEditingArea>iframe")
    """封装操作层"""
    def login_success(self,text1,text2):
        self.input_username(text1)
        self.input_password(text2)
        self.click_login()

    def input_username(self,text):
        """账号输入框输入账号"""
        self.send_keys(self.username_loc,text)

    def input_password(self,text):
        """密码输入框输入密码"""
        self.send_keys(self.password_loc,text)

    def click_login(self):
        """点击登录界面的登录按钮"""
        self.click_element(self.login_loc)

    def click_goods_management(self):
        """点击商品管理"""
        self.to_frame("menu-frame")
        self.click_element(self.goods_management_loc)

    def click_add_new_goods(self):
        """点击添加新商品"""

        self.click_element(self.add_new_goods_loc)

    def input_goods_name(self,text):
        """商品名称输入框输入名称"""
        self.exit_to_default_frame()
        self.to_frame("main-frame")
        self.send_keys(self.goods_name_loc,text)

    def click_goods_classify(self):
        """点击商品的分类"""
        self.click_element(self.goods_classify_loc)

    def choose_goods_classfiy(self,index):
        """选择商品分类下拉框"""
        self.selector_by_index(self.goods_classify_loc,index)

    def click_classify_add(self):
        """点击扩展分类中的添加"""
        self.click_element(self.classify_add_loc)

    def choose_classify_add_choose(self,index):
        """选择扩展分类的下拉框"""
        self.selector_by_index(self.classify_add_choose_loc,index)

    def choose_goods_brand(self,index):
        """选择商品品牌下拉框"""
        self.selector_by_index(self.goods_brand_loc,index)

    def choose_supplier(self,index):
        """选择供货商下拉框"""
        self.selector_by_index(self.supplier_loc,index)

    def input_sales(self,text):
        """商品售价输入框输入数据"""
        self.send_keys(self.sales_loc,text)

    def click_goods_details(self):
        """点击详细描述按钮"""
        self.click_element(self.goods_details_loc)



    def input_details_text(self,text):
        """详细描述输入框输入文本"""
        self.to_frame("goods_desc___Frame")
        self.to_frame_1(self.iframe_loc)
        self.send_keys(self.details_input_text_loc,text)

    def click_goods_others(self):
        """点击其他信息按钮"""
        self.exit_to_default_frame()
        self.to_frame("main-frame")
        self.click_element(self.goods_others_loc)

    def input_goods_weight(self,text):
        """商品重量输入框输入"""
        self.send_keys(self.goods_weight_loc,text)

    def choose_weight_unit(self,index=1):
        """商品重量单位下拉框"""
        self.selector_by_index(self.weight_unit_loc,index)

    def input_stock_num(self,text):
        """商品库存数量输入框的输入"""
        self.send_keys(self.stock_num_loc,text)

    def input_stock_warn(self,text=1):
        """库存警告数量输入框的输入"""
        self.send_keys(self.stock_warn_loc,text)

    def click_is_best_goods(self):
        """点击加入推荐中的精品"""
        self.click_element(self.is_best_goods_loc)

    def click_is_new_goods(self):
        """点击加入推荐中的新品"""
        self.click_element(self.is_new_goods_loc)

    def click_is_hot(self):
        """"点击加入推荐中的热销"""
        self.click_element(self.is_hot_loc)

    def click_is_on_sale(self):
        """"点击是否作为普通商品销售单选框"""
        self.click_element(self.is_on_sale_loc)

    def  click_is_alone_sale(self):
        """点击是否为免运费商品单选框"""
        self.click_element(self.is_alone_sale_loc)

    def input_goods_key_words(self,text):
        """商品关键词的输入"""
        self.send_keys(self.goods_key_words_loc,text)

    def input_goods_simple_descr(self,text):
        """商品简单描述的输入"""
        self.send_keys(self.goods_simple_descr_loc,text)

    def click_goods_property(self):
        """点击商品属性按钮"""
        self.click_element(self.goods_property_loc)

    def choose_goods_property(self,index):
        """选择商品类型"""
        self.selector_by_index(self.goods_property_choose_loc,index)

    def click_goods_gallery(self):
        """点击商品相册按钮"""
        self.click_element(self.goods_gallery_loc)

    def input_gallery_descrip(self,text):
        """图片描述的文本输入"""
        self.send_keys(self.gallery_descrip_loc,text)
    def click_choose_file(self):
        """点击选择文件"""
        self.click_element(self.choose_gallery_file_loc)

    def update_gallery_file(self,filename):
        """上传图片文件"""
        file = self.find_element(self.choose_gallery_file_loc)
        self.send_keys(self.choose_gallery_file_loc,filename)
        file.send_keys(filename)
    def input_outer_http(self,text):
        """输入外部图片链接"""
        self.send_keys(self.outer_http_loc,text)


    def click_goods_confirm(self):
        """"点击商品相册中的确定按钮"""
        self.click_element(self.goods_confirm_loc)


if __name__ == '__main__':
    driver = open_browser()
    back_stage = BackStageManagement(driver)
    back_stage.open_url(url)
    username = "admin"
    time.sleep(2)
    password = "admin123"
    back_stage.input_username(username)
    back_stage.input_password(password)
    back_stage.click_login()
    time.sleep(1)
    back_stage.click_goods_management()
    time.sleep(1)
    back_stage.click_add_new_goods()
    time.sleep(1)
    back_stage.input_goods_name("iphoneX88989")
    time.sleep(1)

    back_stage.choose_goods_classfiy(2)
    time.sleep(1)
    back_stage.click_classify_add()
    time.sleep(1)
    back_stage.choose_classify_add_choose(4)
    time.sleep(1)
    back_stage.choose_goods_brand(1)
    time.sleep(1)
    back_stage.choose_supplier(1)
    time.sleep(1)
    back_stage.input_sales("29999")
    time.sleep(1)
    back_stage.click_goods_details()
    time.sleep(3)
    back_stage.input_details_text("唱歌,跳舞,打篮球,会rap的caixukun")
    time.sleep(3)
    back_stage.click_goods_others()
    time.sleep(1)
    back_stage.input_goods_weight(50)
    time.sleep(2)
    back_stage.choose_weight_unit(1)
    time.sleep(2)
    back_stage.input_stock_num(101)
    time.sleep(2)
    back_stage.input_stock_warn(2)
    time.sleep(2)
    back_stage.click_is_best_goods()
    time.sleep(2)
    back_stage.click_is_new_goods()
    time.sleep(2)
    back_stage.click_is_hot()
    time.sleep(2)
    back_stage.click_is_on_sale()
    time.sleep(2)
    back_stage.click_is_alone_sale()
    time.sleep(2)
    back_stage.input_goods_key_words("AI")
    time.sleep(2)
    back_stage.input_goods_simple_descr("智能机器人可以帮助人类完成很多事情")
    time.sleep(2)
    back_stage.click_goods_property()
    time.sleep(2)
    back_stage.choose_goods_property(5)
    time.sleep(2)
    back_stage.click_goods_gallery()
    # back_stage.input_gallery_descrip("周杰伦是最帅得")
    time.sleep(2)
    back_stage.update_gallery_file(r"D:\test\ECshop\image\周杰伦昆凌.jpg")
    time.sleep(2)
    # back_stage.click_goods_confirm()
    time.sleep(2)
    back_stage.close()















