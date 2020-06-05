# !/usr/bin/python
# -*- coding:utf-8 -*-
'''
从拉钩网上爬取-软件测试-职位所有数据
2020-4-12
'''
import requests
import time
import json

# url start中的网址是浏览器框中的复制得到
# url parse 的网址是按F12-》network——》XHR中在name选择Ajax网页，然后再Preview去查看结果
# 结果中content-》positionResult-》result中是查到第1页所有岗位公司信息
# headers和data中的数据是在第二网址中Headers中，data数据即From data
def main():
    url_start = "https://www.lagou.com/jobs/list_%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95?labelWords=&fromSearch=true&suginput="
    url_parse = "https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false"
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Referer': 'https://www.lagou.com/jobs/list_%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95?labelWords=&fromSearch=true&suginput=',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    }
    for x in range(1, 5):
        data = {
            'first': 'true',
            'pn': str(x),
            'kd': '软件测试'
                }
        # requests库的session会话对象可以跨请求保持某些参数，说白了，
        # 就是比如你使用session成功的登录了某个网站，则在再次使用该session对象
        # 求求该网站的其他网页都会默认使用该session之前使用的cookie等参数
        s = requests.Session()
        s.get(url_start, headers=headers, timeout=3)  # 请求首页获取cookies，用的是get
        cookie = s.cookies  # 为此次获取的cookies
        response = s.post(url_parse, data=data, headers=headers, cookies=cookie, timeout=3)
        # 获取此次文本，用的是post
        time.sleep(5)
        response.encoding = response.apparent_encoding
        text = json.loads(response.text)
        info = text["content"]["positionResult"]["result"]
        for i in info:
            print(i["companyFullName"])
            companyFullName = i["companyFullName"]
            print(i["positionName"])
            positionName = i["positionName"]
            print(i["salary"])
            salary = i["salary"]
            print(i["companySize"])
            companySize = i["companySize"]
            print(i["skillLables"])
            skillLables = i["skillLables"]
            print(i["createTime"])
            createTime = i["createTime"]
            print(i["district"])
            district = i["district"]
            print(i["stationname"])
            stationname = i["stationname"]

if __name__ == '__main__':
    main()

