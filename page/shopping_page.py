
"""
购物车页面
编写人:陆兴雷

"""

import time

from common.base import Base  #selenium的基础操作
from common.base import open_browser #选择浏览器

url = "http://ecshop.itsoso.cn/goods.php?id=84"

class Additive(Base):

    amend_loc=("css selector","input[id*=goods_number]",)#修改数量
    remove_loc=("link text","删除")
    add_loc = ("xpath", "//*[@id='ECS_FORMBUY']/ul/li[7]/table/tbody/tr/td[1]/a/img")  # 添加到购物车
    update_loc=("xpath","//*[@id='formCart']/table[2]/tbody/tr/td[2]/input[2]") #更新购物车
    empty_loc=("xpath","//*[@id='formCart']/table[2]/tbody/tr/td[2]/input[1]")  #清空购物车
    homepage_loc=("link text","首页")  #首页元素


    #封装操作层
    def add(self):    #点击
        """立即购买"""
        self.click_element(self.add_loc)

    def input_amend(self,text):
        """修改数量"""
        self.click_element(self.amend_loc)
        self.send_keys(self.amend_loc,text)

    def update(self):
        """更新购物车"""
        self.click_element(self.update_loc)

    def empty(self):
        """清空购物车"""
        self.click_element(self.empty_loc)

    def homepage(self):
        """回到首页"""
        self.click_element(self.homepage_loc)

    def remove(self):
        """删除"""
        self.click_element(self.remove_loc)




if __name__ == '__main__':
    driver=open_browser()  #打开浏览器
    driver.get(url)  #打开网址
    ada=Additive(driver)
    time.sleep(3)
    ada.add()
    time.sleep(3)
    unm=5
    ada.input_amend(unm)
    time.sleep(3)
    ada.update()
    time.sleep(3)
    ada.remove()
    ada.operation_alert()
    # tanchuang=driver.switch_to_alert()  #捕获弹窗
    # tanchuang.accept()  #弹窗确定
    #tanchuang.dismiss() #弹窗取消
    ada.homepage()
    time.sleep(3)
    #driver.quit()