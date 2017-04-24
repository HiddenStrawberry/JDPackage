# encoding=utf-8
from __future__ import print_function
import csv
import platform
from email.mime.text import MIMEText
import smtplib


version = int(platform.python_version()[0])


def loadCSVfile(file_name):
    t = []
    try:
        csv_file = open(file_name, "r")
        read = csv.reader(csv_file)
        for each in read:
            t.append(each)
        return t
    except:
        print('CSV Reader B')
        csv_file = open(file_name, "r", encoding='utf-8')
        read = csv.reader(csv_file)
        return read


def writeCSVfile(filename, data):
    if version == 3:
        with open(filename, "w", newline="") as datacsv:
            csv_writer = csv.writer(datacsv, dialect="excel")
            for each in data:
                csv_writer.writerow(each)
    if version == 2:
        csvfile = file(filename, 'wb')
        writer = csv.writer(csvfile)
        for each in data:
            writer.writerow(each)
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


def emailto(destination, text, subject,SMTPserver,sender,password):
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