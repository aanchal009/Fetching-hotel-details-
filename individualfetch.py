# import os
# import time
# import csv
# import xlwt
# import requests
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.common.keys import Keys
# driver=webdriver.Firefox(executable_path=r'C:\\Users\\pharry\\Downloads\\geckodriver\\geckodriver')
# driver.get(url)
# agent_name=driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[1]/div[2]/div/div/h1/span/span').text
# address=driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[4]/div[1]/div[1]/ul/li[1]/span[2]/span/span/span').text
# phone=driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[4]/div[1]/div[1]/ul/span[2]/a').text
# website=driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[4]/div[1]/div[1]/ul/li[5]/span/a').text
# print(agent_name,"\n")
# print(phone,"\n")
# print(address,"\n")
# print(website,"\n")

# driver.quit()


from urllib.request import Request, urlopen
import re
from lxml import html
import time
url='https://www.justdial.com/Mumbai/Bookmyticket-com-Near-Andheri-Subway-Andheri-East/022PXX22-XX22-150421200027-L8F2_BZDET?xid=TXVtYmFpIEhvbGlkYXkgVG91ciBQYWNrYWdlcw=='
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
tree=html.fromstring(webpage)
phone_block=tree.xpath('/html/body/div[2]/div[1]/div/div[4]/div[1]/div[1]/ul/span[2]/a')[0]
print(html.tostring(phone_block))
phone_list=tree.xpath('/html/body/div[2]/div[1]/div/div[4]/div[1]/div[1]/ul/span[2]/a/span')
#print(phone_list)
phone=''
for digit in phone_list:
	dc=digit.get('class')
	cl=dc.split()[1]
	print(cl)
	ans=re.search('.'+cl+':before[{]content[:]["](.*?)["][}]',webpage.decode())
	print(ans.group())
	al=ans.group(1)[-2:]
	print(int(al)-1)

print("hello",tree.xpath('/html/body/div[2]/div[1]/div/div[1]/div[2]/div/ul/li[2]/p/span[2]/span/a/span[2]')[0].attrib['style'])
print('hello',html.tostring(tree.xpath('/html/body/div[2]/div[1]/div/div[1]/div[2]/div/ul/li[2]/p/span[2]/span/a/span[2]')[0]))
agent_name=tree.xpath('/html/body/div[2]/div[1]/div/div[1]/div[2]/div/div/h1/span/span')[0].text
address=tree.xpath('/html/body/div[2]/div[1]/div/div[4]/div[1]/div[1]/ul/li[1]/span[2]/span/span/span')[0].text
website=tree.xpath('/html/body/div[2]/div[1]/div/div[4]/div[1]/div[1]/ul/li[5]/span/a')[0].text
print(agent_name.strip(),"\n")
print(phone.strip(),"\n")
print(address.strip(),"\n")
print(website.strip(),"\n")
