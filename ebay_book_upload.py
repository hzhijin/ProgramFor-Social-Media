

from selenium import webdriver
import win32gui,win32con
import time

# options = webdriver.ChromeOptions() 
# options.add_argument("user-data-dir=C:\\Users\\ThinkPad-X200\\AppData\\Local\\Google\\Chrome\\User Data") #Path to your chrome profile
# driver = webdriver.Chrome(chrome_options=options)


try:
	driver.get('https://www.ebay.com/sl/prelist/suggest')
except Exception as e:
	print(e)
time.sleep(2)

ISBN = '978' + '0' + '7783' + '25352'
ISBN = '0373' + '48352X'
ISBN = '1' +'59337' + '4968'
ISBN = '978' +'0' + '947183' + '226'
ISBN = '978' +'0' + '06' + '0598754'
ISBN = '978' +'1' + '4201' + '08866'
ISBN = '0' +'345'+ '48026' + '0'
ISBN = '0' +'451'+ '219791' + ''
ISBN = '978' + '0' + '345' + '542281'
ISBN = '0' +'8217'+ '78803' + ''

ISBN = '0' +'515'+ '12317X' + ''
ISBN = '0' +'553'+ '584863' + ''
ISBN = '978' +'0' + '373' + '775569'
ISBN = '0' +'812'+ '590449' + ''
ISBN = '0' +'373'+ '484631' + ''

ISBN = '978' +'0' + '373' + '285372'
ISBN = '978' + '0' + '446' + '612708'
ISBN = '978' +'0' + '06' + '2429070'
ISBN = '978' +'1' + '4555' + '24150'
ISBN = '978' +'0' + '7611' + '46810'

ISBN = '978' +'0' + '345' + '519467'
ISBN = '978' +'1' + '5011' + '50982'


ISBN = '07783' + '20480'


ISBN = '1' + '59486' + '4705'


ISBN = '978' + '1' + '4165' + '60227'
ISBN = '0' + '06' + '1099732'


ISBN = '1' + '4000' + '32717'

ISBN = '978' + '0' + '8010' + '65989'
ISBN = '0' +'1420' + '04855'
ISBN = '0765303337'


info_input = driver.find_element_by_id('s0-0-0-30-13-keyword-box-input-textbox')
info_input.clear()
info_input.send_keys(ISBN)
time.sleep(2)
driver.find_element_by_xpath("//button[@class='keyword-suggestion__button btn btn--primary']").click()
time.sleep(5)
driver.find_element_by_xpath("//div[@class='product__image-container']").click()
time.sleep(2)
driver.find_element_by_xpath("//input[@value='2750']").click()
time.sleep(2)
driver.find_element_by_xpath("//button[@class='textual-display btn btn--primary prelist__next-action']").click()
time.sleep(7)


driver.find_element_by_id('wc0-w0-LIST_PAGE_WRAPPER__-PRICE_VIEW__-RECOMMENDATION_HEADER__-priceViewSelection__-w0').click()
time.sleep(5)
driver.find_element_by_id('wc0-w0-LIST_PAGE_WRAPPER__-PRICE_VIEW__-PRICE_DETAIL_VIEW__-w0-auctionDiyPriceGroup__-auctionSelection__-checkbox').click()
time.sleep(12)
driver.find_element_by_id('wc0-w0-LIST_PAGE_WRAPPER__-PRICE_VIEW__-PRICE_DETAIL_VIEW__-easyPriceSelection__').click()
time.sleep(7)


driver.find_element_by_id('wc0-w0-LIST_PAGE_WRAPPER__-SHIP_VIEW__-SHIP_GRID_VIEW_PRIMARY__-SHIP_DIY_SERVICES_GROUP__-SHIP_PRIMARY_SERVICES_COST__-w0-SHIP_SERVICE_RECO__-shippingRecommendedCostInfo__').click()
time.sleep(5)
local_btn = driver.find_element_by_id('wc0-w0-LIST_PAGE_WRAPPER__-SHIP_VIEW__-localPickup__-w0').click()
time.sleep(3)
inter_btn = driver.find_element_by_id('wc0-w0-LIST_PAGE_WRAPPER__-SHIP_VIEW__-shippingMoreOptions__-w0').click()
time.sleep(3)
iship_btn = driver.find_element_by_id('wc0-w0-LIST_PAGE_WRAPPER__-SHIP_VIEW__-shippingMoreOptions__-SHIP_GRID_VIEW_INTL__-shippingIntlServiceSelectService__').click()
time.sleep(5)
i1_btn = driver.find_element_by_id('wc0-w0-LIST_PAGE_WRAPPER__-SHIPPING_INTL_SERVICE_OVERLAY__-shippingIntlServiceDetails__-0-w1-w0-w0').click()
time.sleep(3)

# save_btn = driver.find_element_by_id('wc0-w0-LIST_PAGE_WRAPPER__-CTA__-CTA_VIEW__-saveCallToAction__').click()
save_btn = driver.find_element_by_id('wc0-w0-LIST_PAGE_WRAPPER__-CTA__-CTA_VIEW__-listItCallToAction__').click()
time.sleep(3)





