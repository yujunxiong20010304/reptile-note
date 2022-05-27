#爬取诗词名句网站上的标题和内容
import os
from bs4 import BeautifulSoup
import requests
if __name__ == '__main__':
    if not os.path.exists('/Users/yujunxiong/Desktop/1'):
        os.mkdir('/Users/yujunxiong/Desktop/1')
    #对首页页面进行爬取
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
                             '(KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    page_text = requests.get(url=url,headers = headers).text.encode('ISO-8859-1')

    #在首页中解析出章节的标题和详情页的url
    #1。实例化一个BeautifulSoup对象，需要将页面源码数据加载到该对象中
    soup = BeautifulSoup(page_text,'lxml')
#-----------------------------------------------------------------------------------------------------------------------
    # 解析章节标题和详情页的url
    #(1)
    '''a_list = soup.select('.book-mulu>ul>li>a')
       for li in a_list:
           title = li.string
           detail_url = 'https://www.shicimingju.com/'+li['href']'''
    a_list = soup.select('.book-mulu>ul>li')
    with open('/Users/yujunxiong/Desktop/1/task.txt','w',encoding='UTF-8') as file:
        # (2)
        for li in a_list:
            title = li.a.string
            detail_url = 'https://www.shicimingju.com/' + li.a['href']
#解释(1)(2)在一中进行对比，说白了（li.string/li.a.string），（li['href']/li.a['href']），得出，这些东西更取决于标签的本身
# -----------------------------------------------------------------------------------------------------------------------
            #对详情页发出请求
            detail_page_text = requests.get(url=detail_url,headers=headers).text.encode('ISO-8859-1')
            #encode('ISO-8859-1')控制编码格式
            #解析出详情页中相关的章节内容
            detail_soup = BeautifulSoup(detail_page_text,'lxml')
            #解析到了章节的内容
            content = detail_soup.find('div',class_='chapter_content').text
            file.write(title+':'+content+'\n')
            print(title,'爬取成功')
