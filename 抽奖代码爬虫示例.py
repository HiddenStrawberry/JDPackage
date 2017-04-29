#encoding=utf-8
from JDPackage import *
#DOCS : https://github.com/HiddenStrawberry/JDPackage/blob/master/docs/spider.md

#运行爬虫
t=Spider(100) #新建一个JDLottery爬虫，线程数为20

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

#读取代码：
read_lotteryfile('code.txt') #输出抽奖代码具体内容
