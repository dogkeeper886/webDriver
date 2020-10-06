from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import logging
from selenium.common import exceptions
from time import sleep


class slackMonitor:
    css = dict()
    css['message_content'] = 'div[data-qa="message_content"] span[data-qa="message-text"]'

    def __init__(self, url):
        # setup browser
        firefox_options = webdriver.FirefoxOptions()
        # setup remote
        self.driver = webdriver.Remote(
            command_executor='http://192.168.2.219:4444',
            options=firefox_options
        )
        # prepare start
        self.driver.delete_all_cookies()
        self.driver.implicitly_wait(10)
        logging.info('url start')
        self.driver.get(url)

    def __del__(self):
        logging.info('remote firefox del after 10sec')
        sleep(10)
        self.driver.quit()

    def login(self, uName, uPassword):
        logging.info('login start')
        # input email
        self.driver.find_element_by_id('email').send_keys(uName)
        # input password
        self.driver.find_element_by_id('password').send_keys(uPassword)
        # click login
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'signin_btn'))).click()

    def channel(self, id):
        css = 'a[data-qa-channel-sidebar-channel-id="{}"]'
        # go to channel
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, css.format(id)))).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[role="main"]')))

    def sendMessage(self, msg):
        # locate and send message
        minput = self.driver.find_element_by_css_selector(
            'div[data-qa="message_input"] div[role="textbox"]')
        minput.send_keys(msg)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'button[data-qa="texty_send_button"]'))).click()

    def checkCommand(self, msg):
        # make sure command send
        elementList = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'span[data-qa="message-text"]')))
        # elementList = self.driver.find_elements_by_css_selector('span[data-qa="message-text"]')

        for element in elementList:
            if element.text == 'msg':
                print('checkCommand pass')
                logging.info('checkCommand pass')

    def checkQueued(self, msg):
        # make sure alto-bot queued
        elementList = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'span')))
        # elementList = self.driver.find_elements_by_css_selector('span')

        text = 'Queued {}'
        for element in elementList:
            if element.text == text.format(msg):
                print('checkQueued pass')
                logging.info('checkQueued pass')

    def readResponse(self):
        itemList = self.driver.find_elements_by_css_selector(
            'div[data-qa="virtual-list-item"]')

        for item in itemList:
            spanList = item.find_elements_by_css_selector('span')
            for span in spanList:
                if span.text == 'Only visible to you':
                    print(item.find_element_by_css_selector(
                        'span[data-qa="message-text"]').text)
