#爬虫类
import re
import requests
from bs4 import BeautifulSoup
import xlwings as xw

class Spider():
    #定义构造方法
    def __init__(self,headers):
        self.headers=headers

    # 访问网址，返回HTML源代码
    def get_html_source(self,url,headers):
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            # print(response.text)
            html_code = response.content.decode('utf-8')
            # print(type(html_code))
            # print(html_code)
            return html_code
        else:
            print("获取网站源码出错........")

    # 解析HTML源代码，返回二级网址列表
    def get_content_url(self,html):
        url_head = "http://wsjkw.sc.gov.cn/scwsjkw/gzbd01/"
        # 定义正则表达式匹配模型
        pattern = re.compile(r'<a href="/scwsjkw/gzbd01/(.*?)" target="_blank"  >(.*?)</a>', re.S)
        # 在html网页中查找所有匹配的值
        reg_text = pattern.findall(html)
        #  print(reg_text)
        # 链接内容
        herf_content = []
        # 链接网址
        herf_link = []
        # 日期
        data_time = []
        for i in reg_text:
            # 将提取的网址信息进行字符串连接
            i_str = "".join(i[0])
            # 在网址信息中提取年月日信息，并追加到列表
            data_time.append(i_str.split("/", 3)[0] + "年" + i_str.split("/", 3)[1] + "月" + i_str.split("/", 3)[2] + "日")
            # 拼接生成网址
            herf_link.append(url_head + i[0])
            # 提取文字内容
            herf_content.append(i[1])
        return herf_link, data_time, herf_content

    # 解析二级网址HTML源代码，返回获取数据
    def get_data_info(self,html,time):
        #技术点Beautifulsoup 正则表达式
        all_data={}
        # 格式化|结构化HTMl代码
        # 返回的数据要求
        # 日期：2021年5月10日
        # 新增：3
        # 死亡：
        # 治愈：
        # 累计：
        all_data['日期']=time
        # 格式化HMTL，以lxml的格式
        soup = BeautifulSoup(html, 'lxml')
        # 在格式化以后的代码中去确定要查找的范围，并返回相应的文本
        news = soup.find("div", class_="wy_contMain fontSt").get_text()
        # 新增确诊的表述列表，即在网页中可能存在的新增的表述
        list_xz = ['累计治愈出院(\d+)例']
        all_data['治愈']=self.get_re_count(list_xz,news)

        return all_data

    def get_re_count(self,list,news):
        global count
        for i in list:
            result=re.search(i,news)
            if result!=None:
                count=result.group(1)
                break
            else:
                count=0
        return count
    def get_into_excel(self,data_list):
        app = xw.App(visible=False, add_book=False)  # 程序可见，只打开不新建工作薄
        app.display_alerts = False  # 警告关闭
        app.screen_updating = False  # 屏幕更新关闭
        wb=app.books.open('新冠.xlsx')
        wk = wb.sheets['Sheet1']
        sheet = wb.sheets[0]
        info = sheet.used_range
        max_row = info.last_cell.row
        #max_row=wk.api.used_range.rows.count
        #max_row = wk.api.UsedRange.Rows.Count
        if max_row==1:
            wk.range('A1').value=list(data_list[0].keys())
            max_row=2
        else:
            max_row=max_row+1
        for i in range(len(data_list)):
            wk.range('A'+str(i+max_row)).value=list(data_list[i].values())

        wb.save()
        wb.close()
        app.quit()






