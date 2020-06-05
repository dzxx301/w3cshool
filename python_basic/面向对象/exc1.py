# -*- coding: utf-8 -*-

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0]      # ?
def by_score(t):
    return -t[1]     # ?

# 按照字母顺序排列.    sorted()函数按照key进行排序，并按照对应关系返回list相应的元素
L1 = sorted(L, key=by_name)
# 按照成绩高低排列
L2 = sorted(L, key=by_score)
print(L1)
print(L2)

print(dir('abc'))