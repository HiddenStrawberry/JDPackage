# encoding=utf-8
from JDPackage import *

# DOCS:https://github.com/HiddenStrawberry/JDPackage/blob/master/docs/cookies.md
# DOCS:https://github.com/HiddenStrawberry/JDPackage/blob/master/docs/coupon.md



multi_couponA('#', '#', '#', '#', 1,0.1,  #京东账号,京东密码,若快账号,若快密码,线程数,延时
			  '2017-04-28 23:59:30', #开始时间
			  '2017-04-30 00:00:30', #结束时间
              'http://coupon.m.jd.com/coupons/show.action?key=88dfb7d340614fd690296ac8634d12e9&roleId=6244957&to=chongzhi.m.jd.com/&cu=true&utm_source=www.zuanke8.com&utm_medium=tuiguang&utm_campaign=t_1000000936_571233&utm_term=ef10cc211a3a4129851e1251b092cbb4&abt=3'
			  ) #    卷地址

#注意：账号自动一个一个登陆，请提前运行做好登陆准备

# 支持输入手机或电脑端优惠券地址，

# 模式1的抢卷过程:从运行开始就不断尝试抢卷，打码，如此循环。适合京东耍猴不放卷时使用。如线程开的够多密度够大，也适合正常半黑号抢卷使用

# 建议提前30秒左右就开始运行！如果需要提前测试，输入任何一个早于现在的时间即可！时间格式不可以改变，必须和例子格式相同！）
