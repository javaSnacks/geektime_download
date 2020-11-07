#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
# idea中需要安装webdriver-manager
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
# 起始页面地址
driver.get("https://time.geekbang.org/column/article/74988")
print (0)
time.sleep(2)
elem = driver.find_element_by_class_name("_3d13BJVh_0")
elem.click()
time.sleep(2)
print (1)
elem = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[3]/a")
elem.click()
print (2)
time.sleep(2)
elem = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[1]/div[1]/input")
# elem.send_keys("17153185244")
# 通过手机号密码登陆，输入你的手机号
elem.send_keys("16532701597")
print (3)
time.sleep(2)
elem = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[2]/input")
# elem.send_keys("wybq1234")
# 输入你的密码
elem.send_keys("SXSDJKSJ1234")
print (4)
time.sleep(2)
elem = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/button")
elem.click()
print (5)
time.sleep(2)
i = 0
# 输入循环次数
while i < 70:
    # 1. 执行 Chome 开发工具命令，得到mhtml内容
    res = driver.execute_cdp_cmd('Page.captureSnapshot', {})
    html = driver.title
    html = html + ".mhtml"
    # 特殊字符/的处理
    html=html.replace("/","")
    # 待存储目录
    html = '/Users/dev/Desktop/极客时间/geektime/42 Android开发高手课【完结】/mhtml/'+html
    print(html)
    # 2. 写入文件
    with open(html, 'w') as f:
        f.write(res['data'])
    # 获取下一页
    elem = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[3]/div[6]")
    elem.click()
    time.sleep(8)
    i = i + 1
