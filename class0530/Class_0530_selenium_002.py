from selenium import webdriver
from selenium.webdriver.common.by import By

'''
    简单原理:
    selenium 通过 webdriver 操作浏览器
    不同品牌的浏览器有不同的webdriver
    通过python代码操作webdriver => 浏览器 => 测试
'''

# 操作步骤:
# 创建'谷歌'的选项对象
option = webdriver.ChromeOptions()
# 设置待测页面不自动关闭
option.add_experimental_option('detach', True)
# 把selenium中的webdriver加载到我们的代码中 => 导包/导入
driver = webdriver.Chrome(options=option)
# 打开baidu网站
# method => m 方法
driver.get("https://baidu.com")
# 获取title标签
# <title></title>
title = driver.find_element(By.TAG_NAME, 'title')
# id=wrapper
# div = driver.find_element(By.ID, "wrapper")
# 获取title标签中的text属性的属性值
text = title.get_property('text')
# 打印
print(text)
# 手动关闭页面
# driver.quit()
driver.close()
