#简历模版下载https://sc.chinaz.com/jianli/free.html
import requests
from lxml import etree
import os

if __name__ == '__main__':
    if not os.path.exists('/Users/yujunxiong/Desktop/1'):
        os.mkdir('/Users/yujunxiong/Desktop/1')
    url = 'https://sc.chinaz.com/jianli/free.html'
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'
                            'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
    reponse = requests.get(url=url,headers=headers)
    reponse.encoding = reponse.apparent_encoding
    reponse_new = reponse.text
    #xpath解析
    tree = etree.HTML(reponse_new)
    result_one = tree.xpath('//div[@class="box col3 ws_block"]/a/@href')
    for wbsite in result_one:
        wbsite_end = 'https:'+ wbsite
        reponse_two = requests.get(url=wbsite_end,headers=headers)
        reponse_two.encoding = reponse_two.apparent_encoding
        reponse_end = reponse_two.text
        #图片xpath
        tree_two = etree.HTML(reponse_end)
        tree_end = tree_two.xpath('//ul[@class="clearfix"]/li[4]/a/@href')[0]
        #标题xpath
        tree_there =etree.HTML(reponse_end)
        tree_start = tree_two.xpath('//div[@class="ppt_tit clearfix"]/h1/text()')
        file_name = '/Users/yujunxiong/Desktop/1/{}.rar'.format(tree_start)
        with open(file_name,'wb') as file:
            result = requests.get(url=tree_end,headers=headers).content
            file.write(result)
            print(tree_start,'下载成功')








