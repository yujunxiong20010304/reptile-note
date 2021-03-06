'''正则几乎使用所有的语言
而bs4和xpath只适合python
bs4数据解析原理：
1。实例化一个BeautifulSoupd对象，并且将页面源码数据加载到该对象中
2。通过调用BeautifulSoup对象中相关的属性或者方法进行标签定位和数据提取

对象的实例化：
1。将本地的html文档中的数据加载到该对象中
from bf4 import BeautifulSoup
if__name == '__main__':
    file = open('文件名.html','r',encoding='utf-8')
    soup = BeautifulSoup(file,'lxml')        这儿的参数二，是统一固定的
    print(soup)#打印出来的结果是文件中的内容
    --------------------------------------------------------------------------------------------------------------------
    print(soup.tagName)打印出来的结果是文件中第一次出现的tagName标签,tagName是标签名，如a,div...
    print(soup.tagName)<==>print(soup.find('tagName'))
    --------------------------------------------------------------------------------------------------------------------
    属性定位
        print(soup.find('tagName',class_或者 id 或者 atter ='属性名'))
        print(soup.find_all('tagName')) 找出页面中所有名称为tagName的标签，返回的是一个列表
    --------------------------------------------------------------------------------------------------------------------
    层级选择器
        print(soup.select('某种选择器(id,class,标签)'))，返回的是一个列表，这儿的某种选择器就像你在写css时候的那个
        print(soup.select('.ol>.li>a'))返回的是一个列表
        print(soup.select('.ol a'))返回的是一个列表，空格标示多个层级，>号表示一个层级
    --------------------------------------------------------------------------------------------------------------------
    获取标签之间的文本数据
          soup.a.(text/string/get_text())  a是a标签
          text/get_text()可以获取某一个标签中所有的文本内容（意思是标签的子代文本内容也可以获取）
          string 只能获取属于该标签的文本内容
    --------------------------------------------------------------------------------------------------------------------
    获取标签中的属性值
        soup.a['属性值']  例如soup.img['src']  这样就可以获取img标签的图片链接
    --------------------------------------------------------------------------------------------------------------------
2。将互联网上获取的源码数据加载到该对象中
page_text = requests.text
soup = BeautifulSoup(page_text,'lxml')
'''





