# 工作地址参数
import requests
from lxml import etree
import re


def address():
    result = []
    url = 'https://www.zhaopin.com/citymap'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
    city_code = requests.get(url=url,headers=headers)
    city_code.encoding = city_code.apparent_encoding
    city_code = city_code.text
    tree = etree.HTML(city_code)
    list_div = tree.xpath('//*[@id="root"]/div[2]/div[3]/div')
    for div in list_div:
        list_li = div.xpath('./ul/li')
        for li in list_li:
            data = li.xpath('./a/text()')
            real = data[0].rstrip()
            result.append(real)
    return result


def work():
    url = 'https://i.zhaopin.com/'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
    city_code = requests.get(url=url,headers=headers)
    city_code.encoding = city_code.apparent_encoding
    city_code = city_code.text
    reguler = re.compile(r'<a rel="nofollow" class="zp-jobNavigater__pop--href">(.*?)</a>',re.S)
    result = reguler.findall(city_code)
    new_result = list(result)#去重
    return new_result


def merge(title_list, words):
    title_url = []
    for data in title_list:
        url = 'https://sou.zhaopin.com/?jl={}&kw='.format(data)
        for word in words:
            path = url + word+'&p='

            title_url.append(path)

    return title_url


if __name__ == '__main__':
    title_data = address()
    words_data = work()
    urls = merge(title_data, words_data)
