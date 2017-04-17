# encoding=utf-8
import requests
import time
import re
import sys
import csv
import datetime
import threading
from datacontrol import loadCSVfile
from selenium import webdriver
stdi, stdo, stde = sys.stdin, sys.stdout, sys.stderr
reload(sys)
sys.setdefaultencoding('utf-8', )
sys.stdin, sys.stdout, sys.stderr = stdi, stdo, stde

def lottery_time(userid, code, timet, delay, cookielist, proxylist=[]):
    cookiedt = []
    msglist = []
    ps = 0
    print 'Verify Time:',timet
    for each in cookielist:
        try:
            if str(each[0]) == str(userid):
                cookiedt.append(each[1])
                print each[2],'Ready!'
        except:
            pass
    proxies = []

    if proxylist != []:
        ps = 1  # 代理模式开启
        for each in proxylist:
            proxies.append({'http': 'http://' + str(each[0]) + ':' + str(each[1])})
    time1 = datetime.datetime.strptime(timet, '%Y-%m-%d %H:%M:%S')
    enabled = 1
    while enabled == 1:
        time.sleep(0.1)
        if datetime.datetime.now() >= time1:
            for each in cookiedt:
                ck=1
                headers = {'cookie': each,
                           'Referer': 'http://l.activity.jd.com/lottery/lottery_chance.action?lotteryCode=' + code}
                if ps == 1:
                    status = 0
                    while status == 0:
                        try:
                            print proxies[0]
                            goprince = requests.get(
                                'http://l.activity.jd.com/lottery/lottery_start.action?lotteryCode=' + code,
                                headers=headers, proxies=proxies[0], verify=False).text
                            if '登录' in goprince:
                                print 'ID为'+userid+'的Cookies过期！',each
                                ck=0
                            status = 1
                        except:
                            print "Network Error!Change Proxy and Retrying……"
                            del proxies[0]
                if ps == 0:
                    goprince = requests.get('http://l.activity.jd.com/lottery/lottery_start.action?lotteryCode=' + code,
                                            headers=headers, verify=False).text
                    if '登录' in goprince:
                        print 'ID为' + userid + '的Cookies过期！',each
                        ck=0
                winner = re.findall('"winner":(.*?)}', goprince, re.S)
                if str(winner) == '[u\'true\']':
                    print code
                    if ck==1:
                        print goprince
                    msglist.append(goprince)
                ###########如需屏蔽未中奖消息，请注释如下内容
                else:
                    print code
                    if ck==1:
                        print goprince
                    msglist.append(goprince)
                ###########----------------------------
                time.sleep(delay)
            enabled = 0
            f = open('f.txt', 'a')
            for each in msglist:
                f.write(str(each))
                f.write('\n')
            f.close()
            print 'Finished!'

def add_lottery(userid, code, timet, delay, cookielist, proxylist=[]):
    threading.Thread(target=lottery_time, args=(userid, code, timet, delay, cookielist, proxylist)).start()
    print code
    time.sleep(0.1)

def read_lotteryfile(dictfile):
    dc = dict(eval(open(dictfile, 'rb').read()))
    for k, value in dc.items():
        if k != '':
            print k,value
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
            print ' '
            print 'title:',title
            print 'Pricetype:',pricetype
            if yushou:
                print '********************该抽奖可能需要预约********************'
            print 'code:',k
            print 'URL:',
            print value
            print 'Prize:',
            for eachprize in prize:
                if eachprize:
                    eachprize = eachprize.encode('gbk')
                    print '[',eachprize, ']',' ',
            print ''
            print 'Time:',begintime,'-',endtime
            print 'PrizeDesc:'
            for eachprizedesc in prizedesc:
                print '[',eachprizedesc,']'

def testwater(lotterycode):
    waterlist=[]
    headers={'referer':u'http://ls.activity.jd.com/lotteryApi/getWinnerList.action?lotteryCode='+lotterycode}
    count=0
    getwater=requests.get('http://ls.activity.jd.com/lotteryApi/getWinnerList.action?lotteryCode='+lotterycode,headers=headers,verify=False).text
    for eachwater in re.findall('{"prizeName":(.*?)}',getwater,re.S):
        prizename=re.findall('"(.*?)","userPin',eachwater,re.S)[0]
        windate=re.findall('"winDate":"(.*?)"',eachwater,re.S)[0]
        print windate,prizename
        waterlist.append([windate,prizename])
    return waterlist

def get_iplist(filename,page,sort):
    data=[]
    driver = webdriver.PhantomJS()
    csvfile = file(filename, 'wb')
    for r in range(1,page+1):
        print 'Page',
        print r
        a=driver.get('http://www.kuaidaili.com/free/'+str(sort)+'/'+str(r))
        tr=[]
        while tr==[]:
            tr=re.findall('<tr>(.*?)</tr>',driver.page_source,re.S)
        for each in re.findall('<tr>(.*?)</tr>',driver.page_source,re.S):
            try:
                ip=re.findall('<td data\-title="IP">(.*?)</td>',each,re.S)[0]
                port=re.findall('<td data\-title="PORT">(.*?)</td>',each,re.S)[0]
                tp=re.findall('<td data-title="'+'类型'.decode('utf8')+'">(.*?)</td>',each,re.S)[0]
                loc=re.findall('<td data-title="'+'位置'.decode('utf8')+'">(.*?)</td>',each,re.S)[0]
                speed=re.findall('<td data-title="'+'响应速度'.decode('utf8')+'">(.*?)</td>',each,re.S)[0]
                last=re.findall('<td data-title="'+'最后验证时间'.decode('utf8')+'">(.*?)</td>',each,re.S)[0]
                print ip,port,tp,loc,speed,last
                data.append((ip,port,tp,loc,speed,last))
            except Exception as err:
                print err
    driver.quit()
    writer = csv.writer(csvfile)
    writer.writerows(data)
    csvfile.close()

def filter_iplist(filename,newfilename,timeout):
    successlist=[]
    for each in loadCSVfile(filename):
        try:
            proxies=[]
            proxies.append({'http':'http://'+str(each[0])+':'+str(each[1])})
            requests.get('http://www.jd.com',proxies=proxies[0],timeout=timeout,verify=False)
            print 'Success', each[0] ,':', each[1]
            successlist.append((each[0],each[1],each[2],each[3],each[4],each[5]))
        except Exception as err:
            print 'Failed', each[0] ,':', each[1]
    csvfile = file(newfilename, 'wb')
    writer = csv.writer(csvfile)
    writer.writerows(successlist)
    csvfile.close()

if __name__ == "__main__":
    #read_lotteryfile('code.txt')
    '''
    get_iplist('ip.csv', 3, 'inha')  # 参数为（文件名，页数，代理类别）；代理类别包含4种(inha:国内高匿,intr:国内普通,outha:国外高匿,outtr:国外普通
    filter_iplist('ip.csv', 'new.csv', 2)  # 过滤出有效IP并存储为new.csv 参数为（文件名，过滤后的文件名，超时判定秒数）

    cookielist = loadCSVfile('cookies.csv')  # 加载Cookies文件
    proxylist = loadCSVfile('new.csv')  # 加载代理地址文件
    add_lottery('1', '4b6c385f-a626-48d2-8abe-f2ce2ebe5d5f', '2017-03-08 20:57:30', 5, cookielist, proxylist)  # 代理模式
    #add_lottery('1','4b6c385f-a626-48d2-8abe-f2ce2ebe5d5f','2017-03-08 20:57:30',5,cookielist) #无代理模式
    '''
    cookielist = loadCSVfile('cookies.csv')
    add_lottery('1', 'b061839a-fa56-48a2-98aa-718700110405', '2017-04-10 10:44:30', 5, cookielist, proxylist=[])