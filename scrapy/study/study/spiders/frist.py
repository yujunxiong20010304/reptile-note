import scrapy   #导入相关的包


class FristSpider(scrapy.Spider): #Spider是scrapy中的一个类，是scrapy中所有类的父类
    name = 'frist' #爬虫文件的名称：就是爬虫源文件的唯一标识
    #allowed_domains = ['www.baidu.com'] #允许的域名：用来限定start_urls 列表中哪些url可以进行请求的发送
    #通常allowed_domains不会使用，会被注释掉
    start_urls = ['http://www.baidu.com/','https://sogou.com'] #起始的uel列表：该列表中存放的url会被scrapy自动进行请求的发送，可以有多个网址

    #start_urls 中的网址，会自动发送请求，请求成功后会返回给response，相当于响应对象，然后用response进行解析就可以了

    def parse(self, response):#用作与数据解析：response参数表示的就是请求成功后对应的响应对象
        print(response)#打印出来很多东西，其中有执行日志
        #用命令scrapy crawl spiderName --nolog  可以不打印出日志，只打印执行结果 spiderName是爬虫名称,但是不会打印错误信息
