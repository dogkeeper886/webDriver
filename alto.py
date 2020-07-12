import selenium.webdriver
import time


class web:
    browser = selenium.webdriver.Edge(executable_path='msedgedriver.exe')

    def __init__(self, url, uName, uPassword):
        self.browser.delete_all_cookies()
        self.browser.set_window_size(1366, 768)
        self.browser.get(url)
        time.sleep(3)
        self.browser.find_element_by_css_selector(
            'input#user_username').send_keys(uName)
        self.browser.find_element_by_css_selector(
            'input#user_password').send_keys(uPassword)
        self.browser.find_element_by_css_selector(
            'input.button.btn-info.btn-block').click()
        time.sleep(20)

    def find_element_by_match_text(self, css, text):
        for element in self.browser.find_elements_by_css_selector(css):
            if element.text == text:
                print('match', element)
                return element
            else:
                print('not match', element)


class venues(web):
    def goToVenues(self):
        self.find_element_by_match_text(
            'div.widget-caption.properties-headline-cell', 'Venues').click()
        time.sleep(3)

    def addVenue(self, venueName, venueAddr):
        self.find_element_by_match_text('button span', 'Add Venue').click()
        time.sleep(3)
        self.browser.find_element_by_css_selector(
            'input#venueName').send_keys(venueName)
        self.browser.find_element_by_css_selector(
            'input#addVenueFormAddress').send_keys(venueAddr)
        selenium.webdriver.common.keys.Keys.ARROW_DOWN()
        time.sleep(3)
        self.browser.find_element_by_css_selector(
            'span.ui-button-text.ui-clickable').click()
        time.sleep(3)