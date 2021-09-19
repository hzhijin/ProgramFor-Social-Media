# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 15:53:46 2021

@author: ThinkPad-X200
"""

from selenium import webdriver
import win32gui
import win32con
import time

def upload_video(driver,fname,desc):
	print('ready to upload')
	try:
		driver.get('https://www.youtube.com/upload')
	except Exception as e:
		print(e)
	time.sleep(10)

	for i in range(100):
		
		dialog = win32gui.FindWindow('#32770', 'Open')  # 对话框
		if dialog == 0:
			btn = driver.find_element_by_id('select-files-button')
			
			if btn.is_enabled():
				try:
					btn.click()
				except Exception as e:
					print(e)
					continue
				finally:
					time.sleep(3)
				break
			else:
				time.sleep(3)
		else:
			time.sleep(3)

	time.sleep(10)
	# win32gui
	dialog = win32gui.FindWindow('#32770', 'Open')  # 对话框
	
	
	
	
	ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
	ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
	Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
	button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button
	win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, 'C:\\D\youget\\' + fname)  # 往输入框输入绝对地址
	time.sleep(1)
	win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button
	time.sleep(5)


	for i in range(30):
		btn = driver.find_elements_by_id('textbox')[1]
		if btn.is_enabled():
			try:
				btn.clear()
				btn.send_keys(desc)
			
			except Exception as e:
				print(e)
				continue
			finally:
				time.sleep(3)
			break
		else:
			time.sleep(1)
			
			
	for i in range(30):
		btn = driver.find_elements_by_id('radioLabel')[1]
		if btn.is_enabled():
			try:
				btn.click()
			except Exception as e:
				print(e)
				continue
			finally:
				time.sleep(3)
			break
		else:
			time.sleep(1)

	for i in range(30):
		btn = driver.find_element_by_id('next-button')

		if btn.is_enabled():
			try:
				btn.click()
			except Exception as e:
				print(e)
				continue
			finally:
				time.sleep(3)
			break
		else:
			time.sleep(1)

	for i in range(30):
		btn = driver.find_element_by_id('next-button')

		if btn.is_enabled():
			try:
				btn.click()
			except Exception as e:
				print(e)
				continue
			finally:
				time.sleep(3)
			break
		else:
			time.sleep(1)

	for i in range(30):
		btn = driver.find_element_by_id('next-button')

		if btn.is_enabled():
			try:
				btn.click()
			except Exception as e:
				print(e)
				continue
			finally:
				time.sleep(3)
			break
		else:
			time.sleep(1)


# 	for i in range(30):
# 		btn = driver.find_element_by_id('next-button')

# 		if btn.is_enabled():
# 			try:
# 				btn.click()
# 			except Exception as e:
# 				print(e)
# 				continue
# 			finally:
# 				time.sleep(3)
# 			break
# 		else:
# 			time.sleep(1)


	for i in range(30):
		btn = driver.find_elements_by_id('radioContainer')[3]

		if btn.is_enabled():
			try:
				btn.click()
			except Exception as e:
				print(e)
				continue
			finally:
				time.sleep(3)
			break
		else:
			time.sleep(1)

	for i in range(30):
		btn = driver.find_element_by_id('done-button')

		if btn.is_enabled():
			try:
				btn.click()
			except Exception as e:
				print(e)
				continue
			finally:
				time.sleep(3)
			break
		else:
			time.sleep(1)

	for i in range(30):
		try:
			title = driver.find_element_by_id('dialog-title').text
			print(title)
			break
		except Exception as e:
			time.sleep(1)

if __name__ == '__main__':
	fp = webdriver.FirefoxProfile(r'C:\Users\ThinkPad-X200\AppData\Roaming\Mozilla\Firefox\Profiles\45xxuc4l.default-release')
	driver = webdriver.Firefox(fp)
	
	fname = '郑恺苗苗庆祝女儿百天'
	upload_video(driver,fname)


