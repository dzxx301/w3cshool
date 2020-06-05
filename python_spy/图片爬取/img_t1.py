# !/usr/bin/python
# -*- coding:utf-8 -*-
'''
下面例子是爬取一个动态网站消息
'''
import requests
if __name__ == '__main__':
    target = 'https://unsplash.com'
    req = requests.get(url=target)
    print(req.text)