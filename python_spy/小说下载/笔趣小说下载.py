# !/usr/bin/python
# -*- coding:utf-8 -*-
# 小说网站-笔趣看：URL：http://www.biqukan.com/
# 本次实战就是从该网站爬取并保存一本名为《临渊行 》的小说，
# 该小说是耳根正在连载中的一部玄幻小说

from bs4 import BeautifulSoup
import requests, sys

"""
类说明:下载《笔趣看》网小说《一念永恒》
Parameters:
    无
Returns:
    无
Modify:
    2017-09-13
"""
class downloader(object):

    def __init__(self):
        self.server = "https://www.biqukan.com"
        self.target = 'https://www.biqukan.com/25_25963/'
        self.names = []          #存放章节名
        self.urls = []           #存放章节链接
        self.nums = 0            #章节数

    """
    函数说明:获取下载链接
    Parameters:
        无
    Returns:
        无
    Modify:
        2020-02-13
    """
    def get_download_url(self):
        req = requests.get(url = self.target)
        html = req.text.encode('iso-8859-1').decode('gbk')   # 转换为gbk
        div_bf = BeautifulSoup(html,'lxml')
        div = div_bf.find_all('div', class_ = 'listmain')
        a_bf = BeautifulSoup(str(div[0]),'lxml')
        a = a_bf.find_all('a')
        self.nums = len(a[12:])        # 剔除不必要的章节，并统计章节数
        for each in a[12:]:
            self.names.append(each.string)
            self.urls.append(self.server + each.get('href'))
        print(self.names)
    """
    函数说明:获取章节内容
    Parameters:
        target - 下载连接(string)
    Returns:
        texts - 章节内容(string)
    Modify:
        2020-02-13
    """
    def get_contents(self, target):
        req = requests.get(url = self.target)
        html = req.text.encode('iso-8859-1').decode('gbk')
        bf = BeautifulSoup(html,'lxml')
        texts = bf.find_all('div', class_ = 'showtxt')
        text = str(texts).replace('<br/>',"\n")
        print(text)
        return text

    """
    函数说明:将爬取的文章内容写入文件
    Parameters:
        name - 章节名称(string)
        path - 当前路径下,小说保存名称(string)
        text - 章节内容(string)
    Returns:
        无
    Modify:
        2020-02-13
    """
    def writer(self, name, path, text):
        write_flag = True
        with open(path, 'a', encoding='utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')

if __name__ == "__main__":
    dl = downloader()
    dl.get_download_url()
    print('《临渊行》开始下载：')
    for i in range(dl.nums):
        dl.writer(dl.names[i], '临渊行.txt', dl.get_contents(dl.urls[i]))
        sys.stdout.write(" 已下载:%.3f%%" %  float(i/dl.nums) + '\r')
        sys.stdout.flush()
    print('《临渊行》下载完成')