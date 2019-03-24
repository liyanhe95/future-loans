#-*-coding:utf-8-*-
# @time      :2019/1/2014:46
# @Author   :lemon_hehe
# @Email     :976621712@qq.com
# @File      :test_login.py
# @software:PyCharm Community Edition
#https://www.cnblogs.com/kuzhon/articles/5627977.html
import unittest
import allure
import pytest
from selenium import webdriver
from ddt import ddt,data
from pages.login import LoginPage
from data import login_message
from pages.index import IndexPage
from pages.bid import BidPage
from data import bid_message
import string
#web  UI 自动化测试效率不高（而接口自动化测试效率很高），因为每次开关浏览器的时间太长了
#提供自动化测试的效率，每次只需要开关一次浏览器就OK了
#投资的前提条件：登录、有余额、有标、标有余额
#1.手动
#2.自动化的UI操作
#3.利用接口

#如果使用pytest环境管理不要使用unittest，尤其是不可以和ddt一起使用


# @ddt
class TestBid():
    """这是投资类"""

    # def setUp(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.get("http://120.78.128.25:8765/Index/login.html")
    #     self.driver.maximize_window()
    #     self.login_page = LoginPage(self.driver)
    #     self.login_page.submit_userinfo(login_message.user_corrent['phone'], login_message.user_corrent['password'])
    #     self.index_page = IndexPage(self.driver)
    #     self.bid_page = BidPage(self.driver)

    @pytest.mark.usefixtures('init_driver')
    @pytest.mark.smoke
    @pytest.mark.loans
    @pytest.mark.parametrize('data',bid_message.bid_corrent)  #参数化
    # @data(*bid_message.bid_corrent)
    def test_login_loans(self,data,init_driver):
        #点击投标
        driver, index_page, bid_page = init_driver
        index_page.bid()
        #投资页面输入投标金额
        bid_page.bid(data['money'])
        bid_page.click_bid_submit()
        assert (bid_page.popup_text() == data['expected'])
        print(data['expected'])
        #比对金额（判断余额是否正确）投资前获取用户余额一次，减去投资金额，与现在的投资金额相等的话就通过测试用例
        #查找余额 用一个变量记录下来   可用余额（data-amount）-要投资的金额，在进行判断可用提高测试效率
        #投资项目那里是不是出现了新的信息（判断标的信息）

        #比对投资前后的金额
        front_amount = bid_page.data_amount()
        new_front_amount = float(front_amount)   #投资前的
        print('投资前的金额{}'.format(new_front_amount))
        bid_amount = data['money']    #投资金额
        bid_amount = int(bid_amount)
        print('投资金额{}'.format(bid_amount))
        count_amount = new_front_amount - bid_amount   #投资后的
        print('投资后的金额{}'.format(count_amount))
        driver.refresh()
        alter_amount = bid_page.data_amount()
        amount = float(alter_amount)
        print(type(amount))
        assert (count_amount == amount)

        #判断标的信息
        bid_page.click_user()
        index_page.bid_project()
        print(bid_page.title().text)
        assert ('test' in bid_page.title().text)






    #
    # def tearDown(self):
    #     self.driver.quit()






if __name__ == '__main__':
    unittest.main()