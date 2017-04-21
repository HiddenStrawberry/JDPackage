# encoding=utf-8
from __future__ import print_function
from .rk import *
from .datacontrol import *
import time
from PIL import ImageTk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import random


class Account:
    def __init__(self, username, pwd, rk_um, rk_pw):
        self.username = username
        self.pwd = pwd
        self.rc = RClient(rk_um, rk_pw)
        self.ck = ''
        self.ck_pc = ''
        self.ck_browser = ''
        self.ck_pc_browser = ''
        self.session = requests.session()

    def login(self):
        rdname = str(random.randint(1000000, 10000000))
        driver = webdriver.PhantomJS()
        url = "https://plogin.m.jd.com/user/login.action?appid=100&kpkey=&returnurl=http%3A%2F%2Fm.jd.com%3Findexloc" \
              "%3D1%26sid%3D9129920d9c239d7273eed31ddcc2a0ab "
        driver.get(url)
        enabled = 0
        while decoder('专业网上购物平台品质保障') not in driver.title and enabled == 0:
            driver.find_element_by_id("username").send_keys(self.username)
            driver.find_element_by_id("password").send_keys(self.pwd)
            driver.maximize_window()
            verify = False
            while not verify:
                try:
                    driver.save_screenshot('C:\\temp\\' + rdname + '.jpg')
                except:
                    raise Exception("请确认C:\Temp目录存在！")
                try:
                    imgelement = driver.find_element_by_xpath('//*[@id="imgCode"]')
                    location = imgelement.location
                    size = imgelement.size
                    rangle = (
                        int(location['x']), int(location['y']),
                        int(location['x'] + size['width']),
                        int(location['y'] + size['height']))
                    frame4 = ImageTk.Image.open('C:\\temp\\' + rdname + '.jpg').crop(rangle)
                    frame4.save('C:\\temp\\' + rdname + '.png')
                    im = open('C:\\temp\\' + rdname + '.png', 'rb').read()
                    print(decoder('开始识别验证码'), end='')
                except:
                    raise Exception("请确认您安装了正确的Image包")
                try:
                    codex = self.rc.rk_create(im, 3040)['Result']
                except Exception as err:
                    print(err)
                    raise Exception("若快验证码识别出错！")
                print(codex)
                print(decoder('->识别成功'), end='')
                driver.find_element_by_id("code").send_keys(codex)
                driver.find_element_by_xpath('//*[@id="loginBtn"]').send_keys(Keys.ENTER)
                print(decoder('->登陆中……'), end='')
                time.sleep(2)

                if decoder('图片验证码错误，请重试') in driver.page_source:
                    verify = False
                elif decoder('账号或密码不正确') in driver.page_source:
                    driver.quit()
                    raise Exception('账号或密码不正确')
                else:
                    verify = True

                while 1 == 1 and verify == True and enabled == 0:
                    while decoder('专业网上购物平台品质保障') in re.findall('<title>(.*?)</title>', driver.page_source, re.S)[
                        0] and enabled == 0:
                        # print '->请稍后……',
                        cookie = [item["name"] + "=" + item["value"] for item in driver.get_cookies()]
                        self.ck = ';'.join(item for item in cookie)
                        print(self.username, decoder('->M端登陆成功！'))
                        enabled = 1
                        self.ck_browser = set_cookies(driver.get_cookies())
        driver.quit()

    def login_pc(self):
        rand_name = str(random.randint(1000000, 10000000))
        driver = webdriver.PhantomJS()
        url = 'https://passport.jd.com/uc/login?ltype=logout'
        driver.get(url)
        print(decoder('开始登陆……'))
        driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div[2]/a').click()
        driver.find_element_by_id("loginname").send_keys(self.username)
        driver.find_element_by_id("nloginpwd").send_keys(self.pwd)
        driver.find_element_by_id("loginsubmit").send_keys(Keys.ENTER)
        time.sleep(5)
        hm = driver.page_source
        errmsg = ['账户名与密码不匹配', '账户名与密码不匹配', '安全原因', '账户名不存在']

        for each in errmsg:
            if decoder(each) in hm:
                driver.quit()
                raise Exception(each)

        if 'JD_Verification' in hm:
            driver.maximize_window()
            driver.save_screenshot('C:\\temp\\' + rand_name + '.jpg')
            try:
                imgelement = driver.find_element_by_xpath('//*[@id="JD_Verification1"]')
                location = imgelement.location
                size = imgelement.size
                rangle = (int(location['x']), int(location['y']), int(location['x'] + size['width']),
                          int(location['y'] + size['height']))
                frame4 = ImageTk.Image.open('C:\\temp\\' + rand_name + '.jpg').crop(rangle)
                frame4.save('C:\\temp\\' + rand_name + '.png')
                im = open('C:\\temp\\' + rand_name + '.png', 'rb').read()
                print(decoder('开始识别验证码'))
            except Exception as err:
                print(err)
                raise Exception("请确认您安装了正确的Image包！")
            try:
                codex = self.rc.rk_create(im, 3040)['Result']
                print(decoder('识别成功！'), codex)
            except Exception as err:
                print(err)
                raise Exception("若快验证码识别出错！")
            driver.find_element_by_id("authcode").send_keys(codex)
            driver.find_element_by_id("loginsubmit").send_keys(Keys.ENTER)
            time.sleep(2)

        enable = 0
        while enable == 0:
            if decoder("京东(JD.COM)") in driver.title:
                self.ck_pc = ';'.join(
                    item for item in [item["name"] + "=" + item["value"] for item in driver.get_cookies()])
                enable = 1
                self.ck_pc_browser = set_cookies(driver.get_cookies())
                driver.quit()
                print(self.username, decoder('PC端登陆成功！'))

    def get_payment(self):
        payment_list = []
        headers = {'cookie': self.ck_pc}
        html = self.session.get('http://order.jd.com/center/list.action', headers=headers, verify=False).text
        payment = re.findall('<span class="number">(.*?)<div class="operate">', html, re.S)
        for each in payment:
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

    def browser(self, cookies=None):
        try:
            cookies = '{\'' + (cookies.replace('=', '\':\'')).replace(';', '\',\'') + '\'}'
            cookies = eval(str(cookies))
            driver = webdriver.PhantomJS()
            driver.get('http://www.jd.com')
            driver.delete_all_cookies()
            time.sleep(5)
            for k, value in cookies.items():
                driver.add_cookie(
                    {'domain': '.jd.com',
                     'name': k,
                     'value': value,
                     'path': '/', 'expires': None})
            driver.get('http://www.jd.com')
        except:
            print(decoder('载入Cookies出错！由于本功能尚处试验阶段，较不稳定，请重新运行！'))
        return driver

    def comment(self):
        while True:
            html = requests.get('https://club.jd.com/myJdcomments/myJdcomment.action',
                                headers={'Cookie': self.ck_pc}, verify=False).text
            if decoder('没有要评价的订单') in html:
                raise Exception('没有要评价的订单')
            tbody = re.findall('<tbody>(.*?)</tbody>', html, re.S)
            print(decoder('浏览器加载中，请稍候……'))
            driver = self.browser(cookies=self.ck_pc)
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
                                 'tag': '%5B%5B%22732%22%2C%22%E4%BC%A0%E8%BE%93%E9%80%9F%E5%BA%A6%E5%BF%AB%22%5D%5D',
                                 'saveStatus': '1',
                                 'anonymousFlag': '1',
                                 'content': '商品还不错！商品还不错！会推荐'}
                        print(requests.post('https://club.jd.com/myJdcomments/saveProductComment.action',
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
                                            verify=False).text)
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
                except:pass
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


def browser(cookies=None, cookie_dictionary=None):
    try:
        if cookies:
            cookies = '{\'' + (cookies.replace('=', '\':\'')).replace(';', '\',\'') + '\'}'
            cookies = eval(str(cookies))
            driver = webdriver.Firefox()
            driver.get('http://www.jd.com')
            driver.delete_all_cookies()
            time.sleep(5)
            for k, value in cookies.items():
                driver.add_cookie(
                    {'domain': '.jd.com',
                     'name': k,
                     'value': value,
                     'path': '/', 'expires': None})
            driver.get('http://www.jd.com')
        if cookie_dictionary:
            driver = webdriver.Firefox()
            driver.get('http://www.jd.com')
            driver.delete_all_cookies()
            time.sleep(5)
            for item in cookie_dictionary:
                driver.add_cookie(
                    {'domain': '.jd.com',  # 注意baidu.com前的英文句号！
                     'name': item['name'],
                     'value': item['value'],
                     'path': '/', 'expires': None})
            driver.get('http://www.jd.com')
    except:
        print(decoder('载入Cookies出错！由于本功能尚处试验阶段，较不稳定，请重新运行！请确定您已经安装了Firefox 47.0以下的版本！'))
    return driver


if __name__ == '__main__':
    a = Account('#', '#', '#', '#')
    a.login_pc()
    a.get_couponlist()  # 获取优惠券列表
    a.get_msglist()  # 获取消息列表
    a.get_payment()  # 获取订单列表
