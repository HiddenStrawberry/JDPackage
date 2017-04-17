from JDPackage import *
#DOCS : https://github.com/HiddenStrawberry/JDPackage/blob/master/docs/account.md
a=Account('#', '#', '#', '#') #新建账号
a.login_pc() #账号登录
a.get_couponlist() #获取优惠券列表
a.get_msglist() #获取消息列表
a.get_payment() #获取订单列表