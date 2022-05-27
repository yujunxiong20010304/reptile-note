#需求：
import requests
url = 'https://www.baidu.com/s?wd=ip'
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
page_text = requests.get(url=url,headers=headers,proxies={"https":"175.24.250.39.443"}).text
#在proxies={"https":"175.24.250.39.443"}中输入代理IP
page_text.encoding = page_text.apparent_encoding
page_text = page_text.text

with open('ip.html','w',encoding='utf-8') as file:
    file.write(page_text)
