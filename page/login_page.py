
"""
登录页面
编写人:廖松林
"""

"""
1.login_page.py 需要继承Base类
2.封装表现层
3.封装操作层
"""
from common.base import Base
from common.base import open_browser

url = "http://ecshop.itsoso.cn/user.php"

class LoginPage(Base):#继承Base类
    """封装表现层--制作定位器"""
    username_loc = ("name", "username")  # 用户名输入框
    password_loc = ("name", "password")  # 密码输入框
    remember_loc = ("id", "remember")  # 记住密码
    submit_loc = ("name", "submit")  # 立即登录按钮
    qpassword_loc = ("link text", "密码问题")  # 找回密码--密码问题
    email_loc = ("link text", "邮件")  # 找回密码--邮箱
    sms_loc = ("link text", "短信验证")  # 找回密码--短信验证
    register_loc = ("css selector", "body>div.usBox.clearfix>div.usTxt>a")  # 立即注册按钮
    homepage_loc = ("link text", "首页")  # 返回首页链接

    """封装操作层"""
    def input_username(self,text):
        """输入用户名"""
        self.send_keys(self.username_loc,text)#输入用户名
    def input_password(self,text):
        """输入密码"""
        self.send_keys(self.password_loc,text)
    def remmenber_password(self):
        """记住密码"""
        self.click_element(self.remember_loc)
    def submit(self):
        """立即登录"""
        self.click_element(self.submit_loc)
    def find_password_question(self):
        """找回密码-问题"""
        self.click_element(self.qpassword_loc)

    def find_password_email(self):
        """找回密码-邮箱"""
        self.click_element(self.email_loc)
    def find_password_sms(self):
        """找回密码-短信"""
        self.click_element(self.sms_loc)
    def register(self):
        """立即注册"""
        self.click_element(self.register_loc)
    def homepage(self):
        """返回首页"""
        self.click_element(self.homepage_loc)
if __name__ == '__main__':
    driver=open_browser()

    driver.get(url)
    longinpage=LoginPage(driver)
    longinpage.input_username("叶良辰") #输入账号密码
    longinpage.input_password("zhl3841279")    #输入密码
    longinpage.submit() #点击登录
    # driver.quit() #退出
    #longinpage.homepage()#返回首页
    #longinpage.register()#立即注册
    #longinpage.find_password_email()#验证找回密码-邮箱
    #longinpage.find_password_question()#验证找回密-问题
    #longinpage.find_password_sms() #验证找回密码-短信验证



