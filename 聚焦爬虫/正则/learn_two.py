import requests
import re
import os
#通过os模块创建一个文件夹

'''
普及一个format的用法
task = '我是你%s'
ship = '爹'
task_ship = format(task%ship)
'''

'''text(字符串)   content(二进制)  josn()(对象)'''
if __name__ == '__main__':
    if not os.path.exists('/Users/yujunxiong/Desktop/1'):
        os.mkdir('/Users/yujunxiong/Desktop/1')  # 如果这个文件夹不存在则创建一个文件夹
    #如何爬取图片数据
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}

    #使用通用爬虫对整张页面数据进行爬取
    choice = int(input('选择要爬取的页面'))
    url = 'https://www.qiushibaike.com/imgrank/page/{}/'.format(choice)
    #url = 'https://www.qiushibaike.com/imgrank/page/%d/' % choice#这样也行
    general_crawler = requests.get(url=url,headers=headers).text

    #general_crawler.encoding=general_crawler.apparent_encoding

    reguler = re.compile(r'<img src="//pic.qiushibaike.com/system/(.*?)"',re.S)#re.S让.可以匹配/
    result = reguler.findall(general_crawler)
    list_tu = []
    name = 0
    for i in result:
        webist = 'https:'+'//pic.qiushibaike.com/system/'+i
        tutu = requests.get(url=webist,headers=headers).content
        file_name = '/Users/yujunxiong/Desktop/1/{}.jpg'.format(name)
        name+=1
        with open(file_name,'wb') as file:
            file.write(tutu)






