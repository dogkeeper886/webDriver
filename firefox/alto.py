from remote import remoteFiredox
from selenium.common import exceptions
from urllib.parse import urlparse
import re
from time import sleep

class altoWeb(remoteFiredox):

    def login(self, uName, uPassword):
        # user name
        self.driver.find_element_by_id('user_username').send_keys(uName)
        # user password
        self.driver.find_element_by_id('user_password').send_keys(uPassword)
        # login
        self.driver.find_element_by_css_selector(
            'input[type="submit"]').click()
        sleep(15)
        
        # tool tip
        try:
            self.driver.find_element_by_css_selector(
                'a[ptooltip="Close this pop up"]').click()
        except exceptions.NoSuchElementException as noElementErr:
            print('No tool tip.', noElementErr)
        except exceptions.ElementClickInterceptedException as clickErr:
            print('Click tool tip error.', clickErr)
            exit(1)

    def findByText(self, css, text):
        elements = self.driver.find_elements_by_css_selector(css)

        for element in elements:
            if element.text == text:
                return element

    def tenantId(self):
        url = self.driver.current_url
        tId = re.findall('t/(.+?)/', urlparse(url).path)
        return tId[0]
