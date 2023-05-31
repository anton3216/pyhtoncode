from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
# 获取webdriver,创建对应浏览器的对象
driver = webdriver.Chrome(options=option)
# 打开baidu页面
driver.get('https://baidu.com')
# 等待
sleep(1)
# 获取标题
title = driver.find_element(By.TAG_NAME, 'title')
text = title.get_property('text')
print(text)
# 等待
sleep(1)
# 关闭baidu页面
