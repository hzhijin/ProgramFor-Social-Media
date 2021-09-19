# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 15:35:27 2021

@author: ThinkPad-X200
"""

import MetaTrader5 as mt5
import pandas as pd
import time
import datetime as dt

from get_data import mql5_login,get_position

pd.options.display.max_columns=50

columns = ['ticket','time','time_msc','time_update','time_update_msc',
		   'type','magic','identifier','reason','volume',
		   'price_open','sl','tp','price_current','swap',
		   'profit','symbol','comment','external_id']

columns_h = ['ticket','order','time','time_msc','type','entry',
			 'magic','position_id','reason','volume','price','commission',
			 'swap','profit','fee','symbol','comment','external_id']

mt5.initialize('C:\\Program Files\\MetaTrader 5\\terminal64.exe',login=43138350,password='a1muoxik')
positions=mt5.positions_get()
df1 = pd.DataFrame(positions,columns=columns)
h1=mt5.history_deals_get(dt.datetime.now() - dt.timedelta(days=365),dt.datetime.now() + dt.timedelta(days=365))
dfh1 = pd.DataFrame(h1,columns=columns_h)

deviation = 20

user = '5089368'
pw = '523240'
url = 'https://www.mql5.com/en/signals/798802'
cookieStr = mql5_login(user = user,pw = pw)
	
	
df,dfh = get_position(url,cookieStr)


