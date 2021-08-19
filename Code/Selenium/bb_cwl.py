from selenium import webdriver
from submodules.crawler_helper import *
from submodules.login import *
from submodules.file_io import *
from submodules.mysql import read_into_mysql
from submodules.data_cleaner import data_cleaner
from submodules.data_formatter import *
import time
def BB_CWL_retrieve_data(file_postfix = ''):
    
    # count the each function's run time
    count = 1
    while(True):
        print(" this is "+str(count)+" time of thread"+file_postfix)
        
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
        max_try_number=0
        while(max_try_number<3):
            try:
                driver.implicitly_wait(10)
                agree_button = driver.find_element_by_xpath('/html/body/div[8]/div/div/div/div/div/div/div[2]/button')
                agree_button.click()
                break
            except:
                # refresh the page
                driver.refresh()
                max_try_number += 1
                if(max_try_number == 3):    
                    print("didn't find the agree & continue after 3 times")
                    return
            
        # click "announcements"
        driver.implicitly_wait(10)
        announcements_button = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div/div/div/div/div[1]/div[1]/div[2]/ul/li[1]/a')
        announcements_button.click()
        
        # retrieve the form
        form = page_form_extract(driver)
        raw_file_path='products/raw_data'+file_postfix+'.txt'
        clean_file_path='products/clean_data'+file_postfix+'.txt'
        formatted_data_path = 'products/formatted_data'+file_postfix+'.json'
        formatted_data_for_node_path = '../Node/data/formatted_data'+file_postfix+'.json'
        formatted_data_for_javascript_path = '../Node/client_helper/import_data'+file_postfix+'.js'
        write_file(raw_file_path, form, 'txt')  # ''raw_data.txt extant or not, this will always execute
        
        # read again and clean the data
        content = read_file(raw_file_path, 'txt')
        data_cleaner_obj = data_cleaner(content)
        content_clean = data_cleaner_obj.data_cleaner_process()
        write_file(clean_file_path, content_clean, 'txt')
        
        # read again and format the data
        clean_data = read_file(clean_file_path, 'txt')
        format_data_obj = format_data(clean_data)
        write_file(formatted_data_path, format_data_obj, 'json')  # json copy for Selenium
        write_file(formatted_data_for_node_path, format_data_obj, 'json')  # json copy for Node
        write_file(formatted_data_for_javascript_path, format_data_obj, 'js')  # javascript copy for Node
        
        # # import data to MySQL database
        # content = read_file('products/formatted_data.json', 'json')
        # read_into_mysql(content)
        
        # pause the function
        time.sleep(10)
        count += 1
        
        # feedback and exit
        print("All functionalities work.")
        driver.quit()
    return