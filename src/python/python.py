# coding = utf-8

from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('http://localhost:8080/AustralianPlat/')
print(driver.title)  # 把页面title 打印出来
if driver.title==u'澳洲金鼎':
    print('打开链接成功')
else:
    print('打开链接失败')
time.sleep(2)
driver.maximize_window()
print('浏览器最大化处理')
time.sleep(2)
driver.find_element_by_id("account").send_keys("test2") #输入账号
driver.find_element_by_id("pwd").send_keys("123456") #输入密码
driver.find_element_by_id("code").send_keys("1234") #输入要验证码
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/form/div[5]/input").click()  #点击登陆按钮
time.sleep(2)
user=driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/span[2]/div/a/span[1]").text  #获取账号信息
print(user)
if  user==u'test2':#校验是否登陆成功
    print('登陆成功')
else:
    print('登陆失败')
time.sleep(5)
driver.quit()
print('浏览器关闭')