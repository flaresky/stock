import urllib2
import datetime
import argparse

month_str_map = {
                 1 : 'Jan',
                 2 : 'Feb',
                 3 : 'Mar',
                 4 : 'Apr',
                 5 : 'May',
                 6 : 'Jun',
                 7 : 'Jul',
                 8 : 'Aug',
                 9 : 'Sep',
                 10 : 'Oct',
                 11 : 'Nov',
                 12 : 'Dec',
                 }

def getReport(datestr):
    url = 'http://sc.hangseng.com/gb/www.hsi.com.hk/HSI-Net/static/revamp/contents/en/indexes/report/hsi/idx_%s.csv'%(datestr)
    response = urllib2.urlopen(url)
    data = response.read()
    print data.decode("utf-16")

def getDateStr(datestr=None):
    if datestr is None:
        today = datetime.datetime.today()
        year = today.year % 100
        month = month_str_map[today.month]
        day = today.day
    else:
        year = int(datestr[:2])
        month = month_str_map[int(datestr[2:4])]
        day = int(datestr[4:])
    return "%d%s%d"%(day, month, year)

def main():
    parser = argparse.ArgumentParser(description='hscei extractor')
    parser.add_argument('-d', '--date', type=str, required=False, help='date')
    res = parser.parse_args()
    ds = getDateStr(res.date)
    print "get report by %s"%(ds)
    getReport(ds)

if __name__ == '__main__':
    main()