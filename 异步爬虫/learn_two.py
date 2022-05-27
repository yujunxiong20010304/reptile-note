#-----------------------------------------------------------------------------------------------------------------------
'''
#单线程串行方式进行
import time
def get_page(str):
    print('正在下载',str)
    time.sleep(2)
    print('下载成功',str)
name_list = ['aa','bb','cc','dd']
start_time = time.time()
for i in range(len(name_list)):
    get_page(name_list[i])
end_time = time.time()
print('%d scond' % (end_time-start_time))
'''
#-----------------------------------------------------------------------------------------------------------------------

#单线程池方式进行
from multiprocessing.dummy import Pool #导入线程池需要的类
import time
start_time = time.time()
def get_page(str):
    print('正在下载',str)
    time.sleep(2)
    print('下载成功',str)
name_list = ['aa','bb','cc','dd']
#实例化一个线程池对象
pool = Pool(4)
#将列表中每一个列表元素传递给get_page进行处理
pool.map(get_page,name_list)
end_time = time.time()
print('%d second' % (end_time-start_time))
