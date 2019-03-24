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

#很多类共享了某一种行为（继承）
#日志
logging.basicConfig(filename='loans.log')
logger = logging.getLogger()


class BasePage:
    #定义所有页面共享的类
    def __init__(self,driver:Chrome):
        #每个页面都需要浏览器，所以这个浏览器是共享的
        self.driver = driver

    #接受定义的复杂，不接受调用的复杂

    def get_visible_element(self,locator,eqc=20) -> WebElement:
        try:
            return WebDriverWait(self.driver,eqc).until(
                EC.visibility_of_element_located(locator)
            )
        #save_screenshot  保存截屏
        except Exception as e:
            logging.error('no this element:{}'.format(e))
            self.driver.save_screenshot("{}.jpg".format(time.time()))


    def switch_window(self,name=None,fqc=20):
        if name is None:
            current_handle = self.driver.current_window_handle
            WebDriverWait(self.driver,fqc).until(EC.new_window_is_opened(current_handle))
            handles = self.driver.window_handles
            return self.driver.switch_to.window(handles[-1])
        return self.driver.switch_to.window(name)