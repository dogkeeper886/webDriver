from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions


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
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'input[type="submit"]'))).click()
        # tool tip
        try:
            self.driver.find_element_by_css_selector(
                'a[ptooltip="Close this pop up"]').click()
        except exceptions.NoSuchElementException:
            print('no tool tip')

    def findByText(self, css, text):
        elements = self.driver.find_elements_by_css_selector(css)
        for element in elements:
            if element.text == text:
                return element
