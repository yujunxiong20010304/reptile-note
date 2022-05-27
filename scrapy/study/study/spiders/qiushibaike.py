#解析糗事百科作者的名称和段子内容，并且是用基于终端指令来进行的存储
import scrapy


class QiushibaikeSpider(scrapy.Spider):
    name = 'qiushibaike'
    #allowed_domains = ['www.baidu.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    def parse(self, response):
        #在scrapy中是不需要获取响应数据的
        div_list = response.xpath('//*[@id="content"]/div/div[2]/div')
        all_data = []#作用：存储所有解析到的数据
        for div in div_list:
            end = div.xpath('./a/div/span//text()').extract()
            end = ''.join(end)
            dic = {
                'end' : end
            }
            all_data.append(dic)
        return all_data
             #extract()可以将Selector对象中data参数存储的字符串提取出来
        '''不管是谁调用了extract之后，则表示将列表中每一个Selector对象中data对应的字符串提取了出来
            xpath返回结果是一个列表，而这个列表中存储的是许多的Selector对象，所以对他使用后可以将
            data中的字符串提取出来'''



