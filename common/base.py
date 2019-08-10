"""
base_1.py
    1.对浏览器进行封装
    2.对selenium方法进行二次封装
"""
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time
def open_browser(browser='Chrome'):
    driver = None
    if browser == 'Chrome':
        driver = webdriver.Chrome()

    elif browser == 'Firefox':
        driver = webdriver.Firefox()
    elif browser == 'Ie':
        driver = webdriver.Ie()
    else:
        print('请选择正确的浏览器→→Chrome→Firefox→Ie')
    driver.maximize_window()
    return driver



class Base:
    def __init__(self, driver):
        self.driver = driver



    def open_url(self, url):
        """打开网址"""
        self.driver.get(url)


    def back(self):
        """后退"""
        self.driver.back()

    def refresh(self):
        """刷新"""
        self.driver.refresh()

    def farword(self):
        """前进"""
        self.driver.farword()

    def implicitly_wait(self, timeout=10):
        """隐式等待"""
        self.driver.implicitly_wait(timeout)

    def get_attribute(self,locator,attribute):
        """打印元素的信息"""
        return self.find_element(locator).get_attribute(attribute)


    def get_tag_text(self,locator):
        try:
            text=self.find_element(locator).text
            return text
        except:
            print("标签无text值")

    def get_element_value(self,locator,text,timeout=10):
        """判断一个元素的value值与输入的text是否相等"""
        try:
            result = WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element_value(locator,text))
        except:
            print(f"{locator}元素未找到")
            return False
        else:
            return result

    def find_element(self, locator, timeout=10):
        """
        定位一个元素,如果定位到元素则返回元素,否则返回False
        :param locator: 元祖(by.XXX,value)("id","id属性值")
        :param timeout: 秒数
        :return:
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            return element
        except:
            print(f'元素未找到→{locator}')

    def find_elements(self, locator, timeout=10):
        """
        定位一组元素,如果定位到元素则返回元素(list),否则返回False
        :param locator: 元祖(by.XXX,value)
        :param timeout: 秒数
        :return:
        """
        try:
            elements = WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
            return elements
        except:
            print(f'元素未找到→{locator}')

    def selector_by_index(self,locator,index):
        """下拉框通过索引选择元素"""
        selector=Select(self.find_element(locator))
        try:
            selector.select_by_index(index)
        except:
            print("下拉框元素未找到")

    def selector_by_value(self,locator,value):
        """下拉框通过value选择元素"""
        selector=Select(self.find_element(locator))
        try:
            selector.select_by_value(value)
        except:
            print("下拉框元素未找到")

    def scroll(self,to):
        """下拉条滚动"""
        try:
            js=f'window.scrollTo(0,{to})'
            self.driver.execute_script(js)
        except:
            print("下拉滚动条失败")

    def click_element(self, locator, timeout=10):
        """单个元素点击操作"""
        element = self.find_element(locator, timeout)
        try:
            element.click()
        except:
            pass

    def click_one_checkbox(self, locator, timeout=10):
        """点击单个checkbox"""
        try:
            ele = self.find_element(locator, timeout)
            res = ele.is_selected()
            if res:
                pass
            else:
                ele.click()
        except Exception as e:
            return e

    def to_frame(self, id_or_name):
        """通过id和name属性进入frame"""
        try:
            self.driver.switch_to.frame(id_or_name)
        except:
            print(f'元素未找到 -> {id_or_name}')
    def to_frame_1(self,locator):
        """通过定位器进入frame"""
        try:
            element = self.find_element(locator)
            self.driver.switch_to.frame(element)
        except:
            print(f'元素未找到 -> {locator}')

    def exit_to_seed_frame(self):
        """返回上级frame"""
        self.driver.switch_to.parent_frame()

    def exit_to_default_frame(self):
        """返回最外层frame"""
        self.driver.switch_to.default_content()

    def click_elements(self, locator, timeout=10):
        """分别点击一组元素操作"""
        elements = self.find_elements(locator, timeout)
        # elements = [i for i in elements]
        for x in elements:
            x.click()
            time.sleep(2)
            self.back()
            self.refresh()
            time.sleep(2)

    def send_keys(self,locator,text,timeout=10):
        element=self.find_element(locator,timeout)
        try:
            element.clear()
            element.send_keys(text)
        except:
            pass

    def check_text_in_element(self, locator, text, timeout=10):
        """
        判断文本是否在元素中,如果存在,返回True,如果不存在,返回False
        :param locator: 定位器
        :param text:    将要判断的文本--已知文本
        :param timeout:
        :return:
        """
        try:
            result = WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator,text))
        except:
            print(f"{locator}元素未找到")
            return False
        else:
            return result

    def check_value_in_element(self, locator, value, timeout=10):
        """
        判断value值是否存在元素中,如果存在,返回True,如果不存在,返回False
        :param locator: 定位器
        :param value:   将要判断的元素的value的值
        :param timeout:
        :return:
        """
        element = self.find_element(locator)
        try:
            value_1 = element.get_atrribute_value('value')
            if value_1 == value:
                return True
            else:
                return False
        except:
            return False

    def operation_alert(self, timeout=10):
        """处理弹窗"""
        alert = WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
        if alert:
            print(alert.text)
            alert.accept()
        else:
            return False

    def close(self):
        """关闭浏览器"""
        self.driver.quit()

    def screenshot(self,file_path):
        """截屏"""
        self.driver.get_screenshot_as_file(file_path)





