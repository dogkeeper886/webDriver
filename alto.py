import selenium.webdriver
import time


class web:
    browser = selenium.webdriver.Edge(executable_path='msedgedriver.exe')

    def __init__(self, url, uName, uPassword):
        # setup browser
        self.browser.delete_all_cookies()
        self.browser.set_window_size(1366, 768)
        self.browser.get(url)
        time.sleep(3)

        # username
        self.browser.find_element_by_css_selector(
            'input#user_username').send_keys(uName)

        # password
        self.browser.find_element_by_css_selector(
            'input#user_password').send_keys(uPassword)

        # login button
        self.browser.find_element_by_css_selector(
            'input.button.btn-info.btn-block').click()
        time.sleep(20)

        # looking for start tips
        try:
            closeButton = self.browser.find_element_by_css_selector(
                'a.icon.icon-sm.icon-delete.close.ng-star-inserted')
            closeButton.click()
        except selenium.common.exceptions.NoSuchElementException as err:
            print('No start tips', err)

    def find_element_by_match_text(self, css, text):
        status = bool(False)
        elements = self.browser.find_elements_by_css_selector(css)

        for element in elements:
            if element.text == text:
                status = True
                print('click', text, css)
                element.click()
                break

        return status


class venues(web):
    def goToVenues(self):
        self.browser.find_element_by_css_selector(
            'em.menu-icon.menu-venues').click()
        time.sleep(3)

    def addVenue(self, venueName, venueAddr):
        # click add venue
        self.find_element_by_match_text(
            'span.ng-star-inserted rc-link-button.left button span', 'Add Venue')
        time.sleep(3)

        # input venue
        print('input', venueName)
        self.browser.find_element_by_css_selector(
            'input#venueName').send_keys(venueName)

        # input venue
        print('input', venueAddr)
        inputField = self.browser.find_element_by_css_selector(
            'input#addVenueFormAddress')
        inputField.send_keys(venueAddr)
        time.sleep(1)
        inputField.send_keys(selenium.webdriver.common.keys.Keys.ARROW_DOWN)
        time.sleep(2)
        inputField.send_keys(selenium.webdriver.common.keys.Keys.ENTER)
        time.sleep(2)

        # check disabled: button.ui-button.ui-widget.ui-state-default.ui-corner-all.ui-button-text-only.ui-state-disabled span.ui-button-text.ui-clickable
        status = self.find_element_by_match_text(
            'button.ui-button.ui-widget.ui-state-default.ui-corner-all.ui-button-text-only.ui-state-disabled span.ui-button-text.ui-clickable', 'Create')

        if status == True:
            print('Create is disabled')
            self.find_element_by_match_text(
                'rc-link-button button span', 'Cancel')
        else:
            # clickabled: button.ui-button.ui-widget.ui-state-default.ui-corner-all.ui-button-text-only span.ui-button-text.ui-clickable
            self.find_element_by_match_text(
                'button.ui-button.ui-widget.ui-state-default.ui-corner-all.ui-button-text-only span.ui-button-text.ui-clickable', 'Create')

        time.sleep(5)

    def createFromFile(self, fileName):
        self.goToVenues()

        with open('citiList.txt') as f:
            citiList = f.readlines()
        for city in citiList:
            self.addVenue(city, city)

    def basic5(self):
        self.goToVenues()
        self.addVenue('New York', 'New York')
        self.addVenue('Tokyo', 'Tykyo')
        self.addVenue('London', 'London')
        self.addVenue('São Paulo', 'São Paulo')
        self.addVenue('Sydney', 'Sydney')


class wlans(web):
    def goToWlan(self):
        self.browser.find_element_by_css_selector(
            'em.menu-icon.menu-wlans').click()

    def addWlan(self, name):
        # click add network
        self.find_element_by_match_text(
            'span.ng-star-inserted rc-link-button.left button span', 'Add Network')

        # input network name
        networkNameInput = self.browser.find_element_by_css_selector('input#networkName')
        print('input', name)
        networkNameInput.send_keys(name)

    def psk(self):
        # select network type
        self.browser.find_element_by_css_selector('input[value="psk"]').click()


class dhcp(venues):
    def goDhcp(self):
        self.goToVenues()
        
