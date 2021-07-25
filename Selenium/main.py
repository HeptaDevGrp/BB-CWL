from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import configparser
from time import sleep

# load the config file
config = configparser.ConfigParser()
config.read("config.ini")

account = config['identification_information']['account_config']
password = config['identification_information']['password_config']

# open the Blackboard Website
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://learn.intl.zju.edu.cn/")

# click on "INTL ID"
driver.implicitly_wait(10)
INTL_ID_button = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/a/img")
INTL_ID_button.click()

# enter the account name
driver.implicitly_wait(10)
account_input_box = driver.find_element_by_xpath('/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div/div/div[2]/div[2]/div/input[1]')
account_input_box.send_keys(account)
account_input_box.send_keys(Keys.ENTER)

# enter the password and confirm
driver.implicitly_wait(10)
password_input_box = driver.find_element_by_xpath('/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[2]/div/div[2]/input')
password_input_box.send_keys(password)
password_input_box.send_keys(Keys.ENTER)

# click the YES button
driver.implicitly_wait(10)
YES_button = driver.find_element_by_xpath('/html/body/div/form/div/div/div[2]/div[1]/div/div/div/div/div/div/div[1]/div[2]/div/div[2]/div/div[3]/div[2]/div/div/div[2]/input')
YES_button.click()

# click the "click this link" button
driver.implicitly_wait(10)
click_this_link_button = driver.find_element_by_xpath('/html/body/div/div/div[3]/p[2]/span/a[1]')
click_this_link_button.click()

# click the "INTL ID" button again
driver.implicitly_wait(10)
INTL_ID_button_second = driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/div/div[2]/div/div[1]/div/div[1]/a/img')
INTL_ID_button_second.click()

# click the "agree & continue" button
driver.implicitly_wait(10)
agree_button = driver.find_element_by_xpath('/html/body/div[8]/div/div/div/div/div/div/div[2]/button')
agree_button.click()

# successfully logged in
sleep(100)

driver.quit()