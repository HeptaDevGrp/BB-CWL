from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import configparser
import time


class login:
    refresh_limit_number = 5
    def __init__(self, driver=None):
        # local variable initialization
        self.driver = driver
        self.account = "example.19@intl.zju.edu.cn"
        self.password = "PasswordYouLike"

    def load_account_info(self):
        # load the config file
        config = configparser.ConfigParser()
        config.read("config.ini")
        self.account = config['identification_information']['account_config']
        self.password = config['identification_information']['password_config']
        return

    def logging_in_process(self):
        # click on "INTL ID"
        INTL_ID_button = WebDriverWait(self.driver,10).until(lambda d:d.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div/div[1]/a/img"))
        INTL_ID_button.click()
        print("clicked the INTL ID button -> finish")

        # enter the account name
        max_refresh_number=0
        while(True):
            try:
                # due to ZJU portal code change, must use time.sleep() here!
                time.sleep(5)
                account_input_box = WebDriverWait(self.driver, 10).until(lambda d: d.find_element_by_id('i0116'))
                account_input_box.send_keys(self.account)
                next_step_button = WebDriverWait(self.driver, 10).until(lambda d: d.find_element_by_id('idSIButton9'))
                next_step_button.click()
                break
            except:
                print("fail to enter account name -> try again")
                self.driver.refresh()
                time.sleep(2)
                max_refresh_number += 1
            if(max_refresh_number > self.refresh_limit_number):
                print("fail to enter account name -> finish")
                return
        print("entered the account name -> finish")

        # enter the password and confirm
        max_refresh_number = 0
        while(max_refresh_number <= self.refresh_limit_number):
            try:
                time.sleep(5)
                password_input_box = WebDriverWait(self.driver, 10).until(lambda d: d.find_element_by_id('i0118'))
                password_input_box.send_keys(self.password)
                signin_button = WebDriverWait(self.driver, 10).until(lambda d: d.find_element_by_xpath('//*[@id="idSIButton9"]'))
                signin_button.click()
                break
            except:
                print("fail to enter password -> try again")
                # do NOT refresh!
                max_refresh_number += 1
        if(max_refresh_number > self.refresh_limit_number):
            print("fail to enter password -> finish")
            return
        print("entered the password -> finish")

        # click the YES button
        max_refresh_number = 0
        while(max_refresh_number <= self.refresh_limit_number):
            try:
                time.sleep(5)
                YES_button = WebDriverWait(self.driver, 10).until(lambda d: d.find_element_by_xpath('//*[@id="idSIButton9"]'))
                YES_button.click()
                break
            except:
                print("fail to click yes button -> try again")
                self.driver.refresh()
                max_refresh_number += 1
        if(max_refresh_number > self.refresh_limit_number):
            print("fail to click yes button -> finish")
            return
        print("clicked the YES button -> finish")

        # click the "click this link" button
        max_refresh_number = 0
        while(max_refresh_number <= self.refresh_limit_number):
            try:
                click_this_link_button = WebDriverWait(self.driver,10).until(lambda d:d.find_element_by_xpath('/html/body/div/div/div[3]/p[2]/span/a[1]'))
                click_this_link_button.click()
                break
            except:
                print("fail to click the 'this link' button -> try again")
                max_refresh_number += 1
        if(max_refresh_number > self.refresh_limit_number):
            print("fail to click the 'this link' button -> finish")
            return
        print("clicked the 'this link' button -> finish")

        # click the "INTL ID" button again
        max_refresh_number = 0
        while(max_refresh_number <= self.refresh_limit_number):
            try:
                INTL_ID_button_second = WebDriverWait(self.driver,10).until(lambda d:d.find_element_by_xpath('/html/body/div/div[3]/div[2]/div/div[2]/div/div[1]/div/div[1]/a/img'))
                INTL_ID_button_second.click()
                break
            except:
                print("fail to click the 'INTL ID' button again -> try again")
                self.driver.refresh()
                max_refresh_number += 1
            if (max_refresh_number > self.refresh_limit_number):
                print("fail to click 'INTL ID' button again -> finish")
                return
        print("clicked the 'INTL ID' button again -> finish")

        print("You've now successfully logged in -> finish")
        return

    def login_caller(self):
        # load the account info from config file to the program
        self.load_account_info()
        # login the BlackBoard portal
        self.logging_in_process()
        return
