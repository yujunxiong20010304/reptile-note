#解析下载图片数据
from lxml import etree
import requests
import os
if __name__ == '__main__':
    if not os.path.exists('/Users/yujunxiong/Desktop/1'):
        os.mkdir('/Users/yujunxiong/Desktop/1')
    url = 'https://pic.netbian.com/4kmeinv/index.html'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
                             '(KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
    photo_code = requests.get(url=url,headers=headers)
    photo_code.encoding = photo_code.apparent_encoding#指明编码格式
    photo_page = photo_code.text
    tree = etree.HTML(photo_page)
    defect_website = tree.xpath('//ul[@class="clearfix"]/li/a/@href')
    for web in defect_website:
        website = 'https://pic.netbian.com/'+web
        photo = requests.get(url=website,headers=headers)
        photo.encoding = photo.apparent_encoding
        photo_choice = photo.text
        big_brid = etree.HTML(photo_choice)
        hard_bird = big_brid.xpath('//a[@id="img"]/img/@src')
        for gg in hard_bird:
            dagg = 'https://pic.netbian.com/'+gg
            img = requests.get(url=dagg,headers=headers).content
            file_name = gg.split('-', 1 )[1]
            addres = '/Users/yujunxiong/Desktop/1/'+file_name
            with open(addres,'wb') as file:
                file.write(img)
                print(addres,'下载成功')





