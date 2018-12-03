# -*- coding: utf-8 -*-
#from django.http import HttpResponse
from django.shortcuts import render
import requests
from lxml import etree

#import Sprider

def sprider(urls):
	data = []
	for url in urls:
		r = requests.get(url).text
		s = etree.HTML(r)
		file = s.xpath('//*[@id="hardForkInfo"]/h6[2]')
		for i in file:
			data.append(i.xpath('string()'))
	return data

urls = ['https://cash.coin.dance/',]


def hello(request):
	context = {}
	context['hello'] = sprider(urls)

	return render(request, 'hello.html', context)