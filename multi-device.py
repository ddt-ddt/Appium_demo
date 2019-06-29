# coding=utf-8

import time
from appium import webdriver
from gevent import os
import threading

desired_caps1 = {
    'platformName': 'Android',
    'platformVersion': '5.0.2',
    'deviceName': 'EQAUMR7D4HSGGAJF',
    'appPackage': 'com.youba.calculate',
    'appActivity': "com.youba.calculate.MainActivity",
    'systemPort': 5000
}

desired_caps2 = {
    'platformName': 'Android',
    'platformVersion': '5.0.2',
    'deviceName': '03157df36144d40d',
    'appPackage': 'com.youba.calculate',
    'appActivity': "com.youba.calculate.MainActivity",
    'systemPort': 5010

}

def test_case(driver):
    driver.find_element_by_id("com.youba.calculate:id/btn_one").click()
    driver.find_element_by_id("com.youba.calculate:id/btn_plus").click()
    driver.find_element_by_id("com.youba.calculate:id/btn_five").click()
    driver.find_element_by_id("com.youba.calculate:id/btn_equal").click()
    driver.quit()

# Start Appium server
os.system('nohup appium -a 127.0.0.1 -p 5000 -bp 2200 -U EQAUMR7D4HSGGAJF &')
os.system('nohup appium -a 127.0.0.1 -p 5010 -bp 2210 -U 03157df36144d40d &')

# Start the driver
driver_obj1 = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps1)
driver_obj2 = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps2)

# Run test case
threads = []
t1 = test_case(driver_obj1)
t2 = test_case(driver_obj2)
threads.append(t1)
threads.append(t2)
