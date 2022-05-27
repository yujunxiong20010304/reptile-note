#爬虫
#headers这是网站代理  在网站chrome://version/查看
#url 要查看的网站地址
#if response.status_code == 200:判断是否访问成功
#print(response.text) 以文本格式输入
#response.encoding='utf-8' 编码转换
import requests
import django
import pymysql
import re
def sousuo(url,headers):
    response = requests.get(url,headers)
    response.encoding='utf-8'
    #定义正则表达式
    zhengze = re.compile(r'<a href="/scwsjkw/gzbd01/(.*?) target="_blank" (.*?)</a>', re.S)

    if response.status_code == 200:
        response = response.text
        result = zhengze.findall(response)
        print(result)

    else:
        print('无法访问')
def main():
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36'}
    url_list = ['http://wsjkw.sc.gov.cn/scwsjkw/gggs/tygl.shtml',
                'http://wsjkw.sc.gov.cn/scwsjkw/gggs/tygl_2.shtml',
                'http://wsjkw.sc.gov.cn/scwsjkw/gggs/tygl_3.shtml']
    for url in url_list:
        sousuo(url, headers)

if __name__ == '__main__':
    main()
