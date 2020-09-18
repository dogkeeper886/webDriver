from remote import remoteFiredox
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import selenium


class slack(remoteFiredox):

    def waitByid(self, id):
        try:
            print('wait element by id:', id)
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, id)))
        except selenium.common.exceptions.WebDriverException as err:
            print(err)
        return element

    def login(self, uName, uPassword):
        # input email
        self.driver.find_element_by_id('email').send_keys(uName)
        # input password
        self.driver.find_element_by_id('password').send_keys(uPassword)
        # click login
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'signin_btn'))).click()

    def channel(self, cName):
        elements = self.driver.find_elements_by_css_selector('div a span')
        for element in elements:
            if element.text == cName:
                element.click()
                break

    def runCommand(self, command):
        #c_input = self.driver.find_element_by_css_selector('div.ql-editor.ql-blank p')
        #c_input.send_keys(command)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.ql-editor.ql-blank p'))).send_keys(command)
               
        #s_button = self.driver.find_element_by_css_selector('button[aria-label="Send message"]')
        #s_button.click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="Send message"]')))

    def findResult(self):
        elements = self.driver.find_elements_by_css_selector(
            'span[data-qa="message-text"]')
        for element in elements:
            try:
                print(element.text)
            except selenium.common.exceptions.StaleElementReferenceException as err:
                print(err)
