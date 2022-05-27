from selenium import webdriver
from time import sleep
import time
import aiohttp
import re                                           # 导包
from 项目 import parameter_one
import asyncio
import aiofiles
# ======================================================================================================================
def give_cookie():  # 获取cookie的函数
    browser = webdriver.Chrome()
    browser.get('https://i.zhaopin.com/')
    sleep(40)
    cookieh = browser.get_cookies()# 获取cookie
    browser.quit()
    cookies = {}
    for link in cookieh:
        for key in link.keys():
            if key=='expiry':
                now = int(time.time()+1000000)
                link['expiry'] = now
        cookies[link['name']] = link['value']
    return cookies
# ======================================================================================================================
title_data = parameter_one.address() # url 的地址参数
words_data = parameter_one.work()  # url 的工作参数
urls = parameter_one.merge(title_data, words_data) #url的粗模版
urls = list(set(urls))
cookie = give_cookie()  # 调用give_cookie()函数获取cookie
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'
                             'AppleWebKit/537.36 (KHTML,like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
# ======================================================================================================================
sem = asyncio.Semaphore(5) # 信号量，控制协程数，防止爬的过快
async def main_task(ur):
    i = 1
    with(await sem):
        while True:
            url = ur + str(i)
            async with aiohttp.ClientSession(cookies=cookie, headers=headers) as session:
                async with await session.get(url,timeout=650) as response:
                    reponse = await response.text(encoding='utf-8')
                    reguler = re.compile(
                        r'<a href="http://jobs\.zhaopin\.com(.*?)" target="_blank" class="joblist-box__iteminfo iteminfo">',
                        re.S)
                    result = reguler.findall(reponse)
                    if result == []:
                        break
                    else:
                      '''  for u in result:
                            Details_page = []
                            last_url = 'https://jobs.zhaopin.com' + u
                            Details_page.append(last_url)
                            async with aiofiles.open('webesite.txt','a',encoding='utf-8') as file_name:
                                await file_name.write(str(Details_page)+'\n')
                        print(url,result)
                        i += 1'''


# ======================================================================================================================
def main():
    loop = asyncio.get_event_loop()  # 获取事件循环
    tasks = [main_task(ur) for ur in urls]  # 把所有任务放到一个列表中
    loop.run_until_complete(asyncio.wait(tasks)) # 激活协程
    loop.close()  # 关闭事件循环



if __name__ == '__main__':
    main()
