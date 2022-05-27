'''
selenium模块的基本使用
selenium模块和爬虫的关联
    1。便捷获取网站中动态加载的数据
    2。便捷实现模拟登陆
什么是selenium模块：
    基于浏览器自动化的一个模块
编写基于浏览器自动化的代码
    发起请求:get(url)
    标签定位:find系列方法
    标签交互:send_keys('xxx')
    执行js程序:excute_script('jsCode')
    前进，后退:back(),forward()
    关闭浏览器:quit()
selenium处理iframe：（滑动验证码的破解）
    如果定位的标签存在与iframe标签之中，则必须使用switch_to.frame(id)
    动作链（拖动）：from selenium.webdriver import ActionChains
        实例化一个动作链对象：action = ActionChains(bro)
        click_and_hold(div):长按div标签
        move_by_offset(x,y)标签偏移值
        perform()让动作链立即执行
        action.release()释放动作链对象
⚠️：
    要用selenium进行动态数据的全部爬取，需要控制滚轮的滑动，把下面的页面加载出来
'''
