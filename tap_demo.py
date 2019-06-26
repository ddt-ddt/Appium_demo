from appium import webdriver
import time

from appium.webdriver.common.touch_action import TouchAction

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
# time.sleep(5)
# driver.tap([(122,1502)],1)
# time.sleep(5)


action=TouchAction(driver)
action.press(x=220,y=700).move_to(x=840,y=700).move_to(x=220,y=1530).move_to(x=840,y=1530).release().perform()

time.sleep(5)
driver.quit()