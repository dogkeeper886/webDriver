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


class alto():
    def __init__(self, url, login_email, login_password):
        self.driver = webdriver.Edge('msedgedriver.exe')
        self.wait = WebDriverWait(self.driver, 10)

        logging.info('Get URL: ' + url)
        self.driver.set_window_size(1600, 900)
        self.driver.delete_all_cookies()
        self.driver.get(url)

        # user_username
        self.driver.find_element_by_id('user_username').send_keys(login_email)
        # user_password
        self.driver.find_element_by_id(
            'user_password').send_keys(login_password)
        # submit
        self.driver.find_element_by_css_selector(
            'input[type="submit"]').click()

    def __del__(self):
        logging.info('Close after 10 seconds')
        sleep(10)
        self.driver.close()

    def closeToolTip(self):
        logging.info('Locate tooltip')
        try:
            self.driver.find_element_by_css_selector(
                'a[ptooltip="Close this pop up"]').click()
        except NoSuchElementException:
            logging.info('No tooltip found')

    def menuTab(self, tab):
        logging.info('Locate tab: ' + tab)
        leftmenu_tab = self.driver.find_elements_by_css_selector(
            'a.leftmenu-tab.ng-star-inserted div.menu-item-label')
        for menu_item in leftmenu_tab:
            if menu_item.text == tab:
                menu_item.click()
        self.wait.until(presence_of_element_located(
            (By.CSS_SELECTOR, 'div[class="main-area"]')))

    def addVenue(self, venueName):
        logging.info('Click add')
        self.driver.find_element_by_css_selector(
            'rc-link-button.left button span').click()
        self.wait.until(presence_of_element_located(
            (By.CSS_SELECTOR, 'div[role="dialog"]')))
        logging.info('Add: ' + venueName)
        # venueName
        self.driver.find_element_by_css_selector(
            'input#venueName').send_keys(venueName)
        # addVenueFormAddress
        input_element = self.driver.find_element_by_css_selector(
            'input#addVenueFormAddress')
        input_element.send_keys(venueName)
        sleep(1)
        input_element.send_keys(Keys.ARROW_DOWN)
        sleep(2)
        input_element.send_keys(Keys.ENTER)
        sleep(2)
        # create button
        logging.info('Click create')
        self.wait.until(element_to_be_clickable(
            (By.CSS_SELECTOR, 'div.custom-venue-footer.ng-star-inserted div button'))).click()


# setup log level
logging.basicConfig(level=logging.INFO)

# check argument
if len(argv) != 4:
    logging.error('ARGUMENT COUNT DOES NOT MATCH REQUIREMENT')
    exit(1)

# url, login_email, login_password
altoMan = alto(argv[1], argv[2], argv[3])
sleep(15)
altoMan.closeToolTip()
altoMan.menuTab('Venues')
altoMan.addVenue('Roma')
