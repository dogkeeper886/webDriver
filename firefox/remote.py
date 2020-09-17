from selenium import webdriver
from time import sleep


class remoteFiredox():
    firefox_options = webdriver.FirefoxOptions()
    driver = webdriver.Remote(
        command_executor='http://192.168.2.219:4444',
        options=firefox_options
    )

    def __init__(self, url):
        self.driver.delete_all_cookies()
        self.driver.get(url)

    def __del__(self):
        self.driver.quit()
