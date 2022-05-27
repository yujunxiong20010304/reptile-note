# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class SunproPipeline:
    def process_item(self, item, spider):
        #当items.py文件中有多个类时，判断item是那个类的
        if item.__class__.__name__ == 'DetailItem':   #item.__class__.__name__  判断item的所属类的名字
            print(item['detail'])
        else:
            print(item['photot_name'])
        return item
'''
实例调用__class__属性时会指向该实例对应的类
__name__就是用来标识模块的名字的一个系统变量。
简单的讲：就是用来区分是主模块，还是被导入模块。
它具有两个作用：
1、如果模块是被导入，那么被导入模块中__name__属性值就为模块名字。
2、如果模块是被直接执行（即为主模块），__name__的值为“__main __”。
'''
