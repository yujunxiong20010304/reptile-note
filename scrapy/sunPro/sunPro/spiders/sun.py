import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from sunPro.items import SunproItem,DetailItem
#爬取元气壁纸

class SunSpider(CrawlSpider):
    name = 'sun'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['https://bizhi.ijinshan.com/2/index_1.shtml']
    #-------------------------------------------------------------------------------------------------------------------

    #链接提取器：根据指定规则（allow="正则"）进行指定链接的提取
    link = LinkExtractor(allow=r'https://bizhi.ijinshan.com/2/index_\d+\.shtml')
    #规则解析器：将链接提取器提取到的链接进行指定规则（callback）的的解析操作
    link_detail = LinkExtractor(allow=r'https://bizhi.ijinshan.com/2/\d+\.shtml')
    rules = (Rule(link,callback='parse_item',follow=True),
             Rule(link_detail,callback='parse_detail',follow=True)) #这里的 , 不能少
    #follow=True:可以将链接提取器继续作用到连接提取器提取到的链接所对应的页面中（可以一直爬完） 会自动去重

    #⚠️ 当这里有两个link时会先执行第一个在在第一个基础上执行第二个

    #因为这个参数的传递是这Rule来自动进行的，所以是不可以实现请求参数，所以后面的parse_item和parse_detail不能进行请求传参
    #就无法将两个解析出来的数据存储到同一个item中，所以只有存到两个item中，在items.py文件中定义两个类
    #


    '''rules = (
        #Rule规则解析器（实例化了一个rules的对象）将链接提取器提取到的链接进行指定规则（callback）的的解析操作
        #LinkExtractor 链接提取器,根据指定规则（allow="正则"）进行指定链接的提取
        Rule(LinkExtractor(allow=r'https://bizhi.ijinshan.com/2/index_\d+.shtml'), callback='parse_item', follow=True),
    )'''

    #-------------------------------------------------------------------------------------------------------------------
    #解析图片名称
    def parse_item(self, response):
        #xpath中不能出现tbody标签，匹配不到tbody,有tbody就把tbody改为//
        div_list = response.xpath('/html/body/aside[1]/section[2]/div/div')
        for div in div_list:
            photot_name = div.xpath('./a/@href').get()  #get()等同于extract()
            item = SunproItem()
            item['photot_name'] = photot_name
            yield item
    def parse_detail(self,response):
        detail = response.xpath('/html/body/div[1]/section[1]/div[1]/div/h1').extract_first()
        item = DetailItem()
        item['detail'] = detail
        yield item

