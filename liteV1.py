#encoding=utf8
import sys
import threading
import requests
import re
import time
import os
import csv
import warnings
warnings.filterwarnings("ignore")
lc_dict={}
pooltemp=[]
salelist=[]
salelist2=[]
tr=20 #线程数
'''
程序爬取路径：遍历CSV中地址,并在其中搜索SALE页面 ->在SALE页面中搜索SALE页面 ->搜索LC码
程序采用多线程+队列结构，确保爬取完整性。
'''
def findsale(url):
    x=0
    for j in range(10):
        try:
            headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36 Core/1.47.163.400 QQBrowser/9.3.7175.400'}
            html=requests.get(url,headers=headers,verify=False).text
            salepage=re.findall('sale.jd.com/act/(.*?)'+'.html',html,re.S)
            return salepage
            break  
        except Exception as err:
            time.sleep(1)

def findlc(salepage):
    for j in range(10):
        try:
            headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36 Core/1.47.163.400 QQBrowser/9.3.7175.400'}
            html=requests.get('http://sale.jd.com/act/'+salepage+'.html',headers=headers,verify=False).text
            lottery=re.findall('lotterycode:\'(.*?)\'',html,re.S)
            for every_lott in lottery:
                lc_dict[every_lott]=salepage
            lottery2=re.findall('lotterycode=(.*?)"',html,re.S)
            for every_lott2 in lottery2:
                lc_dict[every_lott2]=salepage   
            lottery3=re.findall('data-code="(.*?)',html,re.S)
            for every_lott3 in lottery3:
                lc_dict[every_lott3]=salepage
            lottery4=re.findall('lottNum="(.*?)"',html,re.S)
            for every_lott4 in lottery4:
                lc_dict[every_lott4]=salepage  
            break
        except Exception as err:
            time.sleep(1)
def loadCSVfile(file):
    csv_reader = csv.reader(open(file))
    return csv_reader
def build_sitepool():
    print '开始建立地址库'
    try:
        '''
        1,2 CSV文件含有13万店铺地址信息，如有特殊需要请联系作者付费
        rows=loadCSVfile('1.csv')
        for each in rows:
            pooltemp.append(each[0])
        rows=loadCSVfile('2.csv')
        for each in rows:
            pooltemp.append('http://'+str(each[0]))
        '''
        rows=loadCSVfile('3.csv')
        for each in rows:
            pooltemp.append(each[0])
        
        print '地址库长度:',
        print len(pooltemp)
    except:
        raise Exception('地址库加载失败！')
def startpool():    
    for x in range(0,tr):
        threading.Thread(target = runpool,).start()
    print '开始运行POOL 1'
def runpool():
    while(len(pooltemp)>0):
        site=pooltemp[0]
        del pooltemp[0]
        try:
            salepage=findsale(site)
            for each in salepage:
                
                each=each.lower()
                salelist.append(each)
        except:
            pass
def startpool2():    
    for x in range(0,tr):
        threading.Thread(target = runpool2,).start()
    print '开始运行POOL 2'
def runpool2():
    while(len(salelist)>0):
        site=salelist[0]
        del salelist[0]
        salelist2.append(site)
        try:
            salepage=findsale('http://sale.jd.com/act/'+str(site)+'.html')
            for each in salepage:
                each=each.lower()
                salelist2.append(each)
        except:
            pass
def jdcf():
    for x in range(0,tr):
        threading.Thread(target = codefinding,).start()
def codefinding():    
    while len(salelist2)>0:
        site=salelist2[0]
        del salelist2[0]
        findlc(site)
def read_dict(dictfile):
    a2=open(dictfile,'rb')    
    c2={}
    c2=a2.read()
    c2=dict(eval(c2))
    for k,value in c2.items():
        if k!='':
            print k
            print value
            headers={'Referer':'http://sale.jd.com/act/'+value+'.html'}
            getinfo=requests.get('http://ls.activity.jd.com/lotteryApi/getLotteryInfo.action?lotteryCode='+k,headers=headers,verify=False).text
            endtime=re.findall('"endTime":"(.*?)"',getinfo,re.S)[0]
            details=requests.get('http://sale.jd.com/act/'+value+'.html',verify=False).text
            title=re.findall('<meta content="(.*?)name="description"',details,re.S)[0]
            pricetype=re.findall('"prizeType":(.*?),"',getinfo,re.S)[0]
            yushou=re.search('yushou',details)
            prize=re.findall('"prizeName":"(.*?)"',getinfo,re.S)
            begintime=re.findall('"beginTime":"(.*?)"',getinfo,re.S)[0]
            prizedesc=re.findall('"prizeDesc":"(.*?)"',getinfo,re.S)
            print ' '
            print 'title:',
            print title
            print 'Pricetype:',
            print pricetype
            if yushou:
                print '********************该抽奖可能需要预约********************'
            print 'code:',
            print k
            print 'URL:',
            print 'http://sale.jd.com/act/'+value+'.html'
            print 'Prize:',
            for eachprize in prize:
                if eachprize:
                    eachprize=eachprize.encode('gbk')
                    print '[',
                    print eachprize,
                    print ']',
                    print ' ',
            print ''
            print 'Time:',
            print begintime,
            print '-',
            print endtime
            print 'PrizeDesc:'
            
            for eachprizedesc in prizedesc:
                print '[',
                print eachprizedesc,
                print ']'
            
def spider(filez):
    global salelist
    global salelist2
    build_sitepool()
    startpool()
    while len(pooltemp)>0:
        print '剩余网页数:',
        print len(pooltemp)
        time.sleep(3)
    salelist = list(set(salelist))
    startpool2()
    while len(salelist)>0:
        print '剩余网页数:',
        print len(salelist)
        time.sleep(3)
    salelist2 = list(set(salelist2))
    jdcf()
    while len(salelist2)>0:
        print '剩余网页数:',
        print len(salelist2)
        time.sleep(3)
    print lc_dict
    s = str(lc_dict)
    f = file(filez,'w')
    f.writelines(s)
    f.close()
    return lc_dict
def testwater(lotterycode):
    waterlist=[]
    headers={'referer':u'http://ls.activity.jd.com/lotteryApi/getWinnerList.action?lotteryCode='+lotterycode}
    count=0
    getwater=requests.get('http://ls.activity.jd.com/lotteryApi/getWinnerList.action?lotteryCode='+lotterycode,headers=headers,verify=False).text  
    lastwater=re.findall('{"prizeName":(.*?)}',getwater,re.S)
    for eachwater in lastwater:
        prizename=re.findall('"(.*?)","userPin',eachwater,re.S)[0]
        windate=re.findall('"winDate":"(.*?)"',eachwater,re.S)[0]
        print windate,
        print prizename
        waterlist.append([windate,prizename])
    return waterlist
if __name__ == "__main__":
    #spider('code.txt') #运行爬虫程序，并将结果存入文件 code.txt
    #read_dict('code.txt') #输出抽奖代码具体内容
    print testwater('d2d7f4a5-adb7-41c5-96ce-ba923ea88eba') #输出某代码最近的出奖时间,返回一个list，结构为[[Windate,Prizename],[Windate,Prizename],..,]
