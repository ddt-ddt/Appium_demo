# coding=utf-8
from appium import webdriver
import time

desired_caps = {
    'platformName': 'iOS',
    'deviceName': 'Sophie iphone 6',
    'platformVersion': '10.3.3',
    'udid': '440b89ce2945443a6ee7d00011e04bf0e178280f',
    # app包名
    'bundleId': 'com.active.globalpayments.vip',
    'unicodeKeyboard': 'true',
    'resetKeyboard': 'true'
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(2)
# driver.find_element_by_accessibility_id('OK').click()
# email = driver.find_element_by_xpath('//XCUIElementTypeApplication[@name="On-Site"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeTextField/XCUIElementTypeTextField')
# email.send_keys("danting.deng@activenetwork.com")
# password = driver.find_element_by_xpath('//XCUIElementTypeApplication[@name="On-Site"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeSecureTextField/XCUIElementTypeSecureTextField')
# password.click()
# password.send_keys("123456")
time.sleep(5)
driver.find_element_by_accessibility_id(' CASH IN').click()
time.sleep(5)
# alert = driver.find_element_by_accessibility_id('The system can not log you in. Please check the email address and password that you have entered.')
# verify text in alert
# assert alert.text == "Could not log you in. Please check your login "
# print(alert.text)
# driver.find_element_by_accessibility_id('OK').click()
# driver.switch_to.alert.accept()
time.sleep(5)
driver.quit()
