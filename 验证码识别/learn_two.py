'''
识别古诗文网中的验证码
    1。验证码图片本地下载
    2。代码进行判断

'''
import requests
from lxml import etree
import tesserocr
from PIL import Image
import os
if __name__ == '__main__':
    if not os.path.exists('/Users/yujunxiong/Desktop/1'):
        os.mkdir('/Users/yujunxiong/Desktop/1')
    url = 'https://so.gushiwen.org/user/login.aspx'
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'
                            'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
    reponse = requests.get(url=url,headers=headers)
    reponse.encoding = reponse.apparent_encoding
    reponse_end = reponse.text
    tree = etree.HTML(reponse_end)
    captcha_image = tree.xpath('//*[@id="imgCode"]/@src')
    #⚠️ 这而的//*[@id="imgCode"]/@src，是从网站源码，右键copy，选择copyxpath获取的
    picture_address = 'https://so.gushiwen.org'+captcha_image[0]
    #发起新的请求
    picture_request = requests.get(url=picture_address,headers=headers).content
    file_name = '/Users/yujunxiong/Desktop/1/yanzhnema.gif'
    with open(file_name,'wb') as file:
        file.write(picture_request)
    #破解验证码
    image = Image.open('/Users/yujunxiong/Desktop/1/yanzhnema.gif')
    image.show()  # 可以打印出图片，供预览
    print(tesserocr.image_to_text(image))




