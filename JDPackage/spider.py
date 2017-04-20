# encoding=utf8
from __future__ import print_function
import threading
import re
import time
import requests
import warnings
import copy
from .datacontrol import *

warnings.filterwarnings("ignore")


class Spider:
    def __init__(self, thread_amount):
        """Create a JDLotterySpider"""
        self.thread_amount = thread_amount
        self._headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/47.0.2526.80 Safari/537.36 Core/1.47.163.400 QQBrowser/9.3.7175.400'}
        self._algo = ["lotterycode:'(.*?)'", 'lotterycode=(.*?)"', 'data-code="(.*?)', 'lottNum="(.*?)"']
        # Lotterycode的正则算法，可自行更新（若京东页面更新）
        self._retry_times = 10
        self._pool = []
        self.salelist = []
        self.templist = []
        self.lc_dict = {}

    def Strawberry(self, filename):
        print(len(self._pool))
        """A Spider wrote by author,you can also use this lib to write your own JDSpider"""
        self.startpool(self._pool, self.salelist)
        print('Wait a while ^v^')
        time.sleep(20)

        print('Start')
        while len(self._pool) > 0:
            print(decoder('剩余网页数:'), end=' ')
            print(len(self._pool))
            time.sleep(1)
        self._pool = copy.deepcopy(self.salelist)
        self.startpool(self._pool, self.templist)

        while len(self._pool) > 0:
            print(decoder('剩余网页数:'), end='')
            print(len(self._pool))
            time.sleep(1)
        self.templist.extend(self.salelist)
        self.templist = list(set(self.templist))
        t = list(set(self.templist) ^ set(self.salelist))
        self.startpool(t, self.templist)
        while len(t) > 0:
            print(decoder('剩余网页数:'), end='')
            print(len(t))
            time.sleep(1)
        self.templist = list(set(self.templist))
        self.cf_pool(self.templist)
        while len(self.templist) > 0:
            print(decoder('剩余网页数:'), end='')
            print(len(self.templist))
            time.sleep(1)
        spider_file_csv(self.lc_dict, filename)

    def findsale(self, url):
        """Search JD-Salepage in webpage"""
        spset = []
        for times in range(self._retry_times):
            try:
                for each in re.findall('sale.jd.com/act/(.*?)' + '.html',
                                       requests.get(url, headers=self._headers, timeout=2).text, re.S):
                    spset.append('http://sale.jd.com/act/' + each + '.html')
                return spset
            except:
                time.sleep(1)

    def findlc(self, salepage):
        """Search lotterycode in JD-Salepage"""
        result = []
        for times in range(self._retry_times):
            try:
                for each in self._algo:
                    for each2 in re.findall(each, requests.get(salepage, headers=self._headers, timeout=2).text, re.S):
                        self.lc_dict[each2] = salepage
                return result
            except Exception as err:
                time.sleep(1)

    def runpool(self, pool, to_pool):
        while (len(pool) > 0):
            site = pool[0]
            pool.remove(site)
            try:
                for each in self.findsale(site):
                    each = each.lower()
                    to_pool.append(each)
            except Exception as err:
                print(err)
                pass

    def startpool(self, pool, to_pool):
        for num in range(0, self.thread_amount):
            threading.Thread(target=self.runpool, args=(pool, to_pool)).start()

    def cf_pool(self, pool):
        for num in range(0, self.thread_amount):
            threading.Thread(target=self.codefinding, args=(pool,)).start()

    def codefinding(self, pool):
        while len(pool) > 0:
            site = pool[0]
            pool.remove(site)
            self.findlc(site)


if __name__ == "__main__":
    t = Spider(100)  # 新建一个JDLottery爬虫，线程数为20，线程数的加大到一定程度内显著会加快速度，过大的线程数反而会减慢速度。
    # -- 加载地址到爬虫中 --
    for each in loadCSVfile('3.csv'):
        t._pool.append(each[0])

    '''
    1.csv包含14万京东店铺地址，如有需要请联系作者QQ付费使用。15RMB/1 File
    for each in loadCSVfile('1.csv'):
        t._pool.append(each[0])
    '''
    # -- 加载完毕 --
    t.Strawberry('code.txt')  # 使用作者所写的爬取方法进行爬取

# print t.findsale("http://www.jd.com")
# print t.findlc("http://sale.jd.com/act/bqAdSNyC1Jk.html")
