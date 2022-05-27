import re
import requests
# 实验一：访问51testing网站
# 设置url请求：
url = "http://www.51testing.com/html/index.html"
# 发送请求
headers = {'User-Agent':'Mozilla/5.0 (Macintosh;Intel Mac OS X 10_15_7)'
                        'AppleWebKit/537.36 (KHTML,like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
response = requests.get(url = url,headers=headers)
response.encoding = response.apparent_encoding
response = response.text
# 获取请求结果
print(response)
