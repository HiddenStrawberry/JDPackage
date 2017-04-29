#encoding=utf-8

from JDPackage import *

#DOCS:https://github.com/HiddenStrawberry/JDPackage/blob/master/docs/lotterypack.md

lottery_login('#','#','#','#',1)
lottery_login('#','#','#','#',1)
lottery_login('#','#','#','#',1)
lottery_login('#','#','#','#',2)
#登陆京东账号，设定userid为1(userid用来分组），并将cookies存入cookies文件(注意：每个帐号登录只需要一次，除非cookies失效)



get_iplist('ip.csv', 10,'inha') #此处参数参见文档,无特殊需求勿动
filter_iplist('ip.csv', 'new.csv', 2) #此处参数参见文档,无特殊需求勿动


add_lottery(1, '4b6c385f-a626-48d2-8abe-f2ce2ebe5d5f', '2017-03-08 20:57:30', 5, loadCSVfile('new.csv'))  
add_lottery(2, '4b6c385f-a626-48d2-8abe-f2ce2ebe5d5f', '2017-03-08 20:57:30', 5, loadCSVfile('new.csv')) 
#           userid, 抽奖码,                                      开始时间,              两账号抽奖延迟