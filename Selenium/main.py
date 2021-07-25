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
driver.get("https://learn.intl.zju.edu.cn/")
sleep(1)

# click on "INTL ID"
INTL_ID_button = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/a/img")
INTL_ID_button.click()
sleep(3)

# enter the account name
account_input_box = driver.find_element_by_xpath('/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div/div/div[2]/div[2]/div/input[1]')
account_input_box.send_keys(account)
sleep(1)

# click on the "next step" button
next_step_button = driver.find_element_by_xpath('/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[4]/div/div/div/div[2]/input')
next_step_button.click()
sleep(100)

# enter the password
password_input_box = driver.find_element_by_xpath('/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[2]/div/div[2]/input')
password_input_box.send_keys(password)


print("Successfully tested.")

driver.quit()