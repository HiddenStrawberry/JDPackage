# encoding=utf8
import csv
import platform
from email.mime.text import MIMEText
import smtplib

version = int(platform.python_version()[0])


def loadCSVfile(file_name):
    if version == 3:
        csv_reader=csv.reader(open(file_name,'r',encoding='utf8'))
        return csv_reader
    else:
        try:
            csv_reader = csv.reader(open(file_name))
        except:
            raise Exception('请确认Cookies.csv文件存在！如不存在请复制JDPackage中的Cookies.csv到程序文件目录中！')
        return csv_reader



def writeCSVfile(filename, data):
    if version == 3:
        with open(filename, "w", newline="") as datacsv:
            csv_writer = csv.writer(datacsv, dialect="excel")
            for each in data:
                csv_writer.writerow(each)
    if version == 2:
        csvfile = file(filename, 'wb')
        writer = csv.writer(csvfile)
        writer.writerows(data)
        csvfile.close()
    print('Write to ' + str(filename) + ' Complete!')


def decoder(string):
    if version == 2:
        return string.decode('utf8')
    else:
        return string


def spider_file_csv(lc_dict, filename):
    try:
        s = str(lc_dict)
        f = open(filename, 'w')
        f.writelines(s)
        f.close()
        print('Write to ' + str(filename) + ' Complete!')
    except Exception as Err:
        print(Err)


def emailto(destination, text, subject, SMTPserver, sender, password):
    try:
        msg = MIMEText(text)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = destination
        mailserver = smtplib.SMTP(SMTPserver, 25)
        mailserver.login(sender, password)
        mailserver.sendmail(sender, [destination], msg.as_string())
        mailserver.quit()
        print ('Send to ' + destination + ' Complete!')
    except Exception as err:
        print (err)

def save_img(imgLocate, ir):
    try:
        fp = open(imgLocate, 'wb')
        fp.write(ir.content)
        fp.close()
        return True
    except Exception as Err:
        print (Err)
