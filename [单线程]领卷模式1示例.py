#encoding=utf-8
from JDPackage import *

#DOCS:https://github.com/HiddenStrawberry/JDPackage/blob/master/docs/cookies.md
#DOCS:https://github.com/HiddenStrawberry/JDPackage/blob/master/docs/coupon.md



a = Coupon('#', '#', '#', '#')
#          京东账号     京东密码    若快账号     若快密码
a.login()

a.new_coupon(
	'https://coupon.jd.com/ilink/couponActiveFront/front_index.action?key=61ea1f3fa9804499948617652d256485&roleId=6063883&to=mall.jd.com/index-13001.html',
	'2017-03-08 20:57:30','2017-04-21 00:11:40')

 #支持输入手机或电脑端优惠券地址，
 #格式为（优惠券地址，开始领卷时间，结束领卷时间，

 #模式1的抢卷过程:从运行开始就不断尝试抢卷，打码，如此循环。适合京东耍猴不放卷时使用。如线程开的够多密度够大，也适合正常半黑号抢卷使用


 #建议提前30秒左右就开始运行！如果需要提前测试，输入任何一个早于现在的时间即可！时间格式不可以改变，必须和例子格式相同！）
 
