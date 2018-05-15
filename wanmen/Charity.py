import pandas as pd
from bs4 import BeautifulSoup as bs
import re
import requests
url = 'https://www.charitywatch.org/top-rated-charities'
response = bs(requests.get(url).text,'lxml')
sub_urls = response.find_all(href = re.compile('/ratings-and-metrics'))
sub_url = [addr['href'] for addr in sub_urls]  #get sub_url, can't use addr.href
data = pd.DataFrame(index = ['Money'])
for i,addr in enumerate(sub_urls):
	name = addr.text
	new_addr = 'http://www.charitywatch.org/'+addr['href']
	sub_response = bs(requests.get(new_addr).text,'lxml')
	money = sub_response.find_all(class_ = re.compile('larger'))
	money = money[1].text
	money = money[:money.find('\xa0')]
	data[name] = money
	print(i)