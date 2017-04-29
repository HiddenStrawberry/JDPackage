# encoding=utf-8
from __future__ import print_function
import platform
import csv

version = int(platform.python_version()[0])


def loadCSVfile(file):
    t = []
    try:
        csvfile = open(file, "r")
        read = csv.reader(csvfile)
        for each in read:
            t.append(each)
        return t
    except:
        print('CSV Reader B')
        csvfile = open(file, "r", encoding='utf-8')
        read = csv.reader(csvfile)
        return read


def writeCSVfile(filename, data):
    if version == 3:
        with open(filename, "w", newline="") as datacsv:
            csvwriter = csv.writer(datacsv, dialect="excel")
            for each in data:
                csvwriter.writerow(each)
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
