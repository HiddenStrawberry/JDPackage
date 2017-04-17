#encoding=utf-8
from JDPackage import *

#DOCS : https://github.com/HiddenStrawberry/JDPackage/blob/master/docs/coupon.md
get_ajd_list('http://a.jd.com/coupons.html?page=3')
#                         优惠券列表地址
t={}
t[0] = Coupon('#', '#', '#', '#')
#          京东账号     京东密码    若快账号     若快密码
t[0].login_pc()
t[0].get_ajd_coupon('http://a.jd.com/ajax/freeGetCoupon.html?key=f8d0c71b6a4607a435340fb45cec002660d4259919d9d32026976effd53bb7dbb6c0cd979127aa34d4664d7e12339de1&r=0.7308938041372057',
               '2017-04-17 20:00:00')
#               优惠券链接,开始领取的时间0