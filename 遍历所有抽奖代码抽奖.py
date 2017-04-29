# encoding=utf8
from JDPackage import *
import datetime
print datetime.datetime.now()


# lottery_login('#','#','#','#',1) #登录
time = datetime.datetime.strptime('2017-03-08 20:57:30', '%Y-%m-%d %H:%M:%S') #设置初始时间
dc = dict(eval(open('code.txt', 'rb').read()))  #读取代码字典
for k, value in dc.items():
    time = time + datetime.timedelta(seconds=5) #设置间隔时间秒数
    add_lottery(1, k, str(time), 5) #增加抽奖线程