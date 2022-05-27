# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

from scrapy.http import HtmlResponse #篡改响应对象需要导入的包
from time import sleep



class WangyiproDownloaderMiddleware:


    def process_request(self, request, spider):

        return None

    # 通过该方法拦截五大响应对象对齐进行篡改
    def process_response(self, request, response, spider):  #spider表示爬虫对象
        browser = spider.browser#获取了在wangyi.py文件中定义的浏览器对象
        #挑选出指定的响应对象进行篡改
        #通过url指定request
        #通过request指定response
        if request.url in spider.models_urls:  #调用wangyi.py文件中的属性
            browser.get(request.url)  #五个板块对应的url进行请求发送
            sleep(2)
            page_text = browser.page_source  #包含了动态加载的新闻数据
            #五大板块对应的响应对象
            #针对定位到的response进行篡改
            #实例化一个新的响应对象（符合需求：有动态加载数据），再将新的替换原来旧的
            #如何获取新的动态加载的数据
                #基于selenium便捷的获取动态加载的数据     可以把selenium程序写在爬虫文件中
            new_response = HtmlResponse(url=request.url,body=page_text,encoding='utf-8',request=request)
            #body 是新的响应数据     url响应对象对应请求对象的url

            return new_response
        else:
            return response   #其他请求对应的响应对象


        return response

    def process_exception(self, request, exception, spider):

        pass

