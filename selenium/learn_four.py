from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains #导入动作链对应的类

browser = webdriver.Chrome()
browser.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
#如果想要定位的标签是存在在 iframe 标签之中，那么用find类型的方法是定位不到的，则需要进行如下操作进行标签定位
browser.switch_to.frame('iframeResult')    #这儿的 iframeResult 是ifarme 标签的id
#browser.switch_to.frame('iframeResult') 的作用，切换浏览器标签定位的作用域
div = browser.find_element_by_xpath('//*[@id="draggable"]')

#动作链
action = ActionChains(browser)#动作链实例化
#点击长按指定的标签
action.click_and_hold(div)

for i in range(5):
    #perform()立即执行动作链操作
    action.move_by_offset(17,0).perform()#移动偏移像素  传入一个参数x，一个参数y
    sleep(0.3)
    action.release()    #释放动作链
browser.quit();
