from selenium import webdriver
from crawler_helper import headless_mode_initialization
from time import sleep
from login import login

# set up chrome
chrome_options = headless_mode_initialization()
driver = webdriver.Chrome(options=chrome_options)

# open the Blackboard Website
driver.implicitly_wait(10)
driver.get("https://learn.intl.zju.edu.cn/")

# set up the login process
login_object = login(driver)
login_object.login_caller()

# click the "agree & continue" button
driver.implicitly_wait(10)
agree_button = driver.find_element_by_xpath('/html/body/div[8]/div/div/div/div/div/div/div[2]/button')
agree_button.click()

# click "announcements"
driver.implicitly_wait(10)
announcements_button = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div/div/div/div/div[1]/div[1]/div[2]/ul/li[1]/a')
announcements_button.click()

# retrieve the form
print(driver.page_source)

# wait for next command
sleep(100)


driver.quit()
