#-*-coding:utf-8-*-
# @time      :2019/1/2014:46
# @Author   :lemon_hehe
# @Email     :976621712@qq.com
# @File      :test_login.py
# @software:PyCharm Community Edition
#模块本身也是一个对象
#正确的用户信息
user_corrent = [{"phone":"18684720553","password":"python","expected":"我的帐户[小蜜蜂96027921]"}]
    # {"phone":18684720553,"password":"python","expected":"我的帐户[小蜜蜂96027921]"}


#错误的用户信息
user_incorrent = [
    {"phone":"","password":"","expected":"请输入手机号"},
    {"phone":"5617291","password":"","expected":"请输入正确的手机号"},
    {"phone":"13670287382","password":"","expected":"请输入密码"},
    {"phone":"1868472055","password":"","expected":"请输入正确的手机号"},
    {"phone":"186847205534","password":"","expected":"请输入正确的手机号"},
    {"phone":"18684720l55","password":"","expected":"请输入正确的手机号"},
]


#密码错误的情况下  //div[@class="layui-layer-content"]
user_wrong = [
    {"phone":"18684720553","password":"123456","expected":"帐号或密码错误!"}
    ]

# 未授权  //div[@class="layui-layer-content"]
user_unauthorized = [
    {"phone":"18877314371","password":"123456li","expected":"此账号没有经过授权，请联系管理员!"}
    ]

