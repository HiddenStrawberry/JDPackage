#encoding=utf-8
from JDPackage import *

browser('url',cookies='')
#目前仅支持Firefox 47.0以下的版本!请先安装一个Firefox

#此功能为高级功能,目前稳定性暂时比较差,如失败请重试
#如果是Fiddler之类抓的Cookies,参数写成cookies='xxx(cookies内容)'即可
#如果有cookies字典，参数写成cookie_dictionary=xxx即可。
