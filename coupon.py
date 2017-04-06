 #encoding=utf-8
from selenium import webdriver
from rk import *
from PIL import ImageTk
from selenium.webdriver.common.keys import Keys
import time
import datetime
import sys
import re
import random
import threading
import warnings
warnings.filterwarnings("ignore")
stdi,stdo,stde=sys.stdin,sys.stdout,sys.stderr
reload(sys)
sys.setdefaultencoding('utf-8',)
sys.stdin,sys.stdout,sys.stderr=stdi,stdo,stde
times=0
def login_check(html):
    if '图片验证码错误，请重试' in html:
        return False
    if '账号或密码不正确' in html:
        raise Exception('账号或密码不正确')
    return True
class Coupon:
    def __init__(self,username,pwd,rk_um,rk_pw):
        self.username=username
        self.pwd=pwd
        self.rc = RClient(rk_um, rk_pw)
        self.times=0
        self.ck=''
    def login(self):
        rdname = str(random.randint(1000000, 10000000))
        driver = webdriver.PhantomJS()
        url = 'https://plogin.m.jd.com/user/login.action?appid=100&kpkey=&returnurl=http%3A%2F%2Fm.jd.com%3Findexloc%3D1%26sid%3D9129920d9c239d7273eed31ddcc2a0ab'
        driver.get(url)
        while '专业网上购物平台品质保障' not in driver.title:
            driver.find_element_by_id("username").send_keys(self.username)
            driver.find_element_by_id("password").send_keys(self.pwd)
            driver.maximize_window()
            verify = False
            while verify == False:
                driver.save_screenshot('C:\\temp\\'+rdname+'.jpg')
                imgelement = driver.find_element_by_xpath('//*[@id="imgCode"]')
                location = imgelement.location
                size = imgelement.size
                rangle = (
                    int(location['x']), int(location['y']),
                    int(location['x'] + size['width']),
                    int(location['y'] + size['height']))
                frame4 = ImageTk.Image.open('C:\\temp\\'+rdname+'.jpg').crop(rangle)
                frame4.save('C:\\temp\\'+rdname+'.png')
                im = open('C:\\temp\\'+rdname+'.png','rb').read()
                print '开始识别验证码',
                try:
                    codex = self.rc.rk_create(im, 3040)['Result']
                except Exception as err:
                    print err
                    raise Exception("若快验证码识别出错！")
                print codex
                print '->识别成功',
                driver.find_element_by_id("code").send_keys(codex)
                driver.find_element_by_xpath('//*[@id="loginBtn"]').send_keys(Keys.ENTER)
                print '->登陆中……',
                time.sleep(2)
                verify = login_check(driver.page_source)
                enabled = 0
                while 1 == 1 and verify == True and enabled == 0:
                    while '专业网上购物平台品质保障' in re.findall('<title>(.*?)</title>', driver.page_source, re.S)[
                        0] and enabled == 0:
                        #print '->请稍后……',
                        cookie = [item["name"] + "=" + item["value"] for item in driver.get_cookies()]
                        self.ck = ';'.join(item for item in cookie)
                        print self.username, '->登陆成功！'

                        enabled = 1
        driver.quit()
    def new_coupon(self,url_coupon,timex):
        url_filter='https://coupon.m.jd.com/coupons/show.action?key='+re.findall('key=(.*?)&',url_coupon,re.S)[0]+'&roleId='+re.findall('roleId=(.*?)&',url_coupon,re.S)[0]+'&to=m.jd.com'
        url_filter=str(url_filter)
        print url_filter
        timex = datetime.datetime.strptime(timex, '%Y-%m-%d %H:%M:%S')
        enabled=0
        while enabled==0:
            if datetime.datetime.now() >= timex:
                threading.Thread(target=self.get_coupon, args=(url_filter,)).start()
                enabled=1
    def get_coupon(self,url):
        global times
        while 1 == 1:
            if self.ck!='':
                rdname = str(random.randint(1000000, 10000000))
                headers = {'Cookie': self.ck, 'Referer': url}
                html = requests.get(url, headers=headers).text
                ck = re.findall('authCodeImg.action\?key=(.*?)"', html, re.S)[0]
                ir = requests.get("http://coupon.m.jd.com/authCode/authCodeImg.action?key=" + str(ck), headers=headers)
                fp = open('C:\\temp\\'+rdname+'.png', 'wb')
                fp.write(ir.content)
                fp.close()
                im = open('C:\\temp\\'+rdname+'.png', 'rb').read()
                validatecode=self.rc.rk_create(im, 3040)['Result']
                t1 = re.findall('id="codeKey"(.*?)id="validateCodeSign"', html, re.S)[0]
                datax = {'sid': re.findall('sid=(.*?)"', html, re.S)[0],
                         'codeKey': ck,
                         'validateCode': validatecode,
                         'roleId': re.findall('value="(.*?)"', t1, re.S)[0],
                         'key': re.findall('value="(.*?)"', t1, re.S)[1],
                         'couponKey': re.findall('value="(.*?)"', t1, re.S)[2],
                         'activeId': re.findall('value="(.*?)"', t1, re.S)[3],
                         'couponType': re.findall('value="(.*?)"', t1, re.S)[4],
                         'to': re.findall('value="(.*?)"', t1, re.S)[5]}
                now = requests.post('http://coupon.m.jd.com/coupons/submit.json', headers=headers, data=datax).text
                print re.findall('"returnMsg":"(.*?)"',now,re.S)[0],
                times=times+1
                print times
            time.sleep(1)

if __name__=='__main__':
    t={}
    for x in range(5):
        t[x]=Coupon('abc','abc','abc','abc')
        threading.Thread(target=t[x].login).start()
    for x in range(5):
        t[x].new_coupon('https://coupon.m.jd.com/coupons/show.action?key=0397063756c644a39e304fc216f1d5f9&roleId=5978821&to=pro.m.jd.com/mall/active/4GLeHf2so2RB1TRtLQqSofdvtFHB/index.html','2017-03-08 20:57:30')