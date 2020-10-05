from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import logging
from selenium.common import exceptions


class slackMonitor:

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

    def readMessageContent(self):
        # looking for content
        messages = self.driver.find_elements_by_css_selector(
            'div[data-qa="message_content"]')
        # save content in list
        contents = list()
        # read message sender and message content
        for message in messages:
            sname = message.find_element_by_css_selector(
                'a[data-qa="message_sender_name"]').text
            mcontent = message.find_element_by_css_selector(
                'span[data-qa="message-text"]').text

            # save message
            scontent = {
                "sender": sname,
                "message": mcontent,
            }
            contents.append(scontent)
        return contents

    def sendMessage(self):
        msg = '/alto-profile rplist qa master--1-200711'
        # read message before send
        bcontents = self.readMessageContent()
        # locate and send message
        minput = self.driver.find_element_by_css_selector(
            'div[data-qa="message_input"] div[role="textbox"]')
        minput.send_keys(msg)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'button[data-qa="texty_send_button"]'))).click()
        # read message after send
        ccontents = self.readMessageContent()

        # print new message
        ncontents = list()
        for ccontent in ccontents:
            if ccontent not in bcontents:
                ncontents.append(ccontent)
        print(ncontents)
