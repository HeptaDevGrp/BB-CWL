from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import configparser


class login:
    refresh_limit_number = 100
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
        # self.driver.implicitly_wait(10)
        # INTL_ID_button = self.driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/a/img")
        INTL_ID_button = WebDriverWait(self.driver,10).until(lambda d:d.find_element_by_xpath("/html/body/div[2]/div/div[1]/a/img"))
        INTL_ID_button.click()

        # enter the account name
        max_refresh_number=0
        while(True):
            if(max_refresh_number > self.refresh_limit_number):
                print("fail to enter account name")
                return
            else:
                try:
                    # self.driver.implicitly_wait(10)
                    # account_input_box = self.driver.find_element_by_xpath(
                    #     '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div/div/div[2]/div[2]/div/input[1]')
                    account_input_box = WebDriverWait(self.driver,10).until(lambda d:d.find_element_by_xpath('/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div/div/div[2]/div[2]/div/input[1]'))
                    account_input_box.send_keys(self.account)
                    account_input_box.send_keys(Keys.ENTER)
                    break
                except:
                    max_refresh_number += 1

        # enter the password and confirm
        max_refresh_number = 0
        while(max_refresh_number <= self.refresh_limit_number):
            try:
                # self.driver.implicitly_wait(10)
                # password_input_box = self.driver.find_element_by_xpath(
                #     '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[2]/div/div[2]/input')
                password_input_box = WebDriverWait(self.driver,10).until(lambda d:d.find_element_by_xpath('/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[2]/div/div[2]/input'))
                password_input_box.send_keys(self.password)
                password_input_box.send_keys(Keys.ENTER)
                break
            except:
                self.driver.refresh()
                max_refresh_number += 1
        if(max_refresh_number > self.refresh_limit_number):
            print("fail to enter password")
            return
        
        # click the YES button
        max_refresh_number = 0
        while(max_refresh_number <= self.refresh_limit_number):
            try:
                # self.driver.implicitly_wait(10)
                # YES_button = self.driver.find_element_by_xpath(
                #     '/html/body/div/form/div/div/div[2]/div[1]/div/div/div/div/div/div/div[1]/div[2]/div/div[2]/div/div[3]/div[2]/div/div/div[2]/input')
                YES_button = WebDriverWait(self.driver,30).until(lambda d:d.find_element_by_xpath('/html/body/div/form/div/div/div[2]/div[1]/div/div/div/div/div/div/div[1]/div[2]/div/div[2]/div/div[3]/div[2]/div/div/div[2]/input'))
                YES_button.click()
                break
            except:
                self.driver.refresh()
                max_refresh_number += 1
        if(max_refresh_number > self.refresh_limit_number):
            print("fail to click yes button")
            return

        # click the "click this link" button
        max_refresh_number = 0
        while(max_refresh_number <= self.refresh_limit_number):
            try:
                # self.driver.implicitly_wait(10)
                # click_this_link_button = self.driver.find_element_by_xpath('/html/body/div/div/div[3]/p[2]/span/a[1]')
                click_this_link_button = WebDriverWait(self.driver,10).until(lambda d:d.find_element_by_xpath('/html/body/div/div/div[3]/p[2]/span/a[1]'))
                click_this_link_button.click()
                break
            except:
                self.driver.refresh()
                max_refresh_number += 1
        if(max_refresh_number > self.refresh_limit_number):
            print("fail to click this link")
            return
        
        # click the "INTL ID" button again
        max_refresh_number = 0
        while(max_refresh_number <= self.refresh_limit_number):
            if(max_refresh_number > self.refresh_limit_number):
                print("fail to click INTL ID button again")
                return
            else:
                try:
                    # self.driver.implicitly_wait(10)
                    # INTL_ID_button_second = self.driver.find_element_by_xpath(
                    #     '/html/body/div/div[3]/div[2]/div/div[2]/div/div[1]/div/div[1]/a/img')
                    INTL_ID_button_second = WebDriverWait(self.driver,10).until(lambda d:d.find_element_by_xpath('/html/body/div/div[3]/div[2]/div/div[2]/div/div[1]/div/div[1]/a/img'))
                    INTL_ID_button_second.click()
                    break
                except:
                    self.driver.refresh()
                    max_refresh_number += 1

        return

    def login_caller(self):
        self.load_account_info()
        self.logging_in_process()
        return
