#-*-coding:utf-8-*-
# @time      :2019/1/2014:46
# @Author   :lemon_hehe
# @Email     :976621712@qq.com
# @File      :test_login.py
# @software:PyCharm Community Edition

import pytest

# if __name__ == '__main__':
# #     pytest.main(['-m smoke','--result-log=report/test.log',
# #                  '--junit-xml=report/test.xml',
# #                  '--html=report/test.html'])  #指定存放到那个目录下
# #   #--capture=no  不要捕获异常，让控制台看起来更详细

if __name__ == '__main__':
    pytest.main(['-m smoke','--capture=no','--alluredir=allure'])

