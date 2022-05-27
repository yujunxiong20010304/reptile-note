'''
模拟登陆 人人网
    爬取用户的相关信息
    点击登陆按钮后会发起一个post请求
    post请求会携带登陆的相关信息（账号，密码）
    验证码每次请求都会变化，要把它作为post请求中的一个参数
    验证码和post请求一一对应
'''
"""
编码流程
1。验证码的识别，获取验证码图片文字数据
2。对post发送请求（处理请求参数）
3。对响应数据持久化存储
"""
import requests
from lxml import etree
if __name__ == '__main__':
#-----------------------------------------------------------------------------------------------------------------------
    #创建session对象
    session = requests.Session()
#-----------------------------------------------------------------------------------------------------------------------
    # #1.对验证码图片捕获并识别
    url = 'http://www.renren.com/SysHome.do'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'
                             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
    reponse = requests.get(url=url,headers=headers)
    reponse.encoding = reponse.apparent_encoding
    reponse = reponse.text
    tree = etree.HTML(reponse)
    code_img_src = tree.xpath('//*[@id="verifyPic_login"]/@src')[0]
    code_img_data = requests.get(url=code_img_src,headers=headers).content
    with open('./code.png','wb') as file:
        file.write(code_img_data)
    #post请求模拟登陆
    login_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2021431534400'
    deta = {
            'email': '13440069172',
            'icode': '',
            'origURL': 'http://www.renren.com/home',
            'domain': 'renren.com',
            'key_id': '1',
            'captcha_type':' web_login',
            'password': '8e1d37c88288ed6ef74bcf58c219cceac43dbe2ae6572a6028302842aa0d7042',
            'rkey': '522bdbecfea25d5355f5c15181dcce88',
            'f': 'http%3A%2F%2Fwww.renren.com%2F976768531%2Fnewsfeed%2Fphoto'
    }
#-----------------------------------------------------------------------------------------------------------------------
    #使用session进行post请求发送   请求成功后产生的cookie会自动保存到session当中
    login_page_text = session.post(url=login_url,headers=headers,data=deta)
    print(login_page_text)
#-----------------------------------------------------------------------------------------------------------------------
    '''拿到的响应数据是不确定的，由后台来设置的
    ，这儿的post响应数据的结果是登陆人人网成功后的网址'''
    #response.status_code == 200来判断是否响应成功
    #服务器并没有存储我的登陆状态，意思是并不知道我已经登陆了
#-----------------------------------------------------------------------------------------------------------------------
    #爬取当前对应的个人用户页面
    detail_url = 'http://www.renren.com/976768531/profile'
    detail_page_text = session.get(url = detail_url,headers=headers)
#-----------------------------------------------------------------------------------------------------------------------
    detail_page_text.encoding = detail_page_text.apparent_encoding
    detail_page_text = detail_page_text.text
    with open('biubiu.html','w',encoding='utf-8') as file:
        file.write(detail_page_text)

















