# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
from os import listdir
from os.path import isfile
import matplotlib.pyplot as plt

files = listdir('/home/yuchen/Documents/learn-stock/data/')

industry_type = '02'
column_name = ['type','date','證券代號','證券名稱','成交股數','成交筆數','成交金額','開盤價','最高價','最低價','收盤價',
 '漲跌(+/-)','漲跌價差','最後揭示買價', '最後揭示買量', '最後揭示賣價', '最後揭示賣量','本益比']

mounth_data = pd.DataFrame(columns = column_name)


def fn_float(x):
    if x and x != '--':
        return float(x.replace(',', ''))
    else:
        return None
    
def fn_int(x):
    if x and x != '--':
        return int(x.replace(',', ''))
    else:
        return None

# for date in (20200601,):

for f_name in files:
    # with open('/home/yuchen/Documents/learn-stock/data/{}.csv'.format(date), encoding='big5') as f:
    file_path  = '/home/yuchen/Documents/learn-stock/data/{}'.format(f_name)
    if isfile(file_path):
        with open(file_path, encoding='big5') as f:
            line_text = f.read().split('\n')
        
        date = f_name.replace('.csv', '')
        
        title, unit = line_text[0], line_text[1]
        column_name = [i.replace('"','') for i in line_text[2].split('",') if i != '']
        
        data = []
        
        for line in line_text[3:]:
                tmp = [i.replace('"','') for i in line.split('",') if i != '']
                if len(tmp) == len(column_name):
                    tmp = [tmp[0], tmp[1], *map(fn_int, tmp[2:5]), *map(fn_float, tmp[5:9]), tmp[9], *map(fn_float, tmp[10:])]
                    data.append(tmp)
                
        df = pd.DataFrame(data, columns = column_name)
        df['type'] = industry_type
        df['date'] = date
        mounth_data = pd.concat([mounth_data,df])


group = mounth_data.groupby(by = '證券代號')
code_1201 = group.get_group('1201')
code_1201 = code_1201.sort_values(by = 'date')

fig = plt.Figure()
plt.plot(np.arange(0,len(code_1201)),code_1201['收盤價'].rolling(5).mean())
plt.plot(np.arange(0,len(code_1201)),code_1201['收盤價'].rolling(20).mean())
plt.plot(np.arange(0,len(code_1201)),code_1201['收盤價'].rolling(60).mean())
