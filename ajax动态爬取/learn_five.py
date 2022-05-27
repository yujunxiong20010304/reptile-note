#爬取坑的鸡餐厅信息
import requests
import json

if __name__ == '__main__':
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    heardes = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
    prarm = {
        'cname':'',
        'pid':'',
        'keyword': '邯郸',
        'pageIndex': '1',
        'pageSize': '10'
    }
    reponse = requests.post(url=url,headers=heardes,params=prarm)
    data = reponse.text
    print(data)
