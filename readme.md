﻿﻿京东全能工具包 JDPackage V2.3
===================
作者已停止更新！部分功能可能不可用，欢迎修复问题commit发pr给我，我觉得可以就合并进来！

![python](https://img.shields.io/badge/language-python-orange.svg)

![此处输入图片的描述][1]

特性：
---

 1. 丰富的可扩展性：丰富的文档帮助你借助本程序二次开发出个性化的程序。
 2. 同时兼容Python2/3：无需考虑兼容性问题。
 3. 轻量化：仅依赖3个第三方包（requests，pillow4.0.0，selenium2.53.0）
 4. 全自动：全自动定时抢卷/抽奖功能，并支持多线程，配置有多高，速度就有多快。
 5. 对新手友好：大量的示例，即便不会Python也能快速构建环境。
目前已经实现的功能：
----------
各文件开发文档地址：https://github.com/HiddenStrawberry/JDPackage/wiki

 1. Spider.py #京东抽奖LotteryCode爬虫
 
- 京东抽奖代码爬虫

 2. Lotterypack.py #京东抽奖工具包
 
 - 支持代理IP的定时抽奖工具
 - kuaidaili.com免费代理IP获取+过滤有效IP工具
 - Lotterycode测水工具

 3. account.py #京东账户信息管理工具包
 
 - 浏览器Cookies载入（只要有一段Cookie，就可以在Firefox实现直接登录而无需账号/密码，可以跳过手机验证及风险验证）
 - 电脑端及M端登录
 - 获取优惠券列表
 - 获取消息列表
 - 获取订单列表

 4. datacontrol.py #文件及数据库处理
 - Python2/3兼容性处理
 - CSV文件读写

 5. rk.py #若快打码组件
 
 6. coupon.py # 京东优惠券工具包
 - M端/电脑端优惠券领取
 - 获取a.jd.com领卷中心的任意页面的任意优惠券领取地址
 - 领取a.jd.com领卷中心任意优惠券

 7. mlogin.py #京东M端登陆模拟执行

 8. JDEncrypt.html #京东PC端登陆模拟执行


所有功能都有对应的极为详尽的由作者煞费苦心写的文档及具体的使用例子，可以到docs目录中查看各个文件的文档，新手请参阅[新手教程][2]。

使用方法：

    from JDPackage import *

----------

说明
--
 - 本工具包持续更新
 - 程序仅供您研究使用，严禁用于非法用途，因程序产生的一切问题与源码作者无关



----------

作者QQ：1317171753，学习群：108934299
---------------


  [1]: https://www.gnu.org/graphics/gplv3-127x51.png
  [2]: https://github.com/HiddenStrawberry/JDPackage/wiki/%E6%96%B0%E6%89%8B%E6%95%99%E7%A8%8B
