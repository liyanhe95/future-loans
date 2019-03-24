#-*-coding:utf-8-*-
# @time      :2019/1/2014:46
# @Author   :lemon_hehe
# @Email     :976621712@qq.com
# @File      :test_login.py
# @software:PyCharm Community Edition

import logging
#自己写的日志类
class MyLog:
    def my_log(self,msg,level):
#写一个属于自己的日志系统
#收集器   ---创建一个日志收集器  #getlogger函数
        my_logger=logging.getLogger('math_log')#创建一个日志收集器
        my_logger.setLevel('DEBUG')  #给这个日志收集器setLevel()  设置级别

        #格式   ：规定日志输出的格式
        formatter=logging.Formatter('%(asctime)s-[%(levelname)s]-[%(filename)s]-[%(name)s]-[日志信息]：%(message)s')

        ch=logging.StreamHandler()#  创建一个输出到控制台的渠道
        ch.setLevel('DEBUG')  #给渠道设置级别   如果不设置级别就默认调用console这个渠道
        ch.setFormatter(formatter)
        # 如果两个级别不一致    那么两个一综合就取交集

        # 输出到指定的文件   文件路径：绝对路径    相对路径
        fh=logging.FileHandler('math.log',encoding='utf-8')
        fh.setLevel('DEBUG')#设置渠道级别
        fh.setFormatter(formatter)
# 对接   日志收集器与输出渠道进行对接
        my_logger.addHandler(ch)
        my_logger.addHandler(fh)
        if level=='DEBUG':
            my_logger.debug(msg)
        elif level=='IFNO':
            my_logger.info(msg)
        elif level=='WARNING':
            my_logger.warning(msg)
        elif level=='ERROR':
            my_logger.error(msg)
        elif level=='CRITICAL':
            my_logger.critical(msg)
#去掉日志的重复  每次收集完毕之后  记得移除掉收集器
        my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)
    def debug(self,msg):
        self.my_log(msg,'DEBUG')
    def info(self,msg):
        self.my_log(msg,'INFO')
    def warning(self,msg):
        self.my_log(msg,'WARNING')
    def error(self,msg):
        self.my_log(msg,'ERROR')
    def critical(self,msg):
        self.my_log(msg,'CRITICAL')

# #输出渠道   --指定输出
if __name__ == '__main__':
    my_logger=MyLog()   #实例化对象
    my_logger.debug('我是debug')