import requests
from bs4 import BeautifulSoup

re = requests.get('https://ctee.com.tw/livenews/aj/page/1')
#print(re)

soup = BeautifulSoup(re.text,'html.parser')
#print(soup)

content = soup.select('div.item-content')
#print(content)

url01 = soup.select('div.item-content')[0].select('a')[1]['href']
title01 = soup.select('div.item-content')[0].select('a')[1].text

print(url01)
print(title01)