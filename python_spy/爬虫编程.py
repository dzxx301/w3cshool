# !/usr/bin/python
# -*- coding:utf-8 -*-

import requests
from  bs4 import BeautifulSoup

url = 'https://bj.lianjia.com/zufang/'    #链家网爬虫信息
resp = requests.get(url)
# print(resp.text)   #打印得到信息
soup = BeautifulSoup(resp.text,'lxml')
links_div = soup.find_all('div',class_='content__list--item')
# print(links_div)    # 显示所有信息
#print(links_div[0])   #显示第一个信息
links = [div.a.get('href') for div in links_div]
print(links[0])