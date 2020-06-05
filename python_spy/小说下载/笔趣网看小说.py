# !/usr/bin/python
# -*- coding:utf-8 -*-
# 小说网站-笔趣看：URL：http://www.biqukan.com/
# 本次实战就是从该网站爬取并保存一本名为《临渊行 》的小说，
# 该小说是耳根正在连载中的一部玄幻小说

import requests
from bs4 import BeautifulSoup

# # 以下是代码是爬出网站小说的目录和目录名称
# # 具体的代码参考https://www.w3cschool.cn/python3/python3-enbl2pw9.html
# if __name__ == "__main__":
#     server = "https://www.biqukan.com"
#     target = 'https://www.biqukan.com/25_25963/'
#     req = requests.get(url = target)
#     html = req.text.encode('iso-8859-1').decode('gbk')   # 转换为gbk
#     div_bf = BeautifulSoup(html,'lxml')
#     div = div_bf.find_all('div', class_ = 'listmain')   # 用find_all方法
#      # print(div[0])
#     a_bf = BeautifulSoup(str(div[0]),'lxml')
#     a = a_bf.find_all('a')   # find_all返回的是一个列表，里边存放了很多的<a>标签
#     for each in a:        # for循环遍历每个<a>标签并打印
#         print(each.string, server + each.get('href'))

#  以下代码是爬出网站具体也中的小说文章
if __name__ == '__main__':     # 相当于python模拟的程序入口
    target = 'https://www.biqukan.com/25_25963/526209915.html'
    req = requests.get(url=target)
#    print(req.encoding)       # 得到编码是ISO-8859-1
    html = req.text.encode('iso-8859-1').decode('gbk')   #转换成gbk码可以正常显示
#    print(html)

    bf = BeautifulSoup(html,'lxml')
    texts = bf.find_all('div',class_ = 'showtxt')
    #  在解析html之前，我们需要创建一个Beautiful Soup对象。
    #  BeautifulSoup函数里的参数就是我们已经获得的html信息。
    #  然后我们使用find_all方法，获得html信息中所有class属性为showtxt的div标签。
    #  find_all方法的第一个参数是获取的标签名，第二个参数class_是标签的属性，
    #  为什么不是class，而带了一个下划线呢？因为python中class是关键字，
    #  为了防止冲突，这里使用class_表示标签的class属性，
    #  class_后面跟着的showtxt就是属性值了。
#    print(texts)      # 输出网页信息
    s = str(texts)   #转换成字符串形式
    s=s.replace('<br/>',"\n")         #  <br\>用换行符代替
    print(s)
#    print(str(texts).replace('<br/>',"\n"))    # 所有的<br\>用换行代替