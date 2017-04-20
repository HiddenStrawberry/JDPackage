# encoding=utf-8
from __future__ import print_function
from .account import *
import datetime
import random
import os
import threading
import warnings
import re

warnings.filterwarnings("ignore")
times = 0


class Coupon(Account):
    def __init__(self, username, pwd, rk_um, rk_pw):
        Account.__init__(self, username, pwd, rk_um, rk_pw)
        if os.path.isdir('C:\Temp'):
            pass
        else:
            os.mkdir('C:\Temp')

    def new_coupon(self, url_coupon, timex, endtime):
        url_filter = 'http://coupon.m.jd.com/coupons/show.action?key=' + re.findall('key=(.*?)&', url_coupon, re.S)[
            0] + '&roleId=' + re.findall('roleId=(.*?)&', url_coupon, re.S)[0] + '&to=m.jd.com'
        url_filter = str(url_filter)
        print(url_filter)
        timex = datetime.datetime.strptime(timex, '%Y-%m-%d %H:%M:%S')
        endtime = datetime.datetime.strptime(endtime, '%Y-%m-%d %H:%M:%S')
        enabled = 0
        while enabled == 0:
            if datetime.datetime.now() >= timex:
                threading.Thread(target=self.get_coupon, args=(url_filter, endtime,)).start()
                print('Process Start')
                enabled = 1

    def get_coupon(self, url, endtime):
        global times
        while datetime.datetime.now() <= endtime:
            if self.ck != '':
                rdname = str(random.randint(1000000, 10000000))
                headers = {'Cookie': self.ck, 'Referer': url}
                html = requests.get(url, headers=headers).text
                try:
                    ck = re.findall('authCodeImg.action\?key=(.*?)"', html, re.S)[0]
                    ir = requests.get("http://coupon.m.jd.com/authCode/authCodeImg.action?key=" + str(ck),
                                      headers=headers)
                    fp = open('C:\\temp\\' + rdname + '.png', 'wb')
                    fp.write(ir.content)
                    fp.close()
                    im = open('C:\\temp\\' + rdname + '.png', 'rb').read()
                    validatecode = self.rc.rk_create(im, 3040)['Result']
                except:
                    print(decoder('无需验证码，尝试直接领取'))
                    validatecode = ''
                    ck = ''
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
                print(re.findall('"returnMsg":"(.*?)"', now, re.S)[0], end='')
                times = times + 1
                print(times)
        print('Times Up!Process End.')

    def ajd_coupon(self, url, starttime):
        starttime = datetime.datetime.strptime(starttime, '%Y-%m-%d %H:%M:%S')
        headers = {'Cookie': self.ck_pc,
                   'Referer': url
                   }
        enabled = 0
        while enabled == 0:
            time.sleep(0.1)
            if datetime.datetime.now() >= starttime:
                a = requests.get(url, headers=headers).text
                print(a)
                enabled = 1

    def get_ajd_coupon(self, url, starttime):
        threading.Thread(target=self.ajd_coupon, args=(url, starttime,)).start()


def get_ajd_list(url):
    coupon_dict = {}
    html = requests.get(url).text
    coupon = re.findall('<div class="quan-item(.*?)<div class="q-state">', html, re.S)
    for each in coupon:
        title = re.findall('<p title="(.*?)"', each, re.S)[0]
        min_price = re.findall('<span class="ftx-06">(.*?)</span>', each, re.S)[0].replace('\n', '').replace(' ', '')
        off_price = re.findall('<strong class="num">(.*?)</strong>', each, re.S)[0]
        typ = re.findall('div class="typ-txt">(.*?)</div>', each, re.S)[0]
        data_linkurl = 'http://' + re.findall('data-linkUrl="//(.*?)"', each, re.S)[0]
        try:
            datakey = re.findall('data-key="(.*?)"', each, re.S)[0]
            url = 'http://a.jd.com/ajax/freeGetCoupon.html?key=' + datakey + '&r=0.7308938041372057'
            print(title, typ, min_price, off_price, 'RMB', url, 'Available:', data_linkurl)
            coupon_dict[datakey] = {'title': title,
                                    'min_price': min_price,
                                    'off_price': off_price,
                                    'datakey': datakey,
                                    'data_linkurl': data_linkurl,
                                    'type': typ}
        except:
            data_id = re.findall('data-id="(.*?)"', each, re.S)[0]
            data_bean = re.findall('data-bean="(.*?)"', each, re.S)[0]
            url = 'http://a.jd.com/ajax/beanExchangeCoupon.html?id=' + data_id + '&r=0.5559653794026669'
            print(title, typ, min_price, off_price, 'RMB', url, data_bean, 'JD Bean', 'Available:', data_linkurl)
            coupon_dict[data_id] = {'title': title,
                                    'min_price': min_price,
                                    'off_price': off_price,
                                    'data_id': data_id,
                                    'data_linkurl': data_linkurl,
                                    'data_bean': data_bean,
                                    'type': typ}

    return coupon_dict


def multi_coupon(a, b, c, d, count, start, end, url):
    t = {}
    print(decoder('新建了一个线程为') + str(count) + decoder('的领卷任务'))
    for x in range(count):
        t[x] = Coupon(a, b, c, d)
        t[x].login()
        t[x].new_coupon(url, start, end)


if __name__ == '__main__':
    get_ajd_list('http://a.jd.com/')
    t = {0: Coupon('#', '#', '#', '#')}
    t[0].login_pc()
    t[0].get_ajd_coupon(
        'http://a.jd.com/ajax/freeGetCoupon.html?key'
        '=f8d0c71b6a4607a435340fb45cec002660d4259919d9d32026976effd53bb7dbb6c0cd979127aa34d4664d7e12339de1&r=0'
        '.7308938041372057',
        '2017-04-17 20:03:50')
    # t[0].new_coupon(
    #     'https://coupon.jd.com/ilink/couponActiveFront/front_index.action?key=61ea1f3fa9804499948617652d256485&roleId=6063883&to=mall.jd.com/index-13001.html',
    #     '2017-03-08 20:57:30','2017-04-08 00:11:40')
