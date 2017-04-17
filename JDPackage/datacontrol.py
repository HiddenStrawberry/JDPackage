#encoding=utf-8
import csv
def loadCSVfile(file):
    try:
        csv_reader = csv.reader(open(file))
    except:
        raise Exception('请确认Cookies.csv文件存在！如不存在请复制JDPackage中的Cookies.csv到程序文件目录中！')
    return csv_reader
def spider_file_csv(lc_dict,filename):
    try:
        s = str(lc_dict)
        f = file(filename, 'w')
        f.writelines(s)
        f.close()
        print 'Write to ' + str(filename) +' Complete!'
    except Exception as Err:
        print Err

