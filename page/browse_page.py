
"""
浏览所有商品页面
编写人:钟华龙

"""


import time

from common.base import Base,open_browser
from page.login_page import LoginPage

url = ("http://ecshop.itsoso.cn/")
class HomePageBrowse(Base):
    """制作定位去器"""
    # 所有商品分类的定位器
    category_loc = ("css selector", "div.cat1>a")
    # 下一页的定位器
    next_page_loc = ("css selector","#pager>a.next")
    # 回到主页的定位器
    home_page_loc = ("css selector","#mainNav>div>ul>li:nth-child(1)>a")
    # 所有商品分类里面的商品定位器
    all_goods_loc = ("css selector", "div.goods-title>a")
    """操作商品分类"""

    def get_all_category_text(self):
        """获取所有商品分类"""
        # 1.所有商品分类的定位器
        elements = self.find_elements(self.category_loc)
        all_category_text = []  # 新建一个空列表用于存取所有的text值
        # 将所有的元素遍历出来
        for element in elements:
            # 获取单个元素的text值
            category_text = element.text
            # 将这些元素的text值存入列表中
            all_category_text.append(category_text)
        return all_category_text

    def write_category_locator(self):
        """重写商品分类定位器"""
        all_category_text_01_=[]
        # 调用函数获取所有商品分类的text值
        all_category_text = self.get_all_category_text()
        # 将所有的分类的text值遍历出来
        for text in all_category_text:
            category_loc = ("link text",text)         # 重做定位器
            all_category_text_01_.append(category_loc)    # 将新的定位器存入一个新的列表中
        return all_category_text_01_

    def click_all_categoty(self):
        """点击所有商品分类"""
        all_locactors = self.write_category_locator()
        for locator in all_locactors:
            self.click_element(locator)
            time.sleep(3)
            self.back()
            time.sleep(2)

    def get_all_goods_title(self):
        """获取所有商品title"""
        # 得到所有商品的元素
        elements = self.find_elements(self.all_goods_loc)
        goods_titles = []    #新建一个空列表:用于存放所有商品元素的title值
        # 将元素遍历出来
        for element in elements:
            # 得到所有商品元素的title值
            title = element.get_attribute("title")
            goods_titles.append(title)  # 将所有商品元素的title值存放在列表中
        return goods_titles

    def make_all_goods_loc(self):
        """重写所有商品定位器"""
        goods_titles = self.get_all_goods_title()
        all_goods_loc = []
        for title in goods_titles:
            # 通过css方式重做定位器
            goods_loc = ("css selector", f"a[title = '{title}']")
            all_goods_loc.append(goods_loc)
        return all_goods_loc

    def click_all_goods(self):
        """点击所有商品"""
        # 获取所有商品的定位器
        all_goods_loc = self.make_all_goods_loc()
        # 将所有商品的定位器遍历出来
        for goods_loc in all_goods_loc:
            self.click_element(goods_loc)  # 点击遍历出来的商品
            time.sleep(2)
            self.back()
            time.sleep(3)

    def back_to_page(self):
        """点击回到主页"""
        self.click_element(self.home_page_loc)

    def click_all_goods_01(self):
        """点击所有类里面的商品信息"""
        all_locactors = self.write_category_locator()
        for locator in all_locactors:
            # 点击所有商品分类
            self.click_element(locator)
            time.sleep(2)
            # 点击商品分类里面的单个商品
            self.click_all_goods()
            while True:
                if self.check_text_in_element(self.next_page_loc, "下一页"):  # 判断是否有下一页按钮
                    # 点击下一页按钮
                    self.click_element(self.next_page_loc)
                    # 再点击本页面的单个商品
                    self.click_all_goods()
                else:
                   break # 中止循环
            time.sleep(3)
            # 回到主页
            self.back_to_page()




if __name__ == '__main__':
    driver = open_browser()
    hpg = HomePageBrowse(driver)
    hpg.open_url(url)
    hpg.click_all_goods_01()
    hpg.close()




