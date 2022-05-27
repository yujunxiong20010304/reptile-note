#模拟登陆12306
'''
    使用selenium打开登陆界面
    对当前selenium打开的这张页面进行截图
    对当前局部（验证码）区域进行截图
        可以将验证码图片和模拟登陆一一对应
    使用超级鹰识别验证码图片
'''
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ChromeOptions
from PIL import Image#图片裁剪的包
from selenium.webdriver import ActionChains#动作链


#超级鹰模块
#!/usr/bin/env python
# coding:utf-8
import requests
from hashlib import md5
class Chaojiying_Client(object):

    def __init__(self, username, password, soft_id):
        self.username = username
        password =  password.encode('utf8')
        self.password = md5(password).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }

    def PostPic(self, im, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files, headers=self.headers)
        return r.json()

    def ReportError(self, im_id):
        """
        im_id:报错题目的图片ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        return r.json()

#-----------------------------------------------------------------------------------------------------------------------
#无头规避
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
#-----------------------------------------------------------------------------------------------------------------------
#实例化页面
url = 'https://kyfw.12306.cn/otn/resources/login.html'
browser = webdriver.Chrome()#chrome_options=chrome_options,options=option
browser.get(url)

btn = browser.find_element_by_xpath('/html/body/div[2]/div[2]/ul/li[2]/a')

btn.click()



#浏览器页面最大化显示
browser.set_window_position(0, 0)
browser.set_window_size(1280, 925)
#有利于之后截图


#整张页面进行截图
#browser.save_screenshot 将当前页面进行截图
browser.save_screenshot('12306.png')

#确定验证码左上角和右下角的坐标
browser.maximize_window()
code_img_ele = browser.find_element_by_xpath('//*[@id="J-loginImg"]')#定位验证码所在的标签
location = code_img_ele.location  #返回验证码左上角的坐标x，y  字典
size = code_img_ele.size  #验证码标签对应的长和宽  字典
#左上角坐标和右下角坐标
rangle = (int(location['x'])*2,int(location['y'])*2,int(location['x']+size['width'])*2,int(location['y']+size['height'])*2)

#开始对图片进行截图  需要包from PIL import Image
i = Image.open('12306.png')
code_img_name = 'code.png'
#crop根据指定区域进行裁剪
frame = i.crop(rangle)
frame.save(code_img_name)


#超级鹰进行图片解析
chaojiying = Chaojiying_Client('20302030426', 'yjx20010304', '916273')
im = open('code.png', 'rb').read()
result = chaojiying.PostPic(im, 9004)['pic_str']

#判断坐标的所在
str_two = result.split('|')
list_two = []
count = len(str_two)
for i in range(count):
    list = []
    number = str_two[i].split(',')
    list.append(int(number[0]))
    list.append(int(number[1]))
    list_two.append(list)
#遍历列表 ，使用动作链对每一个元素对应的x，y指定的位置进行点击操作
for l in list_two:
    x = l[0]/2#这儿要除去之前乘的数，不然无法点击准确
    y = l[1]/2
    print(x,y)
    ActionChains(browser).move_to_element_with_offset(code_img_ele,x,y).click().perform()
#   move_to_element_with_offset(code_img,x,y) 的作用将我们点击的这个参照物移动到指定的element当中
#   code_img_ele 之前定位的验证码的标签
sleep(5)

#登陆
account_number = browser.find_element_by_xpath('//*[@id="J-userName"]')
account_number.send_keys('xxxxxxxxx')

password = browser.find_element_by_xpath('//*[@id="J-password"]')
password.send_keys('xxxxxxxxxx')

btn = browser.find_element_by_xpath('//*[@id="J-login"]')
btn.click()



browser.quit()
