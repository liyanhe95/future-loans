# #-*-coding:utf-8-*-
# # @time      :2019/1/2014:46
# # @Author   :lemon_hehe
# # @Email     :976621712@qq.com
# # @File      :test_login.py
# # @software:PyCharm Community Edition
#
# #  接口地址 http://120.79.176.157:8012/Index/login.html
# from selenium import webdriver
# import unittest
# import time
# from selenium.webdriver.support.wait import WebDriverWait  # 显示等待
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.get('http://120.79.176.157:8012/Index/login.html')
#
# #visibility_of_element_located  判断某个元素是否可见
# phone_ele = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='phone']")))
# pwd_ele =  WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='password']")))
#
# phone_ele.send_keys(18684720553)
# pwd_ele.send_keys('python')
#
# phone_ele.submit()
