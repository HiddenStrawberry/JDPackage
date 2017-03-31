#encoding=utf-8
import requests
import time
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import csv

stdi,stdo,stde=sys.stdin,sys.stdout,sys.stderr
reload(sys)
sys.setdefaultencoding('utf-8',) 
sys.stdin,sys.stdout,sys.stderr=stdi,stdo,stde
def loadCSVfile(file):
    csv_reader = csv.reader(open(file))
    return csv_reader
def login(userid):
    data=[]
    driver = webdriver.Firefox()
    url = 'https://passport.jd.com/uc/login?ltype=logout'
    driver.get(url)
    enable=0
    while enable==0:
        if driver.title=="京东(JD.COM)-正品低价、品质保障、配送及时、轻松购物！":
            cookie = [item["name"] + "=" + item["value"] for item in driver.get_cookies()]
            cookiestr = ';'.join(item for item in cookie)
            driver.quit()
            enable=1
    rows=loadCSVfile('cookies.csv')
    for each in rows:
        data.append(each)
    data.append([userid,cookiestr])
    csvfile = file('cookies.csv', 'wb')
    writer = csv.writer(csvfile)
    writer.writerows(data)
    csvfile.close()
login('1')
'''

    login(userid)
    

 - userid可以是重复的，如果您在两个账号录入了相同的userid，那么在执行抽奖，领卷时这些相同的ID会同时执行抽奖，领卷。
执行此函数后，Python会启动Firefox，弹出京东登录窗口，输入账号密码登陆后，请等待Firefox自行关闭。

账号多且有Python基础的用户可以使用日后推出的完整版（全自动打码登录）
'''  
