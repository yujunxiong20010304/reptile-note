import asyncio
import time

async def request(url):
    print('正在下载',url)
    #在异步协程中如果出现同步模块相关代码，那么就无法实现异步
    #time.sleep(2)这是同步模块代码
    #当在asyncio中遇到阻塞操作必须进行手动挂起
    await asyncio.sleep(2)
    print('下载完毕',url)

start= time.time()
urls = ['www.baidu.com',
    'www.sougou.com',
    'www.goubanjia.com']


#任务列表：存放多个任务对象
stasks = []
for url in urls:
    c = request(url)
    task = asyncio.ensure_future(c)
    stasks.append(task)
#需要将任务列表封装到wait中
loop = asyncio.get_event_loop()#事件循环
#asyncio.wait(stasks) 固定格式写法
#需要将任务列表封装到wait中
loop.run_until_complete(asyncio.wait(stasks))#协程对象  协程对象注射到事件循环中
print(time.time()-start)
