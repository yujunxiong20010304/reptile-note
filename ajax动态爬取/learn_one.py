#requests模块的作用：模拟浏览器发请求
'''（requests编码流程）
1。指定url
2。发起请求
3。获取响应数据
4。持久化存储
'''
#爬取搜索狗主页页面
import requests

if __name__ == '__main__':
    #1.指定url
    url = 'https://www.sogou.com/'
    #2.发起请求
    response = requests.get(url=url)#get方法请求成功后会返回一个响应对象
    #3.获取响应数据
    page_text = response.text#text返回一组字符串数据
    print(page_text)
    #4.持久化存储
    with open('sougou','w',encoding='utf-8') as file:
        file.write(page_text)
    print('爬取数据结束')

