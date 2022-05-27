# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class StudyPipeline:
    fp = None
    #重写一个父类的方法
    def open_spider(self,spider):#该方法只会在开始爬虫的时候调用一次
        print('开始爬虫')
        self.fp = open('./qiubai.txt','w',encoding='utf-8')
    #该方法可以接受爬虫文件提交过来的item对象
    #专门用来处理item类型对象
    #该方法每接受一个item就会被调用一次
    def process_item(self, item, spider):
        end = item['end']
        #持久化存储
        self.fp.write(end)
        return item #会被传递给下一个将要被执行的管道类
    #这个方法只会在爬虫结束时调用一次
    def close_spider(self,spider):
        print('结束爬虫')
        self.fp.close()


import pymysql #导入连接数据库的包
#在管道文件中一个管道类对应将一组数据存储到一个平台或者载体中
#虽然在这儿自定义了，但需要进入settings去开启
class mysqlPileLine(object):
    conn = None
    cursor = None #游标对象
    def open_spider(self,spider):
        self.conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='yjx20010304',database='数据库名',charset='utf8')
    def process_item(self,item,spider):
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute('')#这里面写sql语句
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        return item
    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()



