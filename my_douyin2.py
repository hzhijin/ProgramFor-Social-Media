import requests
import pandas as pd
from gorylla import *
from tqdm import *
import hashlib
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.io.VideoFileClip import VideoFileClip
import moviepy.video.fx.all as vfx


from selenium import webdriver
from upload_video import upload_video
import os,re

from youdao import youdao_trans
from translate import Translator
from zhconv import convert

def get_file_md5(file_path):
	with open(file_path, 'rb') as file:
		md5_obj = hashlib.md5()
		while True:
			buffer = file.read(8096)
			if not buffer:
				break
			md5_obj.update(buffer)
		hash_code = md5_obj.hexdigest()
	md5 = str(hash_code).lower()
	return md5

def modify_file_md5(file_path):
	with open(file_path, 'a') as file:
		file.write("####&&&&")

def handle_frame(image_frame):
	image_frame_result = image_frame * 1.1
	image_frame_result[image_frame_result > 255] = 255
	return image_frame_result
def increase_video_brightness(file_path):
	video = VideoFileClip(file_path)
	result = video.fl_image(handle_frame)
	result.write_videofile("new.mp4")
	os.remove(file_path)
	os.rename("new.mp4",file_path)



options = webdriver.ChromeOptions() 
options.add_argument("user-data-dir=C:\\Users\\ThinkPad-X200\\AppData\\Local\\Google\\Chrome\\User Data2") #Path to your chrome profile
driver = webdriver.Chrome(chrome_options=options)
# driver.set_window_position(1500,0)
time.sleep(10)
while True:
	
	strq = 'SELECT aid,flag FROM douyin;'
	dfu = sql_to_df('videos', strq)
	df = pd.read_excel(r'C:\D\youget\douyin_list_inform.xlsx')
	for i in tqdm(range(len(df))):
		n = df.iloc[i]['name']
		u = df.iloc[i]['url']
		
		try:
			r = requests.get(u,timeout=30).json()
			d = r['aweme_list'][0]['desc']
		except Exception as e:
			print(e)
			continue


		
		de = ''
		try:
			de = youdao_trans(d)
		except Exception as e:
			print(e)
			
			try:
				translator= Translator(from_lang="zh",to_lang="en")
				de = translator.translate(d)
				print(de)
				if 'MYMEMORY WARNING: YOU USED ALL AVAILABLE FREE TRANSLATIONS FOR TODAY' in de:
					de = ''
			except Exception as e:
				print(e)
		
		d = convert(d, 'zh-hant')
		print(d)
		d = re.sub('[?*:"<>\/|]','',d + de)[:240]


			
			
		aid = r['aweme_list'][0]['aweme_id']
		
		if aid in dfu.aid.tolist():
			continue
		print(d,aid)
	
		u = r['aweme_list'][0]['video']['play_addr']['url_list'][0]
		
		try:
			r = requests.get(u,timeout=30)
		except Exception as e:
			print(e)
			continue
		
		file_path = d +'.mp4'
		with open('C:\\D\\youget\\' + file_path,'wb') as f:
			f.write(r.content)
		modify_file_md5(file_path)
# 		try:
# 			increase_video_brightness(file_path)
# 		except Exception as e:
# 			print(e)
		
		desc = '古书经典《金瓶梅》https://www.amazon.com/dp/B092H5MGZH'
		desc = '微信: QQQLIBOYANG     LINE: kxykfuntime'
		
		try:
			upload_video(driver,file_path,desc)
		except Exception as e:
			continue
		dft = pd.DataFrame([(aid,'n','d',1)],columns = ['aid','n','desc','flag'])
		df_to_sql('videos', 'douyin', dft)

	time.sleep(10)
	











