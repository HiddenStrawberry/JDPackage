# encoding=utf-8
from PIL import ImageTk
import random
import requests
import hashlib
import os
from datacontrol import *


def fuck_code_rk(rk_um, rk_pwd, imgLocate):
    try:
        rc = RClient(rk_um, rk_pwd)
        im = open(imgLocate, 'rb').read()
        t=rc.rk_create(im, 3040)['Result']
        print (t)
        return (t)
    except Exception as err:
        print (err)
        raise Exception('Ruokuai Error!')

class RClient(object):
    def __init__(self, username, password):
        self.username = username
        self.password = hashlib.md5(password.encode(encoding='utf-8')).hexdigest()
        self.soft_id = '78829'
        self.soft_key = '30dfb059ce40493ea95af20c778ada7c'
        self.base_params = {
            'username': self.username,
            'password': self.password,
            'softid': '78829',
            'softkey': '30dfb059ce40493ea95af20c778ada7c',
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'Expect': '100-continue',
            'User-Agent': 'ben',
        }

    def rk_create(self, im, im_type, timeout=60):
        """
        im: 图片字节
        im_type: 题目类型
        """
        params = {
            'typeid': im_type,
            'timeout': timeout,
        }
        params.update(self.base_params)
        files = {'image': ('a.jpg', im)}
        r = requests.post('http://api.ruokuai.com/create.json', data=params, files=files, headers=self.headers)
        return r.json()

    def rk_report_error(self, im_id):
        """
        im_id:报错题目的ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://api.ruokuai.com/reporterror.json', data=params, headers=self.headers)
        return r.json()


def rk_webdriver_verify(driver,rc,xpath_text):
    if os.path.isdir('C:\Temp'):
        pass
    else:
        os.mkdir('C:\Temp')
    rdname = str(random.randint(1000000, 10000000))
    driver.maximize_window()
    try:
        driver.save_screenshot('C:\\temp\\' + rdname + '.jpg')
    except:
        raise Exception("请确认C:\Temp目录存在！")
    try:
        imgelement = driver.find_element_by_xpath(xpath_text)
        location = imgelement.location
        size = imgelement.size
        rangle = (
            int(location['x']), int(location['y']),
            int(location['x'] + size['width']),
            int(location['y'] + size['height']))
        frame4 = ImageTk.Image.open('C:\\temp\\' + rdname + '.jpg').crop(rangle)
        frame4.save('C:\\temp\\' + rdname + '.png')
        im = open('C:\\temp\\' + rdname + '.png', 'rb').read()
        print(decoder('开始识别验证码')),
    except:
        raise Exception("请确认您安装了正确的Pillow包!")
    try:
        codex = rc.rk_create(im, 3040)['Result']
    except Exception as err:
        print(err)
        raise Exception("若快验证码识别出错！")
    return codex

