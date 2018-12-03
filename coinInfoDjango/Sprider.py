import requests
from lxml import etree

urls = ['https://cash.coin.dance/',]
print(urls)
pinglun = []
for url in urls:
	r = requests.get(url).text
	s = etree.HTML(r)
	file = s.xpath('//*[@id="hardForkInfo"]/h6[2]')
	for i in file:
		print(i.xpath('string()' ))
	pinglun = pinglun + file

#print(pinglun)
