from appium import webdriver

desired_caps={
    'deviceName': 'Android Emulator',
    'automationName': 'appium',
    'platformName': 'Android',
    'appPackage': 'com.android.calculator2',
    'appActivity': '.Calculator'
}
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.find_element_by_id("com.android.calculator2:id/digit_1").click()
driver.find_element_by_id("com.android.calculator2:id/op_add").click()
driver.find_element_by_id("com.android.calculator2:id/digit_2").click()
driver.find_element_by_id("com.android.calculator2:id/eq").click()

driver.quit()