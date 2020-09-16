from selenium import webdriver
from selenium.common import exceptions
from urllib.parse import urlparse
import re


class altoWeb:
    driver = webdriver.Edge(executable_path='msedgedriver.exe')

    def __init__(self, url):
        self.driver.implicitly_wait(10)
        self.driver.delete_all_cookies()
        self.driver.set_window_size(1366, 768)
        self.driver.get(url)

    def login(self, uName, uPassword):
        # user name
        self.driver.find_element_by_id('user_username').send_keys(uName)
        # user password
        self.driver.find_element_by_id('user_password').send_keys(uPassword)
        # login
        self.driver.find_element_by_css_selector(
            'input[type="submit"]').click()
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
        tId = re.findall('t/(.+)/', urlparse(url).path)
        return tId[0]
