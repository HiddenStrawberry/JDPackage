#encoding=utf-8
import requests
import hashlib


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

