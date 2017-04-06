Docs For ROOKIE
===============


----------


这个教程是为无Python或者Python基础较为薄弱的人准备的，如果你拥有一定Python基础，请忽略这部分。

1.安装
----
你需要安装如下几个模块：
1. Python 2.7 32位
>官网下载地址：
>https://www.python.org/ftp/python/2.7/python-2.7.msi
>您也可以通过其他渠道下载

2. 由HiddenStrawberry打包好了的LIB库Windows自解压安装包：
>下载地址：
>http://pan.baidu.com/s/1c27pL3E
>安装方式:
>请直接打开并安装到Python目录中（如安装Python时未更改安装目录则无需更改直接点击安装目录即可）

2.部署
----
1. 下载JDPackage
>地址：
>https://github.com/HiddenStrawberry/JDPackage
>点击页面中的 Clone or Download 然后点击Download ZIP



2. 将压缩包解压放到一个目录中，将文件夹名称改名为JDPackage
3. 在开始菜单中打开Python 2.7文件夹中的IDLE，点击File-New Window
4. 在新窗口中点击File-Save，保存到**JDPackage的上级目录**（如JDPackage位置是C:\JDPackage，那么将这个文件保存到C:\即可
5. 在这个文件中书写代码即可

3.使用
----
详细的各模块文件教程文档：
>https://github.com/HiddenStrawberry/JDPackage/tree/master/docs
点击各文件名即是各个模块的使用教程。只需在刚才新建的文件中使用函数即可。

4.例子
----
抽奖小例子：

hello.py

    from JDPackage import *

    login('1','15840000000','123456') #登陆京东账号，设定userid为1，并将cookies存入cookies文件(注意：登录只需要一次，除非cookies失效)

    get_iplist('ip.csv',3,'inha') #获取3页免费代理IP

    filter_iplist('ip.csv', 'new.csv', 2) #过滤出延迟在2秒以内的IP地址并保存为new.csv

    cookielist=loadCSVfile('cookies.csv') #加载Cookies文件

    proxylist=loadCSVfile('new.csv') #加载代理地址文件new.csv

    add_lottery('1','4b6c385f-a626-48d2-8abe-f2ce2ebe5d5f','2017-03-08 20:57:30',5,cookielist,proxylist)
    #这段代码的含义是，在2017-03-08 20:57:30时使用所有userid为1的账号对抽奖代码为4b6c385f-a626-48d2-8abe-f2ce2ebe5d5f进行抽奖，每个账号间隔5秒进行抽取，每个账号换一个IP

