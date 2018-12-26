# coding=utf-8

from appium import webdriver
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
