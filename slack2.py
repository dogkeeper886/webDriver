from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import selenium


class altobot:
    browser = webdriver.Edge(executable_path='msedgedriver.exe')
    url = 'https://arris.slack.com/'

    def __init__(self):
        # setup browser
        self.browser.implicitly_wait(10)
        self.browser.delete_all_cookies()
        self.browser.set_window_size(1366, 768)
        self.browser.get(self.url)

    def waitByid(self, id):
        try:
            print('wait element by id:', id)
            element = WebDriverWait(self.browser, 10).until(
                expected_conditions.presence_of_element_located((By.ID, id)))
        except selenium.common.exceptions.WebDriverException as err:
            print(err)
            exit(1)
        return element

    def waitBycss(self, css):
        try:
            print('wait element by css:', css)
            element = WebDriverWait(self.browser, 10).until(
                expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, css)))
        except selenium.common.exceptions.WebDriverException as err:
            print(err)
            exit(1)
        return element

    def login(self, uName, uPassword):
        # input email
        self.waitByid('email').send_keys(uName)
        # input password
        self.waitByid('password').send_keys(uPassword)
        # click login
        self.waitByid('signin_btn').click()

    def channel(self, cName):
        elements = self.browser.find_elements_by_css_selector('div a span')
        for element in elements:
            if element.text == cName:
                element.click()
                break

    def runCommand(self, command):
        # enter command
        self.waitBycss('div.ql-editor.ql-blank p br').send_keys(command)
        # send button
        self.waitBycss('button[aria-label="Send message"]').click()

    def findResult(self):
        elements = self.browser.find_elements_by_css_selector(
            'span[data-qa="message-text"]')
        for element in elements:
            try:
                print(element.text)
            except selenium.common.exceptions.StaleElementReferenceException as err:
                print(err)
