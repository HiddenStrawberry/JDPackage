# encoding=utf-8
from __future__ import print_function
from .rk import *
from .mlogin import *
from .datacontrol import *
import time
import re
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0 "
)


class Account:
    def __init__(self, username, pwd, rk_um, rk_pw):
        self.username = username
        self.pwd = pwd
        self.rc = RClient(rk_um, rk_pw)
        self.rk_um = rk_um
        self.rk_pw = rk_pw
        self.ck = ''
        self.ck_pc = ''
        self.ck_browser = ''
        self.ck_pc_browser = ''
        self.session = requests.session()

    def login(self):
        # 2017/04/27 JDMLogin Cracked
        print(self.username, end=' ')
        st = True
        while st == True:
            self.ck = login(self.username, self.pwd, self.rk_um, self.rk_pw)
            st = False
        return self.ck


    def login_pc(self):
        # 2017/04/27 JDLogin HTML Version Updated

        rdname = str(random.randint(1000000, 10000000))
        t = requests.session()
        cookiestr = ''
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/54.0.2840.59 Safari/537.36 115Browser/8.0.0',
            'Accept': 'application / json'
        }
        headers2={'Accept': 'image/webp,image/*,*/*;q=0.8'}
        html = t.get('http://passport.jd.com/new/login.aspx?ReturnUrl=https%3A%2F%2Fwww.jd.com%2F',
                     headers=headers, verify=False).text
        uuid = re.findall('name="uuid" value="(.*?)"', html, re.S)[0]
        if 'JD_Verification' in html:
            yys = time.time() * 1000
            url = 'http://authcode.jd.com/verify/image?a=1&acid='+uuid+'&uid='+uuid+'&yys='+str(int(yys))
            print (url)
            ir = t.get(url, headers=headers2,verify=False)
            save_img('C:\\temp\\' + rdname + '.png', ir)
            authcode = fuck_code_rk(self.rk_um, self.rk_pw, 'C:\\temp\\' + rdname + '.png')
        else:
            authcode = ''
        pubkey = re.findall('id="pubKey" value="(.*?)"', html, re.S)[0]


        data = {'uuid': re.findall('name="uuid" value="(.*?)"', html, re.S)[0],
                '_t': re.findall('id="token" value="(.*?)"', html, re.S)[0],
                'loginType': 'c',
                'loginname': self.username,
                'nloginpwd': self.pwd,
                'chkRememberMe': '',
                'authcode': authcode,
                'pubKey': pubkey,
                'sa_token': re.findall('name="sa_token" value="(.*?)"', html, re.S)[0],
                'seqSid': '9'
                }
        post_url="https://passport.jd.com/uc/loginService?uuid="+uuid+"&ReturnUrl=https%3A%2F%2Fwww.jd.com%2F&r=0.6866403083063548&version=2015"
        print (post_url)
        post_data = t.post(
            post_url,
            data=data, headers=headers, verify=False).text
        if 'success' in post_data:
            print(self.username, decoder('PC端登陆成功！'))
        else:
            print(post_data)
            raise Exception('Login Failed！')
        for k, value in t.cookies.items():
            cookiestr = cookiestr + k + '=' + value + ';'
        self.ck_pc = cookiestr[:-1]
        return self.ck_pc

    def get_payment(self):
        payment_list = []
        headers = {'cookie': self.ck_pc}
        html = self.session.get('http://order.jd.com/center/list.action', headers=headers, verify=False).text
        payment = re.findall('<span class="number">(.*?)<div class="operate">', html, re.S)
        for each in payment:
            try:
                print('===================================')
                add = re.findall('<div class="pc">(.*?)</div>', each, re.S)[0]
                sku = re.findall('data-sku="(.*?)"', each, re.S)[0]
                itemname = re.findall('<title>(.*?)</title>',
                                      self.session.get('http://item.jd.com/' + str(sku) + '.html').text, re.S)[0]

                orderid = re.findall('id="track(.*?)"', each, re.S)[0]
                name = re.findall('<strong>(.*?)</strong>', add, re.S)[0]
                address = re.findall('<p>(.*?)</p>', add, re.S)[0]
                phone = re.findall('<p>(.*?)</p>', add, re.S)[1]
                print(itemname)
                print(orderid, name, address, phone)
                print('===================================')
                payment_list.append({'orderID': orderid,
                                     'name': name,
                                     'address': address,
                                     'phone': phone,
                                     'item': itemname,
                                     'sku': sku})
            except:
                pass
        return payment_list

    def get_msglist(self):
        msglist = []
        headers = {'cookie': self.ck_pc}
        html = re.findall('<div class="mg-content clearfix">(.*?)<ul id="msg-node',
                          self.session.get('http://joycenter.jd.com/msgCenter/queryMessage.action', headers=headers,
                                           verify=False).text, re.S)
        for each in html:
            everycoupon = re.findall('<div>(.*?)</div>', each, re.S)[0]
            print(everycoupon)
            msglist.append(everycoupon)
        return msglist

    def get_couponlist(self):
        headers = {'cookie': self.ck_pc}
        couponlist = []
        for x in range(1, 6):
            html = self.session.get('http://quan.jd.com/user_quan.action?couponType=-1&sort=1&page=' + str(x),
                                    headers=headers, verify=False).text
            everycoupon = re.findall('<div class="coupon-item coupon-item(.*?)<div class="op-btns">', html, re.S)
            for each in everycoupon:
                # print each
                label = re.findall('<span class="txt">(.*?)</span>', each, re.S)[0]
                limit = re.findall('<span class="txt">(.*?)</span>', each, re.S)[1]
                couponnum = re.findall('<span class="txt">(.*?)</span>', each, re.S)[2]
                climit = re.findall('<span>(.*?)</span>', each, re.S)[0]
                price = re.findall('<strong>(.*?)</strong>', each, re.S)[0]
                try:
                    price_limit = re.findall(decoder('满') + '(.*?)' + decoder('可用'), each, re.S)[0]
                except:
                    price_limit = price
                couponlist.append({'label': label,
                                   'limit': limit,
                                   'couponnum': couponnum,
                                   'climit': climit,
                                   'price': price,
                                   'price_limit': price_limit})
                print(couponnum, label, limit, climit, decoder('满'), price_limit, decoder('元可用'), price)
        return couponlist

    def write_cookies(self, userid):
        data = []
        if self.ck_pc == '':
            self.login_pc()
        else:
            for each in loadCSVfile('cookies.csv'):
                data.append(each)
            data.append([str(userid), self.ck_pc, self.username, self.pwd, self.ck_pc_browser])
            writeCSVfile('cookies.csv', data)

    def browser(self, url, cookies=None):

        try:
            cookies = cookies.replace('==', '%%')
            cookies = '{\'' + (cookies.replace('=', '\':\'')).replace(';', '\',\'') + '\'}'
            cookies = cookies.replace('%%', '==')
            cookies = eval(str(cookies))
            print(cookies)
            driver = webdriver.PhantomJS()
            driver.get(url)
            driver.delete_all_cookies()
            time.sleep(2)
            for k, value in cookies.items():
                driver.add_cookie(
                    {'domain': '.jd.com',
                     'name': k,
                     'value': value,
                     'path': '/', 'expires': None})
            driver.get('http://club.jd.com')
        except Exception as err:
            print(err)
        return driver

    def comment(self):
        while True:
            html = requests.get('https://club.jd.com/myJdcomments/myJdcomment.action',
                                headers={'Cookie': self.ck_pc}, verify=False).text
            if decoder('没有要评价的订单') in html:
                print(decoder('没有要评价的订单'))
                raise Exception('Error!')
            tbody = re.findall('<tbody>(.*?)</tbody>', html, re.S)
            print(decoder('浏览器加载中，请稍候……'))
            driver = self.browser('http://club.jd.com', cookies=self.ck_pc)
            for each in tbody:
                try:
                    orderid = re.findall('orderid=(.*?)&', each, re.S)[0]
                    print(orderid)
                    itemid = re.findall('<div class="p-img">(.*?)</div>', each, re.S)
                    for each_item in itemid:
                        productId = re.findall('item.jd.com/(.*?)\.html', each_item, re.S)[0]
                        _data = {'orderId': orderid,
                                 'productId': productId,
                                 'score': '5',
                                 'tag': '%5B%5B%2220078%22%2C%22%E8%BF%98%E4%B8%8D%E9%94%99%22%5D%5D',
                                 'saveStatus': '1',
                                 'anonymousFlag': '1',
                                 'content': '%E8%BF%98%E4%B8%8D%E9%94%99%E5%90%A7%E8%BF%98%E4%B8%8D%E9%94%99%E5%90%A7%E8%BF%98%E4%B8%8D%E9%94%99%E5%90%A7%E8%BF%98%E4%B8%8D%E9%94%99%E5%90%A7%E8%BF%98%E4%B8%8D%E9%94%99%E5%90%A7%E8%BF%98%E4%B8%8D%E9%94%99%E5%90%A7'}
                        result = requests.post('https://club.jd.com/myJdcomments/saveProductComment.action',
                                               data=_data,
                                               headers={'Cookie': self.ck_pc,
                                                        'Referer': 'https://club.jd.com/myJdcomments/orderVoucher.action'
                                                                   '?ruleid=' + orderid,
                                                        'Accept': 'application/json, text/javascript, */*; q=0.01',
                                                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                                                                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                                                                      'Chrome/56.0.2924.87 Safari/537.36',
                                                        'Accept-Language': 'zh-CN,zh;q=0.8',
                                                        'Accept-Encoding': 'gzip, deflate, br',
                                                        'X-Requested-With': 'XMLHttpRequest'},
                                               verify=False).text
                        if '"resultCode":"2"' in result:
                            print(decoder('服务评价中……'))
                        else:
                            print(result)

                    driver.get(
                        'http://club.jd.com/myJdcomments/orderVoucher.action?ruleid=' + orderid + '&operation=survey')
                    time.sleep(2)
                    try:
                        for x in range(1, 10):
                            driver.find_element_by_xpath('//*[@id="activityVoucher"]/div[2]/div[1]/div[1]/div[' + str(
                                x) + ']/span[2]/span[5]').click()
                    except Exception as Err:
                        driver.find_element_by_xpath('//*[@id="container"]/div/div/div[2]/div[2]/a').click()
                        time.sleep(2)
                        print(re.findall('<h3 class="tip-title">(.*?)</h3>', driver.page_source, re.S)[0])
                except:
                    pass
            driver.quit()


def set_cookies(c):
    c = str(c).replace("u'", "'")
    c = c.replace(".www", "www")
    c = c.replace("'.jd", "'jd")
    return c


def lottery_login(a, b, c, d, userid):
    a = Account(a, b, c, d)
    a.login_pc()
    a.write_cookies(userid)


def browser(url, cookies=None, cookie_dictionary=None):
    # try:
    if cookies:
        cookies = cookies.replace('==', '%%')
        cookies = '{\'' + (cookies.replace('=', '\':\'')).replace(';', '\',\'') + '\'}'
        cookies = cookies.replace('%%', '==')
        cookies = eval(str(cookies))
        driver = webdriver.Firefox()
        driver.get(url)
        driver.delete_all_cookies()
        time.sleep(5)
        for k, value in cookies.items():
            driver.add_cookie(
                {'domain': '.jd.com',
                 'name': k,
                 'value': value,
                 'path': '/', 'expires': None})
        driver.get(url)
    if cookie_dictionary:
        driver = webdriver.Firefox()
        driver.get(url)
        driver.delete_all_cookies()
        time.sleep(5)
        for item in cookie_dictionary:
            driver.add_cookie(
                {'domain': '.jd.com',
                 'name': item['name'],
                 'value': item['value'],
                 'path': '/', 'expires': None})
        driver.get(url)
