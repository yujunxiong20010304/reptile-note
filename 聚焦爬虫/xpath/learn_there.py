#查看网页的编码格式
import chardet
import requests
url = 'https://pic.netbian.com/4kmeinv/index.html'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
response = requests.get(url=url, headers=headers)
print(response.apparent_encoding)#判断网页编码格式



