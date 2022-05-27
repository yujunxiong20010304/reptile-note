#爬取豆瓣网
import requests
import json

if __name__ == '__main__':
    url = 'https://movie.douban.com/j/chart/top_list'
    #url = 'https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=20&limit=20'完整地址
    param = {
        'type': '24',
        'interval_id': '100:90',
        'action':'',
        'start': '20',#从库中第几部电影去取
        'limit': '20'#取得个数
    }
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
    response = requests.get(url=url,headers=headers,params=param)
    list_data = response.json()

    fp = open('douban.json','w',encoding='utf-8')
    json.dump(list_data,fp=fp,ensure_ascii=False)

    print('爬取结束！！')
