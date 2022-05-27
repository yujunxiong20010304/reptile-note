#针对淘宝
from selenium import webdriver  #selenium 模块导包
from lxml import etree
from time import sleep
broweser = webdriver.Chrome()
broweser.get('https://www.taobao.com/')


#（标签id定位），在这里面还有其他类型自己去了解
search_input = broweser.find_element_by_id('q')
#标签交互
search_input.send_keys('Iphone')

#执行一组js程序
broweser.execute_script('window.scrollTo(0,document.body.scrollHeight)')#控制浏览器屏幕向下滑动

sleep(4)

#点击搜索按钮
btn = broweser.find_element_by_xpath('//*[@id="J_TSearchForm"]/div[1]/button')
btn.click()#点击事件
sleep(2)
broweser.get('https://www.baidu.com')
sleep(2)
broweser.back() #回退
sleep(2)
broweser.forward()  #前进


sleep(5)
broweser.quit()





'''
#-----------------------------------------------------------------------------------------------------------------------
find_element_by_id // 通过id查找单个元素
find_element_by_name // 通过name查找单个元素
find_element_by_xpath // 通过xpath查找单个元素
find_element_by_link_text // 通过链接查找单个元素
find_element_by_partial_link_text // 通过部分链接查找单个元素
find_element_by_tag_name // 通过标签名称查找单个元素
find_element_by_class_name // 通过类名查找单个元素
find_element_by_css_selector // 通过css选择武器查找单个元素
find_elements_by_name // 通过name查找多个元素
find_elements_by_xpath // 通过xpath查找多个元素
find_elements_by_link_text // 通过链接查找多个元素
find_elements_by_partial_link_text // 通过部分链接查找多个元素
find_elements_by_tag_name // 通过标签名称查找多个元素
find_elements_by_class_name // 通过类名查找多个元素
find_elements_by_css_selector // 通过css选择武器查找多个元素
#-----------------------------------------------------------------------------------------------------------------------
'''
