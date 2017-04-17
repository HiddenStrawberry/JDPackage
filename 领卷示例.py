#encoding=utf-8
from JDPackage import *

#DOCS:https://github.com/HiddenStrawberry/JDPackage/blob/master/docs/cookies.md
#DOCS:https://github.com/HiddenStrawberry/JDPackage/blob/master/docs/coupon.md


t={}
t[0] = Coupon('1234', '1234', '1234', '1234')
#          京东账号     京东密码    若快账号     若快密码
t[0].login()
t[0].new_coupon(
	'https://coupon.jd.com/ilink/couponActiveFront/front_index.action?key=61ea1f3fa9804499948617652d256485&roleId=6063883&to=mall.jd.com/index-13001.html',
	'2017-03-08 20:57:30','2017-04-08 00:11:40')
 #支持输入手机或电脑端优惠券地址，
 #格式为（优惠券地址，开始领卷时间，结束领卷时间，
 #建议提前30秒左右就开始领卷！如果需要提前测试，输入任何一个早于现在的时间即可！时间格式不可以改变，必须和例子格式相同！）
 
