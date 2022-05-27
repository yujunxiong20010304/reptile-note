#基于管道的持久化存储
import scrapy
from study.items import StudyItem   #导入item这个类

class QiushibaikeGdSpider(scrapy.Spider):
    name = 'qiushibaike_gd'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    def parse(self, response):
        # 在scrapy中是不需要获取响应数据的
        div_list = response.xpath('//*[@id="content"]/div/div[2]/div')
        for div in div_list:
            end = div.xpath('./a/div/span//text()').extract()
            end = ''.join(end)
            # extract()可以将Selector对象中data参数存储的字符串提取出来
            '''不管是谁调用了extract之后，则表示将列表中每一个Selector对象中data对应的字符串提取了出来
            xpath返回结果是一个列表，而这个列表中存储的是许多的Selector对象，所以对他使用后可以将
            data中的字符串提取出来'''
            item = StudyItem()  #实例化item对象
            item['end']=end #将解析的数据封装到该类型对象当中
            yield item #将item提交到管道
