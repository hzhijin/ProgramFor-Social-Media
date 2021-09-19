# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 10:51:45 2021

@author: ThinkPad-X200
"""

import os
import subprocess
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import glob
from selenium import webdriver
from upload_video import upload_video
import time
from zhconv import convert

save_dir = r'C:\D\FunOfComics'


def get_file_from_cmd(url):
	cmd = r'C:\D\aria2\aria2c.exe --seed-time=0 -d '+ save_dir +' -c '+ url

	try:
		p1=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
		print("---start---")
		msg_content = ''
		for line in p1.stdout:
			print(line)
			l = line.decode(encoding="utf-8", errors="ignore")
			msg_content += l
		p1.wait()
		if 'Download Progress Summary' in msg_content:
			print("download by aira2 successfully.")
			return msg_content
		return False
	except Exception as e:
		print(e)
		return False

print('a')
time.sleep(5)

options = webdriver.ChromeOptions() 
options.add_argument("user-data-dir=C:\\Users\\ThinkPad-X200\\AppData\\Local\\Google\\Chrome\\User Data4_comics") #Path to your chrome profile
driver = webdriver.Chrome(chrome_options=options)

for i in tqdm(range(100000)):
	vid = str(1366829 + i)
	url = 'https://nyaa.si/view/' + vid
	print(url)
	
	for j in range(100):
		try:
			r = requests.get(url)
			if r.status_code == 404:
				continue
			else:
				break
		except Exception as e:
			print(e)
		finally:
			print(j)
			time.sleep(10)
	
	sizeText = ''
	try:
		b = BeautifulSoup(r.content,'lxml')
		sizeText = b.findAll('div',{'class':'col-md-5'})[-3].text
	except Exception as e:
		print(e)
		continue
	if 'MiB' not in sizeText:
		continue
	
	if b.findAll('div',{'class':'col-md-5'})[-6].text == '0':
		print(url)
		print('no seeds')
		continue
		
	
	try:
		b.find('a',{'class':'folder'}).text
	except Exception as e:
		print(e)
	
		print('ok')
		
		
		desc = b.find('div',{'id':'torrent-description'}).text
		desc = convert(desc, 'zh-hant')
		desc = desc.replace('<','')
		desc = desc.replace('>','')[:5000]
		url = 'https://nyaa.si/download/'+vid+'.torrent'
		
		msg_content = get_file_from_cmd(url)
	
		fnames = glob.glob(save_dir + '\\*.torrent')
		fname = max(fnames, key=os.path.getctime)[:-8]
		try:
			upload_video(driver,fname,desc)
			print('finished')
			print(url)
			print('finished')
			time.sleep(600)
			os.remove(fname)
		except Exception as e:
			print(e)

