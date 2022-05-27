#爬取全国城市名称
import requests
from lxml import etree
if __name__ == '__main__':
    url = 'https://www.aqistudy.cn/historydata/'
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                            'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
    reponse = requests.get(url=url,headers=headers).text
    tree = etree.HTML(reponse)
    data = tree.xpath('//ul[@class="unstyled"]/div/li/a/text()')
    qatq = tree.xpath('//ul[@class="unstyled"]/li/a/text()')
    print(data)
    print(qatq)
