import requests
#UA检测：门户网站的服务器会检测对应请求的载体身份标识，如果检测到载体的身份标识是某一款浏览器，说明该请求是一个正常的请求，
#但如果检测到的身份标识不是基于某一款浏览器的就不是正常请求，就会可能请求失败
#UA：User-Agent
#UA伪装：请求标识伪装为某一款浏览器
if __name__ == '__main__':
    url = 'https://www.sogou.com/web'#query后面对应的是搜索的关键字或者字条
    #UA伪装
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                            'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
    #处理url携带的参数：封装到字典中
    kw = input('录汝一个关键词')
    param = {
        'query':kw
    }
    #对指定的url发起的请求对应的url是携带参数的，并且请求过程中携带了参数
    response = requests.get(url = url,params=param,headers=headers)
    #解释一哈params=param，因为原网站是这样的https://www.sogou.com/web?query=波晓张，而params=param，就是把param参数添加进url中
    print(response.text)
    page_text = response.text

    with open('sousog.html','w',encoding='utf-8') as file:#'sousog.html'这儿可以设置文件格式
        file.write(response.text)
    print('保存成功')
