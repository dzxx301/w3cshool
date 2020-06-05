# !/usr/bin/python
# -*- coding:utf-8 -*-

import pandas as pd

datas = pd.DataFrame()
for i in range(1,188):
    url = 'https://s.askci.com/stock/a/0-0?reportTime=2019-6-30&pageNum=%s' % (str(i))
    # 获取表格数据 1页，它是这网页中的第4个表格
    data = pd.read_html(url)[3]
    # 把各个dataframe合并到一起
    datas = pd.concat([datas,data])
    print('第' + str(i) + '页抓取完成')

datas.to_excel('E:/datas.xlsx',index= None)