#-*-coding:utf-8-*-
# @time      :2019/1/2014:46
# @Author   :lemon_hehe
# @Email     :976621712@qq.com
# @File      :test_login.py
# @software:PyCharm Community Edition

import unittest
from selenium import webdriver
from ddt import ddt,data
from pages.login import LoginPage
from data import login_message
#web  UI 自动化测试效率不高（而接口自动化测试效率很高），因为每次开关浏览器的时间太长了
#提供自动化测试的效率，每次只需要开关一次浏览器就OK了

@ddt
class TestLogin(unittest.TestCase):

    @classmethod #类方法，实例方法，静态方法各自在怎么场景下使用
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://120.78.128.25:8765/Index/login.html")
        cls.driver.maximize_window()
        cls.login_page = LoginPage(cls.driver)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        pass


    @data(*login_message.user_incorrent)
    def test_login_failed(self,data):
        # 访问登录页面
        # 属于一个表单，最后会执行一个js的脚本
        self.login_page.submit_userinfo(data['phone'],data['password'])
        # 断言
        self.assertTrue(data['expected'] == self.login_page.alert_info().text)
        print(self.login_page.alert_info().text)

    @data(*login_message.user_unauthorized)
    def test_login_unauthorized(self,data):

        self.login_page.submit_userinfo(data['phone'], data['password'])
        self.assertTrue(data['expected'] == self.login_page.unauthorized_info().text)
        print(self.login_page.unauthorized_info().text)




    def tearDown(self):
        # self.driver.quit()
        # 输入完以后删除输入框
        self.login_page.clear_phone()
        self.login_page.clear_pwd()




if __name__ == '__main__':
    unittest.main()