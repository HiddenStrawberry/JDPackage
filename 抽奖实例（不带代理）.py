#encoding=utf-8
from JDPackage import *

#DOCS:https://github.com/HiddenStrawberry/JDPackage/blob/master/docs/lotterypack.md

login('1','15840000000','123456')
login('1','15840000001','123456')
login('2','15840000002','123456')
#登陆京东账号，设定userid为1，并将cookies存入cookies文件(注意：登录只需要一次，除非cookies失效)

add_lottery('1', '4b6c385f-a626-48d2-8abe-f2ce2ebe5d5f', '2017-03-08 20:57:30', 5, cookielist, proxylist=[])  
add_lottery('2', '4b6c385f-a626-48d2-8abe-f2ce2ebe5d5f', '2017-03-08 20:57:30', 5, cookielist, proxylist=[]) 
