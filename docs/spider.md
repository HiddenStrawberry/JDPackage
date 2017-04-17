京东抽奖爬虫 Spider.py
===================
这个文件用来爬取整个京东的LotteryCode抽奖代码，你可以通过这些抽奖代码进行抽奖。

----------


使用方法
----
----------
Spider是一个类，具体使用方法如下代码：

    t=Spider(20) #新建一个JDLottery爬虫，线程数为20

    # -- 加载地址到爬虫中 --
    rows = loadCSVfile('3.csv') 
    for each in rows:
        t._pool.append(each[0]) # _pool为需要爬取的地址池

    '''
    #1.csv包含14万京东店铺地址，如有需要请联系作者QQ付费使用。15RMB/1 File，若您已经购买，请去掉这段注释
    rows = loadCSVfile('1.csv')
    for each in rows:
        t._pool.append(each[0])
    '''
    # -- 加载完毕 --

    t.Strawberry('code.txt') #使用作者所写的爬取方法进行爬取，会生成文件名为code.txt的代码字典

----------

如果您不需要利用作者的代码写出您自己的个性京东爬虫，可忽略下文
-------------------------------


----------
Strawberry函数爬取的原理如下：

 1. 先遍历队列中所有地址，寻找所有的sale页面
 2. 除重，遍历第一步得到的sale页面寻找新的sale页面
 3. 除重，遍历第二步额外获得的新结果的sale页面寻找新的sale页面
 4. 除重，遍历所有结果页面获得lotterycode并保存为字典文件

作者使用了threading多线程以及数个队列结构，确保其**可以正常运行于Windows系统**并保证爬取的完整性，如果您有更好的方案比如替换threading使用gevent，可以通过运用Spider类中的如下函数实现：

    findsale(url) #查找页面中的sale地址页面，返回一个list
    findlc(salepage)#查找sale地址中的lotterycode，并将结果存入lc_dict字典

其中的一个变量**_algo**存有正则匹配lotterycode网页代码的算法，若京东日后修改，可以通过增加列表项实现。

----------

