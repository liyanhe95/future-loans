#-*-coding:utf-8-*-
# @time      :2019/1/2014:46
# @Author   :lemon_hehe
# @Email     :976621712@qq.com
# @File      :test_login.py
# @software:PyCharm Community Edition
class Loginpage:
#共享变量，共享函数封装，page封装成一个对象，就是一种编程的抽象（po模式）
#把页面封装成对象，对象可以共享属性，供对象里面的方法进行使用，可以共享变量，可以分类整理函数
    def __init__(self,driver):
        self.driver = driver

    def submit_userinfo(self,phone,password):
        phone_ele = self.driver.find_element_by_name("phone")
        pwd_ele = self.driver.find_element_by_name("password")

        # 点击登录（提交）
        phone_ele.send_keys(phone)
        pwd_ele.send_keys(password)

        phone_ele.submit()

    def click(self):
        pass

