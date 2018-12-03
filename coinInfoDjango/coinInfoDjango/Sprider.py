import requests
from lxml import etree


'''print(urls)
pinglun = []
for url in urls:
	r = requests.get(url).text
	s = etree.HTML(r)
	file = s.xpath('//*[@id="hardForkInfo"]/h6[2]')
	for i in file:
		print(i.xpath('string()' ))
	pinglun = pinglun + file'''



#print(pinglun)
def sprider(urls):
	data = []
	for url in urls:
		r = requests.get(url).text
		s = etree.HTML(r)
		file = s.xpath('//*[@id="hardForkInfo"]/h6[2]')
		for i in file:
			data.append(i.xpath('string()'))
	return data
