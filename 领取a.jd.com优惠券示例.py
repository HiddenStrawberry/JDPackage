#encoding=utf-8
from JDPackage import *

#DOCS : https://github.com/HiddenStrawberry/JDPackage/blob/master/docs/coupon.md


get_ajd_list('http://a.jd.com/coupons.html?page=3')  #获取优惠卷列表
#                         优惠券列表地址



a = Coupon('#', '#', '#', '#')
#          京东账号     京东密码    若快账号     若快密码


a.login_pc() #账号PC端登录


a.get_ajd_coupon('http://a.jd.com/ajax/freeGetCoupon.html?key=f8d0c71b6a4607a435340fb45cec002660d4259919d9d32026976effd53bb7dbb6c0cd979127aa34d4664d7e12339de1&r=0.7308938041372057',
               '2017-04-17 20:00:00')
#               优惠券链接,
#               开始领取的时间


a.get_couponlist() #查询当前优惠卷列表
