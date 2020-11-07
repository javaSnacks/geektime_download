#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://time.geekbang.org/column/article/83087")
print (0)
time.sleep(4)
elem = driver.find_element_by_class_name("_3d13BJVh_0")
elem.click()
time.sleep(2)
print (1)
time.sleep(2)
elem = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[1]/div[1]/input")
# 输入手机号
elem.send_keys("17199741196")
print (2)
elem = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/button")
elem.click()
print (3)
# 在以下时间内输入验证码
time.sleep(50)
# elem = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[2]/input")
# elem.send_keys("wybq1234")
print (4)
time.sleep(2)
elem = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/button")
elem.click()
print (5)
time.sleep(2)
i = 0
while i < 60:
    # 1. 执行 Chome 开发工具命令，得到mhtml内容
    res = driver.execute_cdp_cmd('Page.captureSnapshot', {})
    html = driver.title
    html = html + ".mhtml"
    html = '/Users/dev/Desktop/极客时间/王宝令java并发编程实战/mhtml/'+html
    print(i+html)
    # 2. 写入文件
    with open(html, 'w') as f:
        f.write(res['data'])
    elem = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[3]/div[6]")
    elem.click()
    time.sleep(8)
    i = i + 1
