from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=option)
driver.get("https://baidu.com")

# 获取输入框
input_search = driver.find_element(By.ID, 'kw')
# 向输入框输入 暗黑破坏神4
input_search.send_keys('暗黑破坏神4')

# 获取搜索按钮
button_search = driver.find_element(By.ID, 'su')
# 点击搜索按钮
button_search.click()

sleep(2)
# 获取结果
a = driver.find_element(By.XPATH, '//*[@id="3001"]/div/div[2]/div[2]/div[1]/div/a')
text = a.get_property("text")
print(text == '暗黑4加速器,暴雪战网免费加速器,迅游加速器支持各区服联机加速,轻松加速一..')
