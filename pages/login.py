#-*-coding:utf-8-*-
# @time      :2019/1/2014:46
# @Author   :lemon_hehe
# @Email     :976621712@qq.com
# @File      :test_login.py
# @software:PyCharm Community Edition
from selenium.webdriver.common.by import By
from pages.base import BasePage

class LoginPage(BasePage):
#共享变量，共享函数封装，page封装成一个对象，就是一种编程的抽象（po模式）
#把页面封装成对象，对象可以共享属性，供对象里面的方法进行使用，可以共享变量，可以分类整理函数
    #用户的phone元素定位器
    phone_input_locator = (By.NAME,"phone")
    #密码定位器
    pwd_input_locator = (By.NAME,"password")
    #未授权的信息
    unauthorized_locator = (By.XPATH,'//div[@class="layui-layer-content"]')
    #账号或密码错误
    wrong_locator = (By.XPATH,'//div[@class="layui-layer-content"]')

    #继承了父类，因为父类已经初始化了

    def submit_userinfo(self,phone,password):
        phone_ele = self.get_visible_element(self.phone_input_locator)
        pwd_ele = self.get_visible_element(self.pwd_input_locator)

        phone_ele.send_keys(phone)
        pwd_ele.send_keys(password)

        phone_ele.submit()
        # 上面等着等着，可能会导致下面的元素不见了，注意等着等着元素可能不见了，使用不倒万不得已，不要使用强制等待

    def send_keys(self):
        return self.get_phone_element().send_keys()

    def click_phone(self):
        return self.get_phone_element().click()

    def alert_info(self):
        return self.driver.find_element_by_xpath('//div[@class="form-error-info"]')

    def unauthorized_info(self):
        return self.get_visible_element(self.unauthorized_locator)

    def wrong_info(self):
        return self.get_visible_element(self.wrong_locator)

    def clear_phone(self):  #简化函数的调用
        return self.get_phone_element().clear()

    def clear_pwd(self):
        return self.get_pwd_element().clear()

    #接受定义的复杂，不能接受调用的复杂
    def get_phone_element(self):  #函数的定义
        return self.get_visible_element(self.phone_input_locator)

    def get_pwd_element(self):
        return self.get_visible_element(self.pwd_input_locator)






