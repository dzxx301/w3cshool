# !/usr/bin/python
# -*- coding:utf-8 -*-

import pymysql     #利用mysql-connector驱动
# 创建数据库链接
mydb = pymysql.connect(
    host="localhost",  # 数据库主机地址
    port= 3306,
    user="root",  # 数据库用户名
    passwd="Root_Password",  # 数据库密码
    db="homework1"
)

mycursor = mydb.cursor()
# 输出所有数据库列表：show databases
mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)

try:
    mycursor.execute("select * from user1")
    data1 = mycursor.fetchall()
    print("id","usename","password")
    for row in data1:
        id = row[0]
        usename = row[1]
        password = row[2]
        print(id,usename,password)
except Exception as e:
    raise e
finally:
    mydb.close()
# 遍历结果

#  详细数据库参考https://www.runoob.com/python3/python-mysql-connector.html
# ###################################################################################
# 利用MySQLdb驱动
#  安装mysqldb方法：
#  从https://pypi.python.org/pypi/mysqlclient下载最新的对应版本；
#  下载下来之后，放到你pyhton安装目录pip所在的目录，一般都是\Python\Python37\Scripts这个位置

#  -----------------------------------------------------------
# import MySQLdb
#
# # 连接数据库      连接地址  账号  密码   数据库   数据库编码
# db = MySQLdb.connect(
#     host="localhost",  # 数据库主机地址
#     user="root",  # 数据库用户名
#     passwd="Root_Password",  # 数据库密码
#     database="examination"
#     )
# # 使用cursor()方法获取操作游标
# cursor = db.cursor()
#
# # 使用execute方法执行SQL语句
# cursor.execute("SELECT VERSION()")
#
# # 使用 fetchone() 方法获取一条数据库。
# data = cursor.fetchone()
#
# print("Database version : %s " % data)
#
# # 关闭数据库连接
# db.close()