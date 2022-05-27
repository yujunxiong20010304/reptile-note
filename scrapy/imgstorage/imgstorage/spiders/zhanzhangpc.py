#爬取图片
'''
图片懒加载：
    反爬机制
    只有当图片滑动到可视区范围的时候才能显示真真的东西
    也即是伪属性
'''



import scrapy
from imgstorage.items import ImgstorageItem

class ZhanzhangpcSpider(scrapy.Spider):
    name = 'zhanzhangpc'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['https://sc.chinaz.com/tupian/']

    def parse(self, response):
        div_list = response.xpath('//*[@id="container"]/div')
        for div in div_list:
            #注意使用伪属性
            src = 'https:'+div.xpath('./div/a/img/@src2').extract_first()
            #去掉地址中的_s就是高清
            item = ImgstorageItem()
            item['src'] = src
            yield item



