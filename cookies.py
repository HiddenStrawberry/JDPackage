#encoding=utf-8

import time
from selenium.webdriver.common.keys import Keys
import csv
from Tkinter import *
from PIL import ImageTk
#1
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36 Core/1.47.163.400 QQBrowser/9.3.7175.400"
)
stdi,stdo,stde=sys.stdin,sys.stdout,sys.stderr
reload(sys)
sys.setdefaultencoding('utf-8',)
sys.stdin,sys.stdout,sys.stderr=stdi,stdo,stde
codex=''
def loadCSVfile(file):
    csv_reader = csv.reader(open(file))
    return csv_reader
def verifycode(filename):
    global top
    global code
    top = Tk()
    label = Label(top, image=ImageTk.PhotoImage(file=filename))
    label.pack()
    l1 = Label(top, text="请输入验证码：")
    l1.pack()
    code = StringVar()
    code_text = Entry(top, textvariable = code)
    code.set("")
    code_text.pack()
    Button(top, text="确定", command=a).pack()
    top.mainloop()

    # 进入消息循环
def a():
    global codex
    global code
    codex=code.get()
    top.destroy()
def errCheck(html):
    if '账户名与密码不匹配' in html:
        raise Exception('账号名或密码错误!')
    if '账户名与密码不匹配' in html:
        raise Exception('账号名或密码错误!')
    if '安全原因' in html:
        raise Exception('账号被封锁!')
    if '账户名不存在' in html:
        raise Exception('账户名不存在!')
def login(userid,loginname,password):
    global codex
    data=[]
    driver = webdriver.PhantomJS()
    url = 'https://passport.jd.com/uc/login?ltype=logout'
    driver.get(url)
    driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div[2]/a').click()
    driver.find_element_by_id("loginname").send_keys(loginname)
    driver.find_element_by_id("nloginpwd").send_keys(password)
    driver.find_element_by_id("loginsubmit").send_keys(Keys.ENTER)
    time.sleep(2)
    hm=driver.page_source
    errCheck(hm)
    if 'JD_Verification' in hm:
        driver.maximize_window()
        driver.save_screenshot('temp.png')
        imgelement = driver.find_element_by_xpath('//*[@id="JD_Verification1"]')
        location = imgelement.location
        size=imgelement.size
        rangle=(int(location['x']),int(location['y']),int(location['x']+size['width']),int(location['y']+size['height']))
        frame4=ImageTk.Image.open("temp.png").crop(rangle)
        frame4.save('temp1.png')
        print '需要输入验证码！请在新窗口中输入验证码！'
        verifycode('temp1.png')
        print codex
        driver.find_element_by_id("authcode").send_keys(codex)
        driver.find_element_by_id("loginsubmit").send_keys(Keys.ENTER)
        time.sleep(2)
        hm = driver.page_source
        errCheck(hm)
    t=driver.get_cookies()
    t=str(t).replace("u'","'")
    t = str(t).replace(".www", "www")
    t = str(t).replace("'.jd", "'jd")
    enable=0
    while enable==0:
        if "京东(JD.COM)" in driver.title:
            cookiestr = ';'.join(item for item in [item["name"] + "=" + item["value"] for item in driver.get_cookies()])
            driver.quit()
            enable=1
            print '登陆成功！'
    for each in loadCSVfile('cookies.csv'):
        data.append(each)
    data.append([userid,cookiestr,loginname,password,t])
    csvfile = file('cookies.csv', 'wb')
    writer = csv.writer(csvfile)
    writer.writerows(data)
    csvfile.close()
if __name__ == "__main__":
    login('1','123456','123456')

