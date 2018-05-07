import os
import datetime
from dateutil.parser import parse

def convertDate(input_date,input_format,output_format):
    return datetime.datetime.strptime(input_date, input_format).strftime(output_format)

    dt = parse('31 08 2011')
    print(dt)
    # datetime.datetime(2010, 2, 15, 0, 0)
    print(dt.strftime('%Y/%m/%d'))
    # 15/02/2010


output_date= convertDate('12/17/2017','%m/%d/%Y','%m %d,%Y')
print output_date





