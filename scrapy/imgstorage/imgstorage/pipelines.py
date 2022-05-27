# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


'''class ImgstoragePipeline:
    def process_item(self, item, spider):
        return item'''
import scrapy
from scrapy.pipelines.images import ImagesPipeline
class imagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):#就是根据图片地址的数据请求
        yield scrapy.Request(url=item['src'],)

    def file_path(self, request, response=None, info=None, *, item=None):#定制图片名称
        url = request.url
        file_name = url.split('/')[-1]
        return file_name

#图片存储的目录在settings文件中指明

    def item_completed(self, results, item, info):
        return item #该返回值传递给下一个将要被执行的管道类

