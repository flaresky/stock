# -*- coding: utf-8 -*-
import time
import settings
import extractor
import utils

def main():
    for page in range(1, 57):
        url = "http://q.10jqka.com.cn/interface/stock/fl/zdf/desc/%d/hsa/quote"%(page)
        utils.print_with_time(url)
        jo = utils.fetch_json(url)
        time.sleep(settings.sleepTime)
        for st in jo['data']:
#             print st['stockcode']
            extractor.extract_code(st['stockcode'])
#         break

if __name__ == '__main__':
    main()