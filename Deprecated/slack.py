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
            element = WebDriverWait(self.browser, 10).until(expected_conditions.presence_of_element_located((By.ID, id)))
        except selenium.common.exceptions.WebDriverException  as err:
            print(err)
        return element

    def login(self, uName, uPassword):
        #input email
        self.waitByid('email').send_keys(uName)
        #input password
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
        c_input = self.browser.find_element_by_css_selector(
            'div.ql-editor.ql-blank p br')
        c_input.send_keys(command)
        s_button = self.browser.find_element_by_css_selector(
            'button[aria-label="Send message"]')
        s_button.click()

    def findResult(self):
        elements = self.browser.find_elements_by_css_selector(
            'span[data-qa="message-text"]')
        for element in elements:
            try:
                print(element.text)
            except selenium.common.exceptions.StaleElementReferenceException as err:
                print(err)
