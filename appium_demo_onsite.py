# coding=utf-8
from appium import webdriver
import time

desired_caps1 = {
    'platformName': 'Android',
    'deviceName': 'EQAUMR7D4HSGGAJF',
    'platformVersion': '5.0.2',
    # apk包名
    'appPackage': 'com.active.aps.onsite',
    # apk的launcherActivity
    'appActivity': 'com.active.aps.onsite.activities.EventHomeActivity',
    'unicodeKeyboard': 'true',
    'resetKeyboard': 'true'
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps1)
time.sleep(5)
email = driver.find_element_by_id("com.active.aps.onsite:id/loginEmailAddressEditText")
email.send_keys("danting.deng@activenetwork.com")
password = driver.find_element_by_id("com.active.aps.onsite:id/loginPasswordEditText")
password.click()
password.send_keys("123456")
time.sleep(2)
driver.find_element_by_id("com.active.aps.onsite:id/loginSignInButton").click()
time.sleep(5)
alert = driver.find_element_by_id("android:id/message")
# verify text in alert
# assert alert.text == "Could not log you in. Please check your login "
# print(alert.text)
driver.find_element_by_id("android:id/button1").click()
# driver.switch_to.alert.accept()
time.sleep(5)
driver.quit()
