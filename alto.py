import selenium.webdriver
import time


class web:
    browser = selenium.webdriver.Edge(executable_path='msedgedriver.exe')

    def __init__(self, url, uName, uPassword):
        # self.browser.delete_all_cookies()
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
        # looking for start tips
        self.find_element_if_exist(
            'a.icon.icon-sm.icon-delete.close.ng-star-inserted')

    def find_element_by_match_text(self, css, text):
        for element in self.browser.find_elements_by_css_selector(css):
            if element.text == text:
                print('match', css, element)
                element.click()
                break
            else:
                print('not match', css, element)

    def find_element_if_exist(self, css):
        try:
            webElement = self.browser.find_element_by_css_selector(css)
            print('match', css, webElement)
            webElement.click()
        except selenium.common.exceptions.NoSuchElementException as err:
            print('not match', css, err)


class venues(web):
    def goToVenues(self):
        self.find_element_by_match_text(
            'div.widget-caption.properties-headline-cell', 'Venues')
        time.sleep(3)

    def addVenue(self, venueName, venueAddr):
        # click add venue
        self.find_element_by_match_text(
            'span.ng-star-inserted rc-link-button.left button span', 'Add Venue')

        time.sleep(3)
        # input venue name
        self.browser.find_element_by_css_selector(
            'input#venueName').send_keys(venueName)
        # input venue address
        inputField = self.browser.find_element_by_css_selector(
            'input#addVenueFormAddress')
        inputField.send_keys(venueAddr)
        time.sleep(1)
        inputField.send_keys(selenium.webdriver.common.keys.Keys.ARROW_DOWN)
        time.sleep(1)
        inputField.send_keys(selenium.webdriver.common.keys.Keys.ENTER)
        time.sleep(1)
        # click create
        self.find_element_by_match_text(
            'span.ui-button-text.ui-clickable', 'Create')
        time.sleep(5)
