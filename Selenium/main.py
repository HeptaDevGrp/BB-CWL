from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import configparser
from time import sleep
from login import login

# open the Blackboard Website
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://learn.intl.zju.edu.cn/")

# set up the login process
login_object = login(driver)
login_object.login_caller()

# click the "agree & continue" button
driver.implicitly_wait(10)
agree_button = driver.find_element_by_xpath('/html/body/div[8]/div/div/div/div/div/div/div[2]/button')
agree_button.click()

# successfully logged in
sleep(100)

driver.quit()