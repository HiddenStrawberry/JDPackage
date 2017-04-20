京东优惠券工具包Coupon.py
===============


----------


这个文件是优惠券工具的主程序。包括了如下功能：

 - 多线程优惠券领取工具（测试版）
 - 其他功能不断更新中……

----------

 - 多线程优惠券领取工具（领取模式1）
------------------
使用须知（必看）
> 1. 本工具仅供研究Python的各个模块使用，请勿用于非法用途！
> 2. 本工具优惠券领取全自动实现，打码部分使用了若快打码API，使用本工具前您需要申请若快账号并充值一定的金额，价格1元/250个验证码。
> http://ruokuai.com/login 请选择我是用户，并注册。
> 3. 请确定C:/Temp这个目录存在！（重要），这个目录用来存放验证码图片文件，可以随时删除，如您使用Linux系统，请手动更改程序中的目录。
> 4. 请仔细阅读本文档，如有任何问题欢迎添加QQ交流群：108934299




这个工具包括两个部分：

账号部署和开始领卷
-------
我个人建议通过反复尝试来确定最好的线程数，只要你的配置够好，就可以开更多的线程，加快领卷速度，从而使得领到卷的概率更大。
单线程单账号领卷部署及登录，然后领卷：

    #encoding=utf-8
    from JDPackage import *
    a = Coupon('#', '#', '#', '#')
    #          京东账号     京东密码    若快账号     若快密码
    a.login()
    a.new_coupon(
    	'https://coupon.jd.com/ilink/couponActiveFront/front_index.action?key=61ea1f3fa9804499948617652d256485&roleId=6063883&to=mall.jd.com/index-13001.html',
    	'2017-03-08 20:57:30','2017-04-21 00:11:40')

多线程单账号领卷部署及登录，然后领卷：（举例10线程领卷）

   

    #encoding=utf-8
    from JDPackage import *
    multi_coupon('#','#','#','#',10, #京东账号,京东密码,若快账号,若快密码,线程数
                 '2017-03-08 20:57:30','2017-04-21 00:11:40', #开始时间,结束时间
                 'https://coupon.jd.com/ilink/couponActiveFront/front_index.action?key=61ea1f3fa9804499948617652d256485&roleId=6063883&to=mall.jd.com/index-13001.html'
                 ) #    卷地址

多账号多线程领卷部署及登录，然后领卷：（举例5线程领卷）

    #encoding=utf-8
    from JDPackage import *
    multi_coupon('#','#','#','#',10, 
                '2017-03-08 20:57:30','2017-04-21 00:11:40', 
                'https://coupon.jd.com/ilink/couponActiveFront/front_index.action?key=61ea1f3fa9804499948617652d256485&roleId=6063883&to=mall.jd.com/index-13001.html')  #账号1
                
    multi_coupon('#','#','#','#',10, 
                '2017-03-08 20:57:30','2017-04-21 00:11:40', 
                'https://coupon.jd.com/ilink/couponActiveFront/front_index.action?key=61ea1f3fa9804499948617652d256485&roleId=6063883&to=mall.jd.com/index-13001.html')   #账号2

----------

- 获取a.jd.com的优惠券列表
------------------

    get_ajd_list('http://a.jd.com/coupons.html?page=1&at=2')

你可以获取任意a.jd.com页面中的优惠券，具体返回值请参见代码。

out:



    仅可购买自营家纺指定商品 东券 满29元可用 20 RMB http://a.jd.com/ajax/freeGetCoupon.html?key=b2d9446d26d715074358c711d6e6a0909b39488ab170b36381f3151de5dcc42161fe300d32e5fc53f4dc3c57b5c968e3&r=0.7308938041372057 Available: http://search.jd.com/Search?coupon_batch=35653852
    仅可购买健身车/动感单车、体育用品部分商品 东券 满499元可用 100 RMB http://a.jd.com/ajax/freeGetCoupon.html?key=5ae0b723f1e0a1d18025c0feb3678f0278a50d3cef1428749d34dd576c022707619a78ef45f3acc4f01ecc125bf68e2a&r=0.7308938041372057 Available: http://search.jd.com/Search?coupon_batch=35734211
    ……

其中第一个地址为领取地址，作用于下面的领取工具，第二个地址为卷可用商品链接。


----------

-领取a.jd.com的优惠券
---------------

    a= Coupon('#', '#', '#', '#')
    a.login_pc()
    a.get_ajd_coupon('http://a.jd.com/ajax/freeGetCoupon.html?key=f8d0c71b6a4607a435340fb45cec002660d4259919d9d32026976effd53bb7dbb6c0cd979127aa34d4664d7e12339de1&r=0.7308938041372057',
                   '2017-04-17 20:03:50')

请注意这里的登录使用的是login_pc()函数。get_ajd_coupon()的参数为：领取地址，领取时间，请注意！这个领卷函数只会在设定时间领取一次！（因为a.jd.com不支持反复尝试领卷，会导致频繁）

