#-*-coding:utf-8-*-
# @time      :2019/1/2014:46
# @Author   :lemon_hehe
# @Email     :976621712@qq.com
# @File      :test_login.py
# @software:PyCharm Community Edition

import unittest
import pytest
from selenium import webdriver
from ddt import ddt, data
from pages.login import LoginPage
from data import login_message


# web  UI 自动化测试效率不高（而接口自动化测试效率很高），因为每次开关浏览器的时间太长了
# 提供自动化测试的效率，每次只需要开关一次浏览器就OK了

# @ddt
class TestLogin():

    def setUp(self):
        # self.driver = webdriver.Chrome()
        # self.driver.get("http://120.78.128.25:8765/Index/login.html")
        # self.driver.maximize_window()
        # self.login_page = LoginPage(self.driver)
        pass

    @pytest.mark.smoke
    @pytest.mark.wrong
    @pytest.mark.usefixtures('init_driver')
    @pytest.mark.parametrize('data',login_message.user_wrong)
    # @data(*login_message.user_wrong)
    def test_login_wrong(self, data,init_driver):
        driver, login_page = init_driver
        login_page.submit_userinfo(data['phone'], data['password'])
        assert (data['expected'] == login_page.wrong_info().text)
        print(login_page.wrong_info().text)

    def tearDown(self):
        # self.driver.quit()
        pass



if __name__ == '__main__':
    unittest.main()