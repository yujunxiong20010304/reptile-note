from selenium import webdriver  #selenium 模块导包
from lxml import etree
from time import sleep
#实例化一个浏览器对象（传入浏览器驱动程序）
browser=webdriver.Chrome()
#让浏览器发起一个指定url对应请求
browser.get('http://scxk.nmpa.gov.cn:81/xk/')#就会打开浏览器

#获取当前浏览器页面源码数据
page_text = browser.page_source  #返回页面源码数据
#解析页面源码数据
tree = etree.HTML(page_text)
li_list = tree.xpath('//*[@id="gzlist"]/li')
for li in li_list:
    name = li.xpath('./dl/@title')
    print(name)
sleep(2)
browser.quit()#关闭浏览器

