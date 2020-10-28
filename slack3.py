from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.expected_conditions import NoSuchElementException
from time import sleep
import logging
from sys import argv
from os import environ


class slack():
    def __init__(self, url, login_email, login_password):
        # text mode firefox issue
        options = webdriver.firefox.options.Options()
        options.headless = True
        self.driver = webdriver.Firefox(firefox_options=options)
        #self.driver = webdriver.Edge('msedgedriver.exe')
        self.wait = WebDriverWait(self.driver, 10)

        logging.info('Get URL: ' + url)
        self.driver.get(url)

        # login
        self.driver.find_element_by_id('email').send_keys(login_email)
        self.driver.find_element_by_id('password').send_keys(login_password)
        self.driver.find_element_by_id('signin_btn').click()

    def __del__(self):
        logging.info('Close after 10 seconds')
        sleep(10)
        self.driver.close()

    def changeChannel(self, channel_id):
        css = 'a[data-qa-channel-sidebar-channel-id="{}"]'

        logging.info('Change chnnel: ' + channel_id)
        self.wait.until(presence_of_element_located(
            (By.CSS_SELECTOR, css.format(channel_id)))).click()
        # self.driver.find_element_by_css_selector(css.format(channel_id)).click()
        self.wait.until(presence_of_element_located(
            (By.CSS_SELECTOR, 'div[role="main"]')))

    def dump(self):
        itemList = self.driver.find_elements_by_css_selector(
            'div[data-qa="virtual-list-item"]')
        itemList_output = 'ItemList count: {}'
        logging.info(itemList_output.format(len(itemList)))

        for item in itemList:
            # locate sender
            try:
                message_sender = item.find_element_by_css_selector(
                    'div[data-qa="message_content"] span[data-qa="message_sender"] a[data-qa="message_sender_name"]').text
            except NoSuchElementException:
                try:
                    message_sender = item.find_element_by_css_selector(
                        'div.c-message_kit__labels__label span.c-message_kit__labels__text').text
                except NoSuchElementException:
                    message_sender = 'Not found'
            # locate messasage
            try:
                message_text = item.find_element_by_css_selector(
                    'div[data-qa="message_content"] span[data-qa="message-text"]').text
            except NoSuchElementException:
                message_text = 'Not found'

            item_output = 'message_sender: {} message_text: {}'
            logging.info(item_output.format(message_sender, message_text))

    def sendMessage(self, message):
        logging.info('Send: ' + message)
        # locate editor
        self.driver.find_element_by_css_selector(
            'div[data-qa="message_input"] div[role="textbox"]').send_keys(message)
        # locate send button
        self.wait.until(element_to_be_clickable(
            (By.CSS_SELECTOR, 'button[data-qa="texty_send_button"]'))).click()


def loopInput():

    # read input
    rawInput = input('Input: ')
    logging.info('Read input: ' + rawInput)

    while rawInput != 'q':
        slackMan.sendMessage(rawInput)
        # dump message
        sleep(10)
        slackMan.dump()

        # read input
        rawInput = input('Input: ')
        logging.info('Read input: ' + rawInput)


# setup log level
logging.basicConfig(level=logging.INFO)

# check argument
if len(argv) != 5:
    logging.error('ARGUMENT COUNT DOES NOT MATCH REQUIREMENT')
    exit(1)

# url, login_email, login_password
slackMan = slack(argv[1], argv[2], argv[3])
# channel_id
slackMan.changeChannel(argv[4])

# dump message
sleep(10)
slackMan.dump()

# send message
slackMan.sendMessage(environ['MESSAGE'])

# dump message
sleep(10)
slackMan.dump()
