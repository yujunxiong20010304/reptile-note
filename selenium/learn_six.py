#谷歌无头浏览器加反检测
from selenium import webdriver
from time import sleep
#-----------------------------------------------------------------------------------------------------------------------
#！！！！！！！！！！！！！！！！！
#让程序运行后不会弹出浏览器（无头浏览器）
from selenium.webdriver.chrome.options import Options  #无头浏览器需要导入的包
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

#-----------------------------------------------------------------------------------------------------------------------

#如何实现让selenium规避被检测到的风险
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
from selenium.webdriver import ChromeOptions   #实现让selenium规避被检测到的风险的类
option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])

#-----------------------------------------------------------------------------------------------------------------------

url = 'https://www.baidu.com/'
browser = webdriver.Chrome(chrome_options=chrome_options,options=option)
#
#chrome_options=chrome_options   options=option  ,这两个参数的值来自前面的规避和无头
#
browser.get(url)
print(browser.page_source)
browser.quit()

