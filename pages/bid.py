#-*-coding:utf-8-*-
# @time      :2019/1/2014:46
# @Author   :lemon_hehe
# @Email     :976621712@qq.com
# @File      :test_login.py
# @software:PyCharm Community Edition

import time
import logging
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait  # 显示等待
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from pages.base import BasePage
from pages.index import IndexPage

class BidPage(BasePage):

    bid_input_locator = (By.XPATH,'//input[contains(@class,"invest-unit-investinput")]')

    bid_submit_locator = (By.XPATH, '//button[contains(@class,"btn-special")]')

    #投标成功弹出框
    bid_popup_locator = (By.XPATH,'//div[@class="layui-layer-content"]//div[contains(@class,"capital_font1")]')

    #账户信息
    bid_user_locator = (By.XPATH,'//img[@class="mr-5"]//..')

    #获取页面标题
    bid_title_locator = (By.XPATH,'//div[@class="deal_tab_font1" and @ms-html="item.title"]')

    def bid(self,money):
        return self.bid_input.send_keys(money)

    def click_bid_submit(self):
        return self.bid_submit.click()

    def popup_text(self):
        return self.bid_popup.text

    def data_amount(self):
        return self.bid_input.get_attribute("data-amount")

    def click_user(self):
        return self.bid_user.click()

    def title(self):
        return self.bid_title

    @property
    def bid_input(self):
        return self.get_visible_element(self.bid_input_locator)

    @property
    def bid_submit(self):
        return self.get_visible_element(self.bid_submit_locator)

    @property
    def bid_popup(self):
        return self.get_visible_element(self.bid_popup_locator)

    @property
    def bid_user(self):
        return self.get_visible_element(self.bid_user_locator)

    @property
    def bid_title(self):
        return self.get_visible_element(self.bid_title_locator)

