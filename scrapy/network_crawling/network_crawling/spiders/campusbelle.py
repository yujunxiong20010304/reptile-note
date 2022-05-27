import scrapy
#全站数据爬取  校花网

class CampusBelleSpider(scrapy.Spider):
    name = 'campus_belle'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.521609.com/meinvxiaohua/']

    #生程一个url模版（不可变）
    url = 'http://www.521609.com/meinvxiaohua/list12%s.html'.format()
    page_num = 2

    def parse(self, response):
        li_list = response.xpath('/html/body/div[4]/div[2]/div[2]/ul/li')
        for li in li_list:
            img_name = li.xpath('./a[2]//text()').extract_first()
            print(img_name)
        if self.page_num<=4:
            new_url = format(self.url%self.page_num)
            self.page_num += 1
            #手动发送请求:callback函数回调用于数据解析
            yield scrapy.Request(url=new_url,callback=self.parse)
