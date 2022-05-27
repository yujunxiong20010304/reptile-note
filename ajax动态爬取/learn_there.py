#破解百度翻译
#要找出post请求的网址，检查——>Network——>XHR，#同时也可以判断是否用post请求，Request URL:网址，最底部就是携带的参数
import json

import requests

if __name__ == '__main__':
    #这儿是发送post请求
    post_url = 'https://fanyi.baidu.com/sug'
    #post请求参数处理(同get参数处理一样)
    word = input('请输入要翻译的单词')
    data = {
        'kw':word
    }
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
    response = requests.post(url=post_url,data=data,headers = headers)
    #获取响应数据json（）方法返回的是obj（如果确认响应数据是json类型的，才可以使用json（））
    dic_obj = response.json()
    print(dic_obj)
    #持久化存储数据
    fp = open('nnn.json','w',encoding='utf-8')
    json.dump(dic_obj,fp=fp,ensure_ascii=False)#ensure_ascii=False   因为json.dump拿到的是中文的所以不能用ascii编码

