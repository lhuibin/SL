import requests,io,sys,time
import pandas as pd
from lxml import etree

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding = 'gb18030') 



# 爬取(mytoken)交易所交易对，并根据市值筛选
url = 'https://www.mytoken.io/api/ticker/pairlist?market_id=1490&market=&page=1&size=100&need_pagination=1&timestamp=1538536674881&code=d2b9f5abb2b6ecb4ce009faea7953e7a&platform=web_pc&v=1.0.0&language=zh_CN&legal_currency=USD'

response = requests.get(url).json()['data']['list']
data = []

for i in response:
	if i['rank']<200 or float(i['market_cap_usd'])>20000000.00: # 筛选数据
		pass
	else:
		data.append([i['id'],i['symbol'],i['rank'],i['market_cap_usd']])

print(len(data),data)



for j in data:
	url_coin = 'https://www.mytoken.io/currency/{}'.format(j[0])
	try:
		response_data = requests.get(url_coin).text
		s = etree.HTML(response_data)
		#base_info_1 = s.xpath('//*[@id="__layout"]/div/div[1]/section/div[1]/div[2]/div[2]/div[1]/div[1]/div/h3/text()')
		#base_info_2 = s.xpath('//*[@id="__layout"]/div/div[1]/section/div[1]/div[2]/div[2]/div[1]/div[1]/div/div/p/text()')
		Circulating_Supply = s.xpath('//*[@id="__layout"]/div/div[1]/section/div[1]/div[2]/div[2]/div[1]/div[1]/table/tbody/tr[1]/td[2]/div[2]/text()')[0].split(' ')[0]
		Total_Supply = s.xpath('//*[@id="__layout"]/div/div[1]/section/div[1]/div[2]/div[2]/div[1]/div[1]/table/tbody/tr[1]/td[3]/div[2]/text()')[0].split(' ')[0]
		other_info_1 = s.xpath('string(//*[@id="__layout"]/div/div[1]/section/div[1]/div[2]/div[2]/div[1])')
		ex = s.xpath('//*[@id="__layout"]/div/div[1]/section/div[1]/div[3]/div[3]/div/div/div/div/div/table/tbody/tr/td[1]/a/div/div/text()')
		#j.append(base_info_1)
		#j.append(base_info_2)
	
		j.append(Circulating_Supply)
		j.append(Total_Supply)
		j.append(ex)
		j.append(other_info_1)
		print(j,'\n +++++++++++++++++++ \n')
	except:
		j.append('flase')
		print('错误，跳过。。。')

	time.sleep(2)
df = pd.DataFrame(data)

df.to_excel('data.xlsx', sheet_name = 'Sheet1')
df.to_csv('data.csv')
