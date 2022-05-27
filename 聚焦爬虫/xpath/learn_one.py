'''
xpath原理  基础
1。实例化一个etree的对象，且需要将被解析的页面源码数据加载到该数据中
2。调用etree对象中xpath方法结合着xpath表达式实现标签的定位和内容的捕获
------------------------------------------------------------------------------------------------------------------------
如何实例化一个etree对象： from lxml import etree
1。将本地的html文档中的源码数据加载到etree对象中
    etree.parse(filepath)    filepath是本地的html文件存储路径
2。可以将从互联网上获取的源码数据加载到该对象中
    etree.HTML('page_text')    page_text是从互联网中获取的响应数据
    xpath('xpath表达式')
3。xpath表达式
    例子：
        tree = etree.parse('html文件')
        r = tree.xpath('/html/head/title') 从/(根节点)->html->head->title
        print(r)  返回的是一个列表，里面是一个element类型的对象，

    例子：
        tree = etree.parse('html文件')
        r = tree.xpath('/html/body/div')《=》r = tree.xpath('/html//div')《=》r = tree.xpath('//div')
        print(r)    #假如说body中有多个div，那么r中是一个列表存储这多个element的对象
        / ： 表示从根节点开始的定位。表示的是一个层级
        //：表示多个层级。表示从任意位置开始定位

    属性定位：
        r = tree.xpath('//div[@class="属性名称"]')   属性定位class为某名称的div
        xpath 返回的永远是一个列表
        假如像class可以有多个属性名，要定位他，只有把全部属性名写出来

    索引定位
        r = tree.xpath('//div[@class="属性名称"]/p[3]')   拿到这个属性名称的div中第三个p标签（索引的下标是从1开始的）
        索引定位这里也可以用id

    取文本
        r = tree.xpath('//div[@class="属性名称"]//li[5]/a/text()')   text()取文本，并且只能取直系（也就是不能取子代的文本）
        r = tree.xpath('//div[@class="属性名称"]//li[5]/a//text()')   因为text()前面是//，所以可以取到子代的文本信息
        print(r)  结果是一个列表，存储这文本信息

    取属性
        r = tree.xpath('//div[@class="属性名称"]/img/@src')   取到了img中属性src的值

    警告⚠！！！！！️
        例子：
            li_list = tree.xpath('//ul[@class="house-list-wrap"]/li')
            for wli in li_list:
                wli.xpath('./div[2]/h2/a/text()')
        这是是在学习视频中的一个例子，首先从 //ul[@class="house-list-wrap"]/li 定位到许多的li标签，保存在li_list中，
        然后对他进行了一个遍历，其实这个就和路径擦不多，一种是绝对路径，一种是相对路径。参照物变了
        最重要的是你知道li_list的含义嘛，他是一群拥有相同父亲的子级


    ⚠️运算符：
        例子：
            r = tree.xpath('//div[@class="属性名称"]/img/@src | //div[@class="属性名称"]//li[5]/a//text()')
        xpath可以使用｜这个运算符，来进行或者匹配

    ⚠️ ：
        当你去取一个拥有相同属性名的子类群体时，不能把属性名带上
'''
