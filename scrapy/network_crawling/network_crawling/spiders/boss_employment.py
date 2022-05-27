#深度爬取  爬取boss直聘中的网页数据


#！！！注意这个程序爬不出代码，应为当前所爬网页为动态加载数据，而现在还没学动态加载  只为记录请求传参操作

import scrapy
from spiders.items import NetworkCrawlingItem

class BossEmploymentSpider(scrapy.Spider):
    name = 'boss_employment'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.zhipin.com/job_detail/?query=python&city=101270100&industry=&position=']

    def parse_detail(self,response):
        #回调函数接受参数
        item = response.meta['item']
        job_desc = response.xpath('//*[@id="main"]/div[3]/div/div[2]/div[2]/div[1]/div//text()').extract()
        job_desc = ''.join(job_desc)
        item['job_desc'] = job_desc

        yield item

    def parse(self, response):
        li_list = response.xpath('//*[@id="main"]/div/div[3]/ul/li')
        for li in li_list:
            item = NetworkCrawlingItem()
            job_name = li.xpath('.//div[@class="info-primary"]/h3/a/div[1]/text()').extract_first()
            item['job_name'] = job_name
            detail_url = 'https://www.zhipin.com/'+li.xpath('//div[@calss="info-primary"]/h3/a/@href').extract_first()
            #对详情页发请求获取详情页的页面源码数据
            #手动请求的发送
            #请求传参
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})


