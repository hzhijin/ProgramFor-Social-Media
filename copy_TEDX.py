# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 10:49:46 2021

@author: ThinkPad-X200
"""


import youtube_dl
from youtube_dl.utils import DateRange
import pandas as pd
from selenium import webdriver
import time
import win32gui,win32con
from selenium.webdriver.common.keys import Keys
import glob
import os


def upload_bilibili(fname,title,desc):
	
	options = webdriver.ChromeOptions() 
	options.add_argument("user-data-dir=C:\\Users\\ThinkPad-X200\\AppData\\Local\\Google\\Chrome\\User Data3") #Path to your chrome profile
# 	driver = webdriver.Chrome(chrome_options=options)
	driver = webdriver.Chrome(options=options)


	# windows = driver.window_handles
	# driver.switch_to.window(windows[0])

	url2 = 'https://member.bilibili.com/platform/upload/video/frame'

	try:
		driver.get('https://member.bilibili.com')
	except Exception as e:
		print(e)
	time.sleep(10)
		
	try:
		driver.get(url2)
	except Exception as e:
		print(e)
	time.sleep(10)
		
		
	for i in range(100):
		try:
			driver.switch_to.frame('videoUpload')
			
			break
		except Exception as e:
			print(e)
		finally:
			time.sleep(3)
	
	for i in range(100):
		time.sleep(3)
		dialog = win32gui.FindWindow('#32770', 'Open')  # 对话框
		if dialog == 0:
			driver.find_element_by_id('bili-upload-btn').click()
			break
		else:
			pass
	
	time.sleep(10)
	# win32gui
	dialog = win32gui.FindWindow('#32770', 'Open')  # 对话框
	
	ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
	ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
	Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
	button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button
	win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, fname)  # 往输入框输入绝对地址
	time.sleep(1)
	win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button
	time.sleep(5)
	
	driver.find_elements_by_class_name('check-radio-v2-container')[1].click()
	
	driver.find_elements_by_class_name('input-box-v2-1-val')[0].click()
	driver.find_elements_by_class_name('input-box-v2-1-val')[0].send_keys(Keys.BACKSPACE*500)
	driver.find_elements_by_class_name('input-box-v2-1-val')[0].send_keys(Keys.DELETE*500)
	driver.find_elements_by_class_name('input-box-v2-1-val')[0].send_keys('https://www.ted.com/tedx')
	
	driver.find_elements_by_class_name('input-box-v2-1-val')[1].click()
	driver.find_elements_by_class_name('input-box-v2-1-val')[1].send_keys(Keys.BACKSPACE*500)
	driver.find_elements_by_class_name('input-box-v2-1-val')[1].send_keys(Keys.DELETE*500)
	driver.find_elements_by_class_name('input-box-v2-1-val')[1].send_keys(title)
	
	driver.find_elements_by_class_name('label-item-v2-2-container')[2].click()
	driver.find_elements_by_class_name('label-item-v2-2-container')[5].click()
	driver.find_elements_by_class_name('label-item-v2-2-container')[6].click()
	
# 	driver.find_element_by_class_name('text-area-box-v2-container').click()
	driver.find_element_by_class_name('content-desc-v2-text-wrp').click()
	
	
# 	driver.find_element_by_xpath('//div[@class="ql-editor"]').send_keys(Keys.BACKSPACE*5000)
# 	driver.find_element_by_xpath('//div[@class="ql-editor"]').send_keys(Keys.DELETE*5000)

	driver.find_element_by_xpath('//div[@class="ql-editor ql-blank"]').send_keys(desc[:250])

# 	driver.find_element_by_class_name('text-area-box-v2-val').send_keys(Keys.BACKSPACE*5000)
# 	driver.find_element_by_class_name('text-area-box-v2-val').send_keys(Keys.DELETE*5000)
# 	driver.find_element_by_class_name('text-area-box-v2-val').send_keys(desc[:250])
	
	time.sleep(5)
	
	driver.find_element_by_class_name('submit-btn-group-add').click()
	
	time.sleep(14400)
	driver.quit()
	
	return True


# print('a')
# time.sleep(5)



while True:
	
	url1 = 'https://youtube.com/user/TEDxTalks'
	
	ydl_opts = {
	    'format': 'bestaudio/best',   
		 'download_archive': 'C:\\D\\TEDx\\download_archive',
		 'Download':False,
		 }
	
	try:
		with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		    ydl.download([url1])
	except Exception as e:
		print(e)
		
		
	
	
	with open(r'C:\D\TEDx\download_archive','r') as f:
		data = f.read().split('\n')
	df = pd.DataFrame(data,columns = ['url'])
	df['url'] = df.url.str[8:]
	
	with open(r'C:\D\TEDx\upload_archive','r') as f:
		data = f.read().split('\n')
	dfu = pd.DataFrame(data,columns = ['url'])
	
	df = df[~df.url.isin(dfu.url)]
	
	
	for i in range(len(df)):
		
	
		try:
			vid = df.iloc[i]['url']
			url = 'https://youtu.be/' + vid
			ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})
			with ydl:
			    result = ydl.extract_info(url)
				
				
			fname = glob.glob('C:\\D\\TEDx\\' + vid+'.*')[0]
	
			title = result['title']
			desc = result['description']
			
		
			upload_bilibili(fname,title,desc)
			
			os.remove(fname)
			with open('C:\\D\\TEDx\\upload_archive','a+') as f:
				f.write(vid+'\n')
		except Exception as e:
			print(e)
		finally:
			time.sleep(120)




