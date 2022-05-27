#爬取网易云新闻页面
import scrapy
from selenium import webdriver #导入selenium的包
from zhilian.items import ZhilianItem
class WangyiSpider(scrapy.Spider):
    name = 'wangyi'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['https://news.163.com/']
    models_urls = []  # 存储五个板块的详情页面板块

    # ——————————————————————————————————————————————————————————————
    # 实例化一个浏览器对象
    def __init__(self):
        # 书写selenium程序
        self.browser = webdriver.Chrome()
    # ---------------------------------------------------------------

    #解析五大板块对应详情页的url
    def parse(self, response):
        li_list = response.xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div/ul/li')
        alist = [3,4,6,7,8]
        for index in alist:
            model_url = li_list[index].xpath('./a/@href').extract_first()
            self.models_urls.append(model_url)
            #依次对每个板块的详情页发送请求
        for url in self.models_urls:
            yield scrapy.Request(url=url,callback=self.parse_model)


    #每一个板块详情页的信息都是动态加载的
    def parse_model(self,response):#解析每一个板块的详情页
        div_list = response.xpath('/html/body/div/div[3]/div[4]/div[1]/div[1]/div/ul/li/div/div')
        for div in div_list:
            title = div.xpath('./div/div[1]/h3/a/text()').extract_first()
            new_detail_url = div.xpath('./a/@href').extract_first()
            #对详情页的url发送请求
            item = WangyiproItem()
            item['title'] = title
            yield scrapy.Request(url=new_detail_url,callback=self.parse_detail,meta={'item':item})

    def parse_detail(self,response):
        content = response.xpath('/html/body/div[3]/div[1]/div[3]/div[2]/p//text()').extract()
        content =''.join(content)
        item = response.meta['item']
        item['content'] = content
        yield item

    def closed(self,spider):
        self.browser.quit()






