from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from time import sleep
import logging


class slack():
    def __init__(self, url, login_email, login_password):
        self.driver = webdriver.Edge('msedgedriver.exe')
        self.wait = WebDriverWait(self.driver, 10)

        logging.info('Get URL: ' + url)
        self.driver.get(url)

        # login
        self.driver.find_element_by_id('email').send_keys(login_email)
        self.driver.find_element_by_id('password').send_keys(login_password)
        self.driver.find_element_by_id('signin_btn').click()

    def __del__(self):
        logging.info('Close after 30 seconds')
        sleep(30)
        self.driver.close()

    def changeChannel(self, channel_id):
        css = 'a[data-qa-channel-sidebar-channel-id="{}"]'

        logging.info('Change chnnel: ' + channel_id)
        self.wait.until(element_to_be_clickable(
            (By.CSS_SELECTOR, css.format(channel_id)))).click()

    def dump(self):
        self.wait.until(presence_of_element_located(
            (By.CSS_SELECTOR, 'div[role="main"]')))


slackMan = slack('', '', '')
slackMan.changeChannel('')
slackMan.dump()
