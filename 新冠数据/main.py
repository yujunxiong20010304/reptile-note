#import spider
from spider import Spider

#主程序

def main():
    # headers
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
    }
    #构建一级网址列表
    page_url = ['http://wsjkw.sc.gov.cn/scwsjkw/gzbd01/ztwzlmgl.shtml',
                'http://wsjkw.sc.gov.cn/scwsjkw/gzbd01/ztwzlmgl_2.shtml',
                'http://wsjkw.sc.gov.cn/scwsjkw/gzbd01/ztwzlmgl_3.shtml',
                'http://wsjkw.sc.gov.cn/scwsjkw/gzbd01/ztwzlmgl_4.shtml',
                'http://wsjkw.sc.gov.cn/scwsjkw/gzbd01/ztwzlmgl_5.shtml',
                'http://wsjkw.sc.gov.cn/scwsjkw/gzbd01/ztwzlmgl_6.shtml',
                'http://wsjkw.sc.gov.cn/scwsjkw/gzbd01/ztwzlmgl_7.shtml',
                'http://wsjkw.sc.gov.cn/scwsjkw/gzbd01/ztwzlmgl_8.shtml',
                'http://wsjkw.sc.gov.cn/scwsjkw/gzbd01/ztwzlmgl_9.shtml',
                'http://wsjkw.sc.gov.cn/scwsjkw/gzbd01/ztwzlmgl_10.shtml',
                'http://wsjkw.sc.gov.cn/scwsjkw/gzbd01/ztwzlmgl_11.shtml']
    # 实例化爬虫类
    all_data={}
    pys=Spider(headers)
    all_herf_content = []
    # 链接网址
    all_herf_link = []
    # 日期
    all_data_time = []
    # 数据
    all_data=[]
    #逐个访问一级网址列表
    for i in page_url:
        #获得网页源代码
        html_code=pys.get_html_source(i,headers)
        #当前一级网址返回的网址列表、日期、文本内容
        herf_link, data_time, herf_content=pys.get_content_url(html_code)
        all_herf_link.append(herf_link)
        all_data_time.append(data_time)
        all_herf_content.append(herf_content)

        #从二级网址中解析HTML源代码，提取相关数据
        #思路一：处理一级网址列表的同时解析二级网址源码
        #逐个处理当前一级网页返回的二级网址列表
        for link,time in zip(herf_link,data_time):
            #访问二级网址，返回HTML代码
            html2=pys.get_html_source(link,headers)
            #调用获取数据的方法
            all_data.append(pys.get_data_info(html2,time))
    print(all_data)
    pys.get_into_excel(all_data)
        #思路二：处理完一级网址列表之后，解析二级网址源码






if __name__ == '__main__':
    main()
