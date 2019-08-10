
"""
注册页面

编写人:廖松林
"""

"""
封装logon.py 需要基础base类
封装表现层
封装操作层
"""

from common.base import Base
from common.base import open_browser
from selenium.webdriver.support.ui import Select
url='http://ecshop.itsoso.cn/user.php?act=register'
class Logonpage(Base):#继承Base类
    """封装表现层-制作定位器"""
    username_loc=("id","username")#账号输入框
    password_loc= ("id", "password1")#密码输入框
    email_loc=("id","email")#邮箱输入框
    conform_password_loc=("id","conform_password")#确认密码输入框
    tel_loc=("css selector",'input[name="extend_field5"][type="text"][size="25"][class="inputBg"]') #手机号码输入框

    question_loc=("css selector",'select[name="sel_question"]')#密码提示问题下拉菜单
    answer_loc=("css selector",'input[name="passwd_answer"][type="text"][size="25"]')#密码问题答案输入框
    logon_loc=("css selector",'input[name="Submit"][type="submit"]')#立即注册按钮
    radio_loc=("css selector","body > div.usBox > div > form > table > tbody > tr:nth-child(12) > td:nth-child(2) > label > input[type=checkbox]")
    now_name_loc=("css selector",'#ECS_MEMBERZONE > font > font')#注册成功后界面显示的当前账号名字
    """封装操作层"""
    def input_username(self,text):
        #输入账号
        self.send_keys(self.username_loc,text)
    def input_email(self,text):
        """输入邮箱"""
        self.send_keys(self.email_loc,text)
    def input_password(self, text):
        """输入密码"""
        self.send_keys(self.password_loc, text)
    def input_conform_password(self,text):
        """确认密码"""
        self.send_keys(self.conform_password_loc,text)
    def input_phone(self,int):
        """输入手机号"""
        self.send_keys(self.tel_loc,int)
    def tishimima(self,index):
        """选择提示问题"""
        self.selector_by_index(self.question_loc,index)
    def input_answer(self,text):
        """输入密码问题答案"""
        self.send_keys(self.answer_loc,text)
    def click_radio(self):
        """单选框"""
        self.click_one_checkbox(self.radio_loc)
    def click_logon(self):
        """点击立即注册"""
        self.click_element(self.logon_loc)
    def get_now_name(self):
        """获取登录成功后的登录用户名"""
        now_name=self.get_tag_text(self.now_name_loc)
        return now_name


    """封装操作层"""
if __name__ == '__main__':
    dirver=open_browser()
    dirver.get(url)
    longon=Logonpage(dirver)
    longon.input_username("叶良辰3")
    longon.input_email("1758293133@qq.com")
    longon.input_password("zhl3841279")
    longon.input_conform_password("zhl3841279")
    longon.input_phone("18380434331")
    longon.tishimima(3)
    longon.input_answer("啦啦操浏览")
    longon.click_radio()#选着单选框
    longon.click_logon()#点击立即登录











