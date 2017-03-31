import csv
def loadCSVfile(file):
    csv_reader = csv.reader(open(file))
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

