# 性能测试  运行方式 locust -f 脚本名
from locust import HttpUser,TaskSet,task
from locust.clients import HttpSession
import re

# 性能测试实验
#测试51setting网站首页
class UserBehavior(TaskSet):
    # 任务标签
    @task
    def text_index(self):  # 要访问的功能
        # /html/index.html 子页面
        # response = self.client.get('/html/index.html') 等价与=》response = requests.get(url = url,headers=headers)
        response = self.client.get('/')
        response.encoding = response.apparent_encoding
        response = response.text
        print(response)
class WebSiteUser(HttpUser): # 要访问的公共参数
    #设置被测网站的域名
    host = "https://www.baidu.com/"  # 主机域名
    #设置性能测试任务类
    task_set = UserBehavior
    #设置等待的时间区间
    min_wait = 2000
    max_wait = 5000

