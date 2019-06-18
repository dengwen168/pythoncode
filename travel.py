import requests
from bs4 import BeautifulSoup

url = "http://wap.bytravel.cn/"
wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text,'lxml')


urls = []

with open("result.txt","a",encoding='utf-8') as f:
	address = soup.find_all('li')
	for i in address:
		f.write(i.find('a').get("href"))
