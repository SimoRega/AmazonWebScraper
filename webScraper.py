# import libraries 

from bs4 import BeautifulSoup
import requests
import time
import datetime

import smtplib

URL = 'https://www.amazon.it/Intel-Core-i5-12500-generazione-BX8071512500/dp/B09MDDBYXZ/ref=sr_1_1?__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=AAACP6JFD5LX&keywords=12500&qid=1658778075&sprefix=1250%2Caps%2C97&sr=8-1'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find(id = "productTitle").get_text().strip()[:20]
costo=soup2.find_all("span", class_="a-offscreen")
costo=costo[0].get_text().strip()[0:]


print(title)
print(costo)
