'''from selenium import webdriver
from time import sleep
import time
import aiohttp
import re                                           # 导包
import asyncio
import aiofiles

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'
                             'AppleWebKit/537.36 (KHTML,like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
job_title = []  # 工作名称
corporate_name = []  # 公司名称
Working_treatment = []   # 工作待遇
Place_of_work = []     # 工作地点
Education_requirements = []    # 学历要求
Job_requirements = []     # 工作要求

sem = asyncio.Semaphore(1000)
async def main_task(url):
    with(await sem):
        async with aiohttp.ClientSession(headers=headers) as session:
            async with await session.get(url,timeout=650) as response:
                reponse = await response.text(encoding='utf-8')
                job_title = re.compile(r'',re.S)
                corporate_name =
                result = reguler.findall(reponse)


def main(url_list):
    loop = asyncio.get_event_loop()  # 获取事件循环
    tasks = [main_task(url) for url in url_list]  # 把所有任务放到一个列表中
    loop.run_until_complete(asyncio.wait(tasks))  # 激活协程
    loop.close()  # 关闭事件循环
'''
