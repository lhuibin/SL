#! /usr/bin/env python
# -*- coding:utf=8 -*-
''' 爬取拉钩职位列表
from pymongo import MongoClient
import requests,time
from fake_useragent import UserAgent


client = MongoClient()
db = client.lagou # 创建一个拉钩数据库
lagou = db.C # 创建job集合




headers = {
    'Cookie':'JSESSIONID=ABAAABAAAGFABEF314098DC27BD35542BCE0BC1B97D6CB3; user_trace_token=20180923214542-5f06c7e4-8aaf-4be7-8932-5517792ebcf7; _ga=GA1.2.383354067.1537710344; _gid=GA1.2.1396643864.1537710344; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1537710344; LGSID=20180923214543-f7555a59-bf36-11e8-bb56-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_%25E7%2588%25AC%25E8%2599%25AB%3FlabelWords%3D%26fromSearch%3Dtrue%26suginput%3D; LGUID=20180923214543-f7555c96-bf36-11e8-bb56-5254005c3644; TG-TRACK-CODE=jobs_code; _gat=1; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1537710719; LGRID=20180923215158-d6cabc6a-bf37-11e8-a57a-525400f775ce; SEARCH_ID=6717b8d9b1e244a5aed937b13e18303c',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'Referer':'https://www.lagou.com/jobs/list_%E7%88%AC%E8%99%AB?px=default&city=%E8%8B%8F%E5%B7%9E',
} #填入对应的headers信息

def get_job_info(page, kd):
    url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E8%8B%8F%E5%B7%9E&needAddtionalResult=false'
    #ua = UserAgent()
  #  headers['User-Agnet'] = ua.random
    for i in range(1,page+1):
        payload = {
            'first':'True',
            'pn':i,
            'kd':kd,
        }
        response = requests.post(url, data = payload, headers = headers)
        if response.status_code == 200:
            job_json = response.json()['content']['positionResult']['result']
            lagou.insert(job_json)
        else:
            print('Something Wrong!')
        print('正在爬取'+ str(i) + '页的数据...')
        time.sleep(3)

if __name__ == '__main__':
    get_job_info(27,'c')
'''

#爬取拉钩详情页面
from pymongo import MongoClient
import requests,time
from lxml import etree
from fake_useragent import UserAgent


client = MongoClient()
db = client.lagou # 创建一个拉钩数据库
lagou = db.job_info # 创建job集合



global headers
headers = {
    'Cookie':'user_trace_token=20180923214542-5f06c7e4-8aaf-4be7-8932-5517792ebcf7; _ga=GA1.2.383354067.1537710344; _gid=GA1.2.1396643864.1537710344; LGUID=20180923214543-f7555c96-bf36-11e8-bb56-5254005c3644; index_location_city=%E5%85%A8%E5%9B%BD; JSESSIONID=ABAAABAAAGFABEF40DDA666E3A5EB063AD9B0E4A97463CB; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1537710344,1537755914,1537801946; LGSID=20180924231228-405f86bc-c00c-11e8-a5b1-525400f775ce; PRE_UTM=; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DQ3OxbHxsez7eW51gN3CqDyFHD9r689t4m1DOmWRokEO%26wd%3D%26eqid%3Dd50455700001b78e000000055ba8fed6; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; TG-TRACK-CODE=index_search; SEARCH_ID=029a54068e61474b92e21bb8f5467f20; _gat=1; LGRID=20180924231440-8edf4caf-c00c-11e8-a5b1-525400f775ce; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1537802078',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'Referer':'https://www.lagou.com/jobs/list_c?px=default&city=%E8%8B%8F%E5%B7%9E',
} #填入对应的headers信息

def get_text_info(positionId):
    text_info = {}
    url = 'https://www.lagou.com/jobs/{}.html'.format(positionId)
    response =  requests.get(url, headers = headers)

    headers['Cookie'] = response.request.headers['Cookie']
    time.sleep(1)
    if response.status_code == 200:
        r = response.text
        s = etree.HTML(r)
        text_info['title'] = s.xpath('/html/body/div[3]/div/div[1]/div/span/text()')[0]
        text_info['title_yaoqiu'] = [i.strip('/') for i in s.xpath('/html/body/div[3]/div/div[1]/dd/p[1]/span/text()')]
        text_info['title_lable'] = s.xpath('/html/body/div[3]/div/div[1]/dd/ul/li/text()')
        title_youhuo11 = s.xpath('//*[@id="job_detail"]/dd[position()<4]')
        title_youhuo = []
        for z in title_youhuo11:
            title_youhuo.append(z.xpath('string(.)').replace('  ','').replace('\n', '').replace('查看地图', ''))
        text_info['title_youhuo'] = title_youhuo
        company_info11 = s.xpath('//*[@id="job_company"]')

        company_info = []
        for z in company_info11:
            company_info.append(z.xpath('string()').replace('   ','').replace('\n', ''))
        text_info['company_info'] = company_info
        #print(text_info)
        lagou.insert(text_info)
    else:
        print('Something Wrong!')

def get_job_info(page, kd):
    url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E8%8B%8F%E5%B7%9E&needAddtionalResult=false'
    #ua = UserAgent()
  #  headers['User-Agnet'] = ua.random
    for i in range(1,page+1):
        payload = {
            'first':'True',
            'pn':i,
            'kd':kd,
        }
        response = requests.post(url, data = payload, headers = headers)

        headers['Cookie'] = response.request.headers['Cookie']
        print('正在爬取第'+ str(i) + '页列表')
        if response.status_code == 200:
            job_json = response.json()['content']['positionResult']['result']
            for j in job_json:
                get_text_info(j['positionId'])
                print('第'+str(j['positionId'])+'职位的数据')
            #lagou.insert(job_json)
        else:
            print('Something Wrong!')

        time.sleep(3)

if __name__ == '__main__':
    get_job_info(10,'c')
