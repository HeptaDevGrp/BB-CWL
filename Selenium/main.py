from selenium import webdriver
from submodules.crawler_helper import *
from time import sleep
from submodules.file_io import *
from submodules.data_cleaner import data_cleaner

# set up chrome
chrome_options = headless_mode_initialization()
driver = webdriver.Chrome(options=chrome_options)

# open the Blackboard Website
driver.implicitly_wait(10)
driver.get("https://learn.intl.zju.edu.cn/")

# # set up the login process
# login_object = login(driver)
# login_object.login_caller()
#
# # click the "agree & continue" button
# driver.implicitly_wait(10)
# agree_button = driver.find_element_by_xpath('/html/body/div[8]/div/div/div/div/div/div/div[2]/button')
# agree_button.click()
#
# # click "announcements"
# driver.implicitly_wait(10)
# announcements_button = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div/div/div/div/div[1]/div[1]/div[2]/ul/li[1]/a')
# announcements_button.click()
#
# # retrieve the form
# form = page_form_extract(driver)
# write_file('raw_data.txt', form)  # ''raw_data.txt extant or not, this will always execute

# read again and clean the data
content = read_file('products/raw_data.txt')
data_cleaner = data_cleaner(content)
content_clean = data_cleaner.data_cleaner_process()
write_file('products/clean_data.txt', content_clean)

# feedback and exit
print("All functionalities work.")
driver.quit()
