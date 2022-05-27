import requests
import aiohttp#基于异步请求的网络模块
import asyncio
import time
start = time.time()
urls = ['http://127.0.0.1:5000/bobo','http://127.0.0.1:5000/jay','http://127.0.0.1:5000/tom']

async def get_page(url):
    #-------------------------------------------------------------------------------------------------------------------
    ''' print('正在下载',url)
    #requests.get发送的请求是基于同步的,
    #⚠！！！！aiohttp：基于异步网络请求的模块️
    response = requests.get(url=url)#这是一个同步代码
    print('下载完毕',response.text)'''
    #-------------------------------------------------------------------------------------------------------------------
    #注意在获取响应 session.get(url) 和获取响应数据 response.text() 时，前面要加个 await 来进行手动挂起！！！！！！！！！
    async with aiohttp.ClientSession() as session:
        #get()和post()方法和之前使用一样
        #参数：headers，parmars/data,proxy=''是字符串了
        async with await session.get(url) as response:    #和之前模拟登陆类型不一样，但用法一样
            #text()返回的是字符串形式的响应数据
            #read()返回的是二进制形式的响应数据
            #json()返回的就是json对象
            page_text = await response.text()
            print(page_text)
tasks = []
for url in urls:
    c = get_page(url)#因为函数get_page被async修饰了，所以调用后会返回一个对象
    task = asyncio.ensure_future(c)#协程对象封装到任务对象中
    tasks.append(task)#把任务对象添加到任务列表
loop = asyncio.get_event_loop()#创建一个循环对象
loop.run_until_complete(asyncio.wait(tasks))#多任务列表的注入
print(time.time()-start)



