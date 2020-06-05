# !/usr/bin/python
# -*- coding:utf-8 -*-

import pandas as pd

df=pd.read_excel(r'E:\cj1921.xlsx')
print(df.duplicated())