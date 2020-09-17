from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep


class deepTools:
    browser = webdriver.Edge(executable_path='msedgedriver.exe')

    def __init__(self, url):
        # setup browser
        self.browser.implicitly_wait(10)
        self.browser.delete_all_cookies()
        self.browser.set_window_size(1366, 768)
        self.browser.get(url)

    def deleteByIdmId(self, idmId):
        inputField = self.browser.find_element_by_css_selector(
            'input#tenantId')
        inputField.send_keys(idmId)
        buttinDelete = self.browser.find_element_by_css_selector(
            'button#deleteButton')
        buttinDelete.click()

    def statusCheck(self):
        outputWait = self.browser.find_element_by_css_selector(
            'output#waiting')
        waitText = str(outputWait.text)
        print(waitText)
        return waitText

    def status(self):
        statusText = self.statusCheck()
        while len(statusText) > 0:
            sleep(10)
            statusText = self.statusCheck()

    def checkResult(self):
        results = self.browser.find_element_by_css_selector('div#results')
        print(results.text)
