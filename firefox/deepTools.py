from remote import remoteFiredox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep


class deepTools(remoteFiredox):

    def deleteByIdmId(self, idmId):
        inputField = self.driver.find_element_by_css_selector(
            'input#tenantId')
        inputField.send_keys(idmId)
        buttinDelete = self.driver.find_element_by_css_selector(
            'button#deleteButton')
        buttinDelete.click()

    def statusCheck(self):
        outputWait = self.driver.find_element_by_css_selector(
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
        results = self.driver.find_element_by_css_selector('div#results')
        print(results.text)

    def searchTenant(self, tenantId):
        #enter tenantId
        self.driver.find_element_by_css_selector('input#tenantForSearch').send_keys(tenantId)
        #click search button
        self.driver.find_element_by_css_selector('button#searchTenantButton').click()
        #status check
        self.status()


