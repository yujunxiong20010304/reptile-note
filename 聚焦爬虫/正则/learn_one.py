#爬取图片
#xpath 和 bs4只能解析标签
import requests
'''text(字符串)   content(二进制)  josn()(对象)'''
if __name__ == '__main__':
    #如何爬取图片数据
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
    url = 'https://pic.qiushibaike.com/system/pictures/12428/124284609/medium/FF503J7FDUCXJAJ3.jpg'
    img = requests.get(url = url,headers = headers)
    img_one = img.content#二进制形式的图片数据
    print(img_one)
    with open('/Users/yujunxiong/Desktop/1/tu.jpg','wb') as file:#因为是content所以是一个二进制文件，就是wb
        file.write(img_one)
    print('存储成功')
