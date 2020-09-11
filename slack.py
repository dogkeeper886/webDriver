import selenium.webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class altobot:
    browser = selenium.webdriver.Edge(executable_path='msedgedriver.exe')
    url = 'https://arris.slack.com/'

    def __init__(self):
        # setup browser
        self.browser.implicitly_wait(10)
        self.browser.delete_all_cookies()
        self.browser.set_window_size(1366, 768)
        self.browser.get(self.url)

    def login(self, uName, uPassword):
        #d_input = self.browser.find_element_by_id('domain')
        # d_input.send_keys('arris')
        #c_button = self.browser.find_element_by_css_selector('button[type="submit"]')
        # c_button.click()

        e_input = self.browser.find_element_by_id('email')
        e_input.send_keys(uName)
        p_input = self.browser.find_element_by_id('password')
        p_input.send_keys(uPassword)
        s_button = self.browser.find_element_by_id('signin_btn')
        s_button.click()

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
        elements = self.browser.find_elements_by_css_selector('span[data-qa="message-text"]')
        for element in elements:
            try:
                print(element.text)
            except selenium.common.exceptions.StaleElementReferenceException as err:
                print(err)
            
        