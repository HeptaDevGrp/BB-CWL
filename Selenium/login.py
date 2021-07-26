from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import configparser


class login:
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
        self.driver.implicitly_wait(10)
        INTL_ID_button = self.driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/a/img")
        INTL_ID_button.click()

        # enter the account name
        self.driver.implicitly_wait(10)
        account_input_box = self.driver.find_element_by_xpath(
            '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div/div/div[2]/div[2]/div/input[1]')
        account_input_box.send_keys(self.account)
        account_input_box.send_keys(Keys.ENTER)

        # enter the password and confirm
        self.driver.implicitly_wait(10)
        password_input_box = self.driver.find_element_by_xpath(
            '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[2]/div/div[2]/input')
        password_input_box.send_keys(self.password)
        password_input_box.send_keys(Keys.ENTER)

        # click the YES button
        self.driver.implicitly_wait(10)
        YES_button = self.driver.find_element_by_xpath(
            '/html/body/div/form/div/div/div[2]/div[1]/div/div/div/div/div/div/div[1]/div[2]/div/div[2]/div/div[3]/div[2]/div/div/div[2]/input')
        YES_button.click()

        # click the "click this link" button
        self.driver.implicitly_wait(10)
        click_this_link_button = self.driver.find_element_by_xpath('/html/body/div/div/div[3]/p[2]/span/a[1]')
        click_this_link_button.click()

        # click the "INTL ID" button again
        self.driver.implicitly_wait(10)
        INTL_ID_button_second = self.driver.find_element_by_xpath(
            '/html/body/div/div[3]/div[2]/div/div[2]/div/div[1]/div/div[1]/a/img')
        INTL_ID_button_second.click()

        return

    def login_caller(self):
        self.load_account_info()
        self.logging_in_process()
        return
