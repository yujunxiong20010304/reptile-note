import threading
import queue
from 项目 import content
# 生产者
def readfile(q):
    list_url = []
    with open('webesite.txt','r',encoding='utf-8') as file_name:
        while True:
            url = file_name.readline()
            url = eval(url.strip('\n'))
            url = url[0]
            list_url.append(url)
            if len(list_url)>10000:
                q.put(list_url)
                list_url = []
        q.put(None)
        q.task_done()

def usefile(q):
    while True:
        url_list = q.get()
        if url_list==None:
            break
        print(url_list)
        content.main(url_list)
    q.task_done()


if __name__ == '__main__':
    q = queue.Queue(100)

    #创建生产者
    th = threading.Thread(target=readfile,args=(q,))
    th.start()

    #创建消费者
    tc = threading.Thread(target=usefile,args=(q,))
    tc.start()
    th.join()
    tc.join()



