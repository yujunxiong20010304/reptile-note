#selenium 项目案例
#模拟登陆qq空间
from selenium import webdriver  #selenium 模块导包
from lxml import etree
from time import sleep

url = 'https://i.qq.com'
browsesr = webdriver.Chrome()
browsesr.get(url)


browsesr.switch_to.frame('login_frame')
but = browsesr.find_element_by_xpath('/html/body/div[1]/div[9]/a[1]')
but.click()
sleep(4)

account_number = browsesr.find_element_by_xpath('/html/body/div[1]/div[5]/div/div[1]/div[3]/form/div[1]/div/input')
account_number.send_keys('2140585762')
sleep(2)

password = browsesr.find_element_by_xpath('/html/body/div[1]/div[5]/div/div[1]/div[3]/form/div[2]/div[1]/input')
password.send_keys('yjx20010304')
sleep(2)
login = browsesr.find_element_by_xpath('/html/body/div[1]/div[5]/div/div[1]/div[3]/form/div[4]/a/input')
login.click()
sleep(5)

browsesr.quit()
