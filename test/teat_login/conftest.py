#-*-coding:utf-8-*-
# @time      :2019/1/2014:46
# @Author   :lemon_hehe
# @Email     :976621712@qq.com
# @File      :test_login.py
# @software:PyCharm Community Edition
import pytest
from selenium import webdriver
from pages.login import LoginPage
from data import login_message
from pages.index import IndexPage
from pages.bid import BidPage
@pytest.fixture
def init_driver():
    print('begin driver')
    driver = webdriver.Chrome()
    driver.get("http://120.78.128.25:8765/Index/login.html")
    driver.maximize_window()
    login_page = LoginPage(driver)

    yield  (driver,login_page)#在执行yield地时候会执行测试用例，执行完测试用例在执行quit driver（生成器）

    print('quit driver')
    driver.quit()


#return可以终止一个函数，而yield可以接着执行
@pytest.fixture('class')
def my_set_class():
    print('begin my class')
    driver = webdriver.Chrome()
    driver.get("http://120.78.128.25:8765/Index/login.html")
    driver.maximize_window()
    login_page = LoginPage(driver)

    yield (driver,login_page)

    print('finish my class')
    driver.quit()