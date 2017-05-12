#encoding=utf8
from __future__ import print_function
from .datacontrol import *
import requests
import time
import re
import datetime
import threading
from selenium import webdriver
import warnings
warnings.filterwarnings("ignore")


def lottery_time(userid, code, timet, delay, proxylist=None):
    time1 = datetime.datetime.strptime(timet, '%Y-%m-%d %H:%M:%S')
    if proxylist is None:
        proxylist = []
    cookiedt = []
    msglist = []
    ps = 0
    print('Verify Time:', timet)
    try:
        cookielist = loadCSVfile('cookies.csv')
    except:
        raise Exception('请确认Cookies文件存在!')
    for each in cookielist:
        try:
            if str(each[0]) == str(userid):
                cookiedt.append(each[1])
                print(each[2], 'Ready!')
        except:
            pass
    proxies = []
    if proxylist:
        ps = 1  # 代理模式开启
        for each in proxylist:
            proxies.append({'http': 'http://' + str(each[0]) + ':' + str(each[1])})
    enabled = 1
    while enabled == 1:
        time.sleep(0.1)
        if datetime.datetime.now() >= time1:
            for each in cookiedt:
                ck = 1
                headers = {'cookie': each,
                           'Referer': 'http://l.activity.jd.com/lottery/lottery_chance.action?lotteryCode=' + code}
                if ps == 1:
                    status = 0
                    while status == 0:
                        try:
                            print(proxies[0])
                            goprince = requests.get(
                                'http://l.activity.jd.com/lottery/lottery_start.action?lotteryCode=' + code,
                                headers=headers, proxies=proxies[0], verify=False).text
                            if decoder('登录') in goprince:
                                print(decoder('ID为') ,userid,decoder('的Cookies过期！'), each)
                                ck = 0
                            status = 1
                        except:
                            print("Network Error!Change Proxy and Retrying……")
                            del proxies[0]
                if ps == 0:
                    goprince = requests.get('http://l.activity.jd.com/lottery/lottery_start.action?lotteryCode=' + code,
                                            headers=headers, verify=False).text
                    if decoder('登录') in goprince:
                        print(decoder('ID为') , userid , decoder('的Cookies过期！'), each)
                        ck = 0
                winner = re.findall('"winner":(.*?)}', goprince, re.S)
                if str(winner) == '[u\'true\']':
                    print(code)
                    if ck == 1:
                        print(goprince)
                    msglist.append(goprince)
                # 如需屏蔽未中奖消息，请注释如下内容
                else:
                    print(code)
                    if ck == 1:
                        print(goprince)
                    msglist.append(goprince)
                # ----------------------------
                time.sleep(delay)
            enabled = 0
            # Fix later
            # f = open('f.txt', 'a')
            # for each in msglist:
            #     f.write(decoder(each))
            #     f.write('\n')
            # f.close()
            print('Finished!')


def add_lottery(userid, code, timet, delay, proxylist=None):
    if proxylist is None:
        proxylist = []
    threading.Thread(target=lottery_time, args=(userid, code, timet, delay, proxylist)).start()
    print(code)
    time.sleep(0.1)


def yuyue(userid, url):
    cookiedt=[]
    try:
        cookielist = loadCSVfile('cookies.csv')
    except:
        raise Exception('请确认Cookies文件存在!')
    for each in cookielist:
        try:
            if str(each[0]) == str(userid):
                cookiedt.append(each[1])
        except:
            pass
    for each in cookiedt:
        headers = {'Cookie': each,'Referer':url}
        html = requests.get(url,headers=headers,verify=False).text
        result = ''
        try:
            result = re.findall('<p class="bd-right-result">(.*?)</p>', html, re.S)[0]
            result=result.replace('<i>','').replace('</i>','')
        except Exception as err:
            print (err)
            pass
        print(result)


def read_lotteryfile(dictfile):
    dc = dict(eval(open(dictfile, 'rb').read()))
    for k, value in dc.items():
        if k != '':
            print(' ')
            print(k, value)
            headers = {'Referer': value}
            getinfo = requests.get('http://ls.activity.jd.com/lotteryApi/getLotteryInfo.action?lotteryCode=' + k,
                                   headers=headers, verify=False).text
            endtime = re.findall('"endTime":"(.*?)"', getinfo, re.S)[0]
            details = requests.get(value, verify=False).text
            title = re.findall('<meta content="(.*?)name="description"', details, re.S)[0]
            pricetype = re.findall('"prizeType":(.*?),"', getinfo, re.S)[0]
            yushou = re.search('yushou', details)
            prize = re.findall('"prizeName":"(.*?)"', getinfo, re.S)
            begintime = re.findall('"beginTime":"(.*?)"', getinfo, re.S)[0]
            prizedesc = re.findall('"prizeDesc":"(.*?)"', getinfo, re.S)
            print('Time:', begintime, '-', endtime)
            print('title:', title)
            print('Pricetype:', pricetype)
            if yushou:
                print(decoder('********************该抽奖可能需要预约********************'))
            print('code:', k)
            print('URL:'),
            print(value)
            print('Prize:')
            for eachprize in range(len(prize)):
                print('[', prize[eachprize], ']', '[', prizedesc[eachprize], ']')


def testwater(lotterycode):
    waterlist = []
    headers = {'referer': u'http://ls.activity.jd.com/lotteryApi/getWinnerList.action?lotteryCode=' + lotterycode}
    getwater = requests.get('http://ls.activity.jd.com/lotteryApi/getWinnerList.action?lotteryCode=' + lotterycode,
                            headers=headers, verify=False).text
    for eachwater in re.findall('{"prizeName":(.*?)}', getwater, re.S):
        prizename = re.findall('"(.*?)","userPin', eachwater, re.S)[0]
        windate = re.findall('"winDate":"(.*?)"', eachwater, re.S)[0]
        print(windate, prizename)
        waterlist.append([windate, prizename])
    return waterlist


def get_iplist(filename, page, sort):
    data = []
    driver = webdriver.PhantomJS()
    for r in range(1, page + 1):
        print ('Page',end='')
        print(r)
        driver.get('http://www.kuaidaili.com/free/' + str(sort) + '/' + str(r))
        tr = []
        while tr == []:
            tr = re.findall('<tr>(.*?)</tr>', driver.page_source, re.S)
            time.sleep(1)
        for each in re.findall('<tr>(.*?)</tr>', driver.page_source, re.S):
            try:
                ip = re.findall('<td data-title="IP">(.*?)</td>', each, re.S)[0]
                port = re.findall('<td data-title="PORT">(.*?)</td>', each, re.S)[0]

                tp = re.findall('<td data-title="' + decoder('类型') + '">(.*?)</td>', each, re.S)[0]
                loc = re.findall('<td data-title="' + decoder('位置') + '">(.*?)</td>', each, re.S)[0]
                speed = re.findall('<td data-title="' + decoder('响应速度') + '">(.*?)</td>', each, re.S)[0]
                last = re.findall('<td data-title="' + decoder('最后验证时间') + '">(.*?)</td>', each, re.S)[0]

                print (ip, port, tp,   last)
                data.append((ip, port, tp,   last))
            except Exception as err:
                print(err)
    driver.quit()
    writeCSVfile(filename, data)


def filter_iplist(filename, newfilename, timeout):
    successlist = []
    f = loadCSVfile(filename)
    for each in f:
        try:
            proxies = [{'http': 'http://' + str(each[0]) + ':' + str(each[1])}]
            requests.get('http://www.jd.com', proxies=proxies[0], timeout=timeout, verify=False)
            print ('Success', each[0], ':', each[1])
            successlist.append([each[0], each[1], each[2], each[3]])
        except:
            print ('Failed', each[0], ':', each[1])
    writeCSVfile(newfilename, successlist)

