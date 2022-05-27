#单线程+异步协程
import asyncio
#-----------------------------------------------------------------------------------------------------------------------
async def request(url):
    print('正在请求的url是：',url)
    print('请求成功',url)
    return url
c = request('www.baidu.com')
#在这儿用async修饰后去调用这个函数会返回一个协程对象,需要把协程对象放到事件循环对象中
#-----------------------------------------------------------------------------------------------------------------------
'''
#创建一个事件循环对象
loop = asyncio.get_event_loop()

#将协程对象注册到loop中，然后启动loop
loop.run_until_complete(c)#这个函数既可以实现注册又可以实现启动事件循环'''
#-----------------------------------------------------------------------------------------------------------------------

'''#task的使用
loop = asyncio.get_event_loop()
#基于loop创建来一个task对象
task = loop.create_task(c)
print(task)#显示的结果是未执行成功的
loop.run_until_complete(task)
print(task)#显示的结果是执行成功的'''
#-----------------------------------------------------------------------------------------------------------------------
'''#future的使用
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(c)
print(task)#显示的结果是未执行成功的
loop.run_until_complete(task)
print(task)#显示的结果是执行成功的'''

#-----------------------------------------------------------------------------------------------------------------------

#回调函数
def callback_func(task):
    #result返回的就是任务对象中封装的协程对象对应函数的返回值
    print(task.result())
#这个函数的传参是默认的

#绑定回调
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(c)
#将回调函数绑定到任务对象中
task.add_done_callback(callback_func)
loop.run_until_complete(task)
