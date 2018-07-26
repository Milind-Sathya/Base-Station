#This code scroll and scrape the website link that you provide and download all the
#images in that site in to a folder called 'image' crated inside scraper folder.
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import shutil
import time
"""
base1_url = 'http://pgstay.com/pgs-near-'
location_url = 'marathahalli'
base2_url = '/page/'
page_url = '1'
"""
url = input('Provide the link of the page: ')#'http://www.crossword.in/books'
rawwebpage = requests.get(url)
print(rawwebpage.status_code)
webpage = BeautifulSoup(rawwebpage.text,'html.parser')
"""
#To save details in text doc
with open('C:\\Users\\Milind\\Desktop\\deolite.txt','a') as filer:
	for link in webpage.find_all('a'):
		#print(a.get_text())
		filer.write(link.get_text())
"""
"""
#To get a string inside a tag by mentining its class name
for each_div in webpage.find_all('div',{'class':'categoryBookTitle'}):
	print(each_div.string)
"""
'''
for each_book in webpage.find_all(class_ = "variant-desc"):
	book_name = each_book.find('a',title = True)
	print(book_name.get_text())
	book_author = each_book.find_all(class_ = 'ctbr-name')[0]
	print(book_author.get_text())
	print('\n')
'''	
pageimage = len(webpage.find_all('img'))
print('from request: ' + str(pageimage))
driver = webdriver.Chrome('C:\\Python36\\chromedriver.exe')
driver.get(url)
numOfScroll = 0
while numOfScroll < 2:
	driver.execute_script('window.scrollTo(0,10000)')
	numOfScroll +=1
	time.sleep(5)
rawpage = driver.execute_script('return document.documentElement.outerHTML')
page = BeautifulSoup(rawpage,'html.parser')
cur_path = os.getcwd()
imagetaglist = page.find_all("img",limit = 10)
for imagetag in imagetaglist:
	imagesource = imagetag["src"]
	imagename = os.path.basename(imagesource)
	print(imagename)
	new_path = os.path.join(cur_path,"images",imagename)
	online_img = requests.get(imagesource,stream = True)
	print(online_img.raw)
	with open(new_path,"wb") as output:
		shutil.copyfileobj(online_img.raw,output)