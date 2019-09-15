import os
import time
import csv
import xlwt
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

###when window
#driver=webdriver.Firefox(executable_path=r'C:\\Users\\pharry\\Downloads\\geckodriver\\geckodriver')
#####
#when ubuntu
driver=webdriver.Firefox(executable_path=r'/media/pharry/New Volume/software/geckodriver')
###
url='https://www.justdial.com/Pune/Holiday-Tour-Packages/nct-10489548'
driver.get(url)
time.sleep(8)
webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
c=1
fh=open('pune_Agents_link.txt','w')
while c<=10:
	for i in range(10):
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(3)
	time.sleep(2)
	data_section=driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[2]/div[1]/div/section/div/ul')
	allagentLinks=data_section.find_elements_by_tag_name('li')
	a=[]
	for agent in allagentLinks:
		if agent.get_attribute("data-href"):
			a.append(agent.get_attribute("data-href"))
			# print(agent.get_attribute("data-href"))
			fh.write(agent.get_attribute("data-href")+"\n")
	print(len(a))
	# if 'Next' in driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/section/div/a[11]').text:
	# 	driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/section/div/a[11]').click()
	# elif 'Next' in driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/section/div/a[12]').text:
	# 	driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[2]/section/div/a[12]').click()
	c+=1
	driver.get('https://www.justdial.com/Pune/Holiday-Tour-Packages/nct-10489548/page-'+str(c))
	time.sleep(5)
fh.close()
driver.quit()

