# coding=utf-8
from appium import webdriver
import time


desired_caps = {
    'platformName': 'Android',
    'deviceName': 'EQAUMR7D4HSGGAJF',
    'platformVersion': '5.0',
    # apk包名
    'appPackage': 'com.taobao.taobao',
    # apk的launcherActivity
    'appActivity': 'com.taobao.tao.welcome.Welcome'
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(5)
driver.find_element_by_id("com.taobao.taobao:id/home_searchedit").click()
time.sleep(5)
driver.find_element_by_id("com.taobao.taobao:id/searchEdit").click()
driver.find_element_by_id("com.taobao.taobao:id/searchEdit").send_keys("JBL")
driver.quit()
