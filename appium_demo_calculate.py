# coding=utf-8
from appium import webdriver
import time

desired_caps = {
    'platformName': 'Android',
    'deviceName': 'EQAUMR7D4HSGGAJF',
    'platformVersion': '5.0',
    # apk包名
    'appPackage': 'com.youba.calculate',
    # apk的launcherActivity
    'appActivity': 'com.youba.calculate.MainActivity'
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(5)
# driver.find_element_by_id("com.youba.calculate:id/btn_one").click()
# driver.find_element_by_id("com.youba.calculate:id/btn_plus").click()
# driver.find_element_by_id("com.youba.calculate:id/btn_five").click()
# driver.find_element_by_id("com.youba.calculate:id/btn_equal").click()
time.sleep(5)
driver.quit()
