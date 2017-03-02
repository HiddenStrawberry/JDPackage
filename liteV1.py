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
            for every_lott4 in lottery3:
                lc_dict[every_lott4]=salepage  
            break
        except Exception as err:
            print err
            time.sleep(1)
def loadCSVfile(file):
    csv_reader = csv.reader(open(file))
    return csv_reader
def build_sitepool():
    print '开始建立地址库'
    try:
        '''
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
        salepage=findsale(site)
        for each in salepage:
            each=each.lower()
            salelist.append(each)
def startpool2():    
    for x in range(0,tr):
        threading.Thread(target = runpool2,).start()
    print '开始运行POOL 2'
def runpool2():
    while(len(salelist)>0):
        site=salelist[0]
        del salelist[0]
        salelist2.append(site)
        salepage=findsale('http://sale.jd.com/act/'+str(site)+'.html')
        for each in salepage:
            each=each.lower()
            salelist2.append(each)        
def jdcf():
    for x in range(0,tr):
        threading.Thread(target = codefinding,).start()
def codefinding():    
    while len(salelist2)>0:
        site=salelist2[0]
        del salelist2[0]
        findlc(site)
        
if __name__ == "__main__":  
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
