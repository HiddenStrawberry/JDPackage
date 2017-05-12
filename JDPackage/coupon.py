# encoding=utf-8
from __future__ import print_function
from .account import *
from .mlogin import *
import datetime
import random
import threading
import warnings
import re

warnings.filterwarnings("ignore")
times = 0


class Coupon(Account):
    def __init__(self, username, pwd, rk_um, rk_pw):
        Account.__init__(self, username, pwd, rk_um, rk_pw)

    def coupon_modeA(self, url_coupon, start, end,delay):
        url_filter = 'http://coupon.m.jd.com/coupons/show.action?key=' + re.findall('key=(.*?)&', url_coupon, re.S)[
            0] + '&roleId=' + re.findall('roleId=(.*?)&', url_coupon, re.S)[0] + '&to=m.jd.com'
        print (url_filter)
        start = datetime.datetime.strptime(start, '%Y-%m-%d %H:%M:%S')
        end = datetime.datetime.strptime(end, '%Y-%m-%d %H:%M:%S')
        threading.Thread(target=self.get_coupon_a, args=(url_filter, start, end,delay,)).start()

    def coupon(self, url):
        global times
        if self.ck != '':
            headers = {'Cookie': self.ck, 'Referer': url,
                       'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                     'Chrome/54.0.2840.59 Safari/537.36 115Browser/8.0.0',
                       'Accept': 'text/html,application/xhtml+xml, application/xml;q=0.9,*/*;q=0.8'}
            rdname = str(random.randint(1000000, 10000000))
            html = requests.get(url, headers=headers).text
            t1 = re.findall('id="codeKey"(.*?)id="couponBatch"', html, re.S)[0]
            try:
                ck = re.findall('authCodeImg.action\?key=(.*?)"', html, re.S)[0]
                ir = requests.get("http://coupon.m.jd.com/authCode/authCodeImg.action?key=" + str(ck),
                                  headers=headers)
                save_img('C:\\temp\\' + rdname + '.png', ir)
                validatecode = fuck_code_rk(self.rk_um, self.rk_pw, 'C:\\temp\\' + rdname + '.png')
            except:
                print(decoder('无需验证码，尝试直接领取'))
                validatecode = ''
                ck = ''
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
            print (re.findall('"returnMsg":"(.*?)"', now, re.S)[0],end='')
            times += 1
            print(times)

    def get_coupon_a(self, url, start, endtime,delay):
        global times
        enabled = 0

        while datetime.datetime.now() <= endtime:
            while endtime >= datetime.datetime.now() >= start:
                self.coupon(url)
                time.sleep(delay)
            time.sleep(0.1)

        print('Times Up!Process End.')

    def ajd_coupon(self, url, starttime):
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
        starttime = datetime.datetime.strptime(starttime, '%Y-%m-%d %H:%M:%S')
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
            print (title, typ, min_price, off_price, 'RMB', url, 'Available:', data_linkurl)
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
            print (title, typ, min_price, off_price, 'RMB', url, data_bean, 'JD Bean', 'Available:', data_linkurl)
            coupon_dict[data_id] = {'title': title,
                                    'min_price': min_price,
                                    'off_price': off_price,
                                    'data_id': data_id,
                                    'data_linkurl': data_linkurl,
                                    'data_bean': data_bean,
                                    'type': typ}

    return coupon_dict


def multi_couponA(a, b, c, d, count,delay,start, end, url):
    t = {}
    for x in range(1, count + 1):
        print (decoder('开始登陆第' + str(x) + '个账号'))
        t[x] = Coupon(a, b, c, d)
        t[x].login()
        print (decoder('第' + str(x) + '线程登陆成功'))
        t[x].coupon_modeA(url, start, end,delay)
