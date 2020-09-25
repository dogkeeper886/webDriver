from alto import altoWeb
from time import sleep
from selenium.webdriver.common.keys import Keys


class venues(altoWeb):
    def goToVenues(self):
        self.driver.find_element_by_css_selector(
            'em.menu-icon.menu-venues').click()

    def addVenue(self, venueName, venueAddr):
        # click add venue
        self.findByText(
            'span.ng-star-inserted rc-link-button.left button span', 'Add Venue')

        # input venue
        print('input', venueName)
        self.driver.find_element_by_css_selector(
            'input#venueName').send_keys(venueName)

        # input venue
        print('input', venueAddr)
        inputField = self.driver.find_element_by_css_selector(
            'input#addVenueFormAddress')
        inputField.send_keys(venueAddr)
        sleep(1)
        inputField.send_keys(Keys.ARROW_DOWN)
        sleep(2)
        inputField.send_keys(Keys.ENTER)
        sleep(2)

        # check disabled: button.ui-button.ui-widget.ui-state-default.ui-corner-all.ui-button-text-only.ui-state-disabled span.ui-button-text.ui-clickable
        status = self.findByText(
            'button.ui-button.ui-widget.ui-state-default.ui-corner-all.ui-button-text-only.ui-state-disabled span.ui-button-text.ui-clickable', 'Create')

        if status == True:
            print('Create is disabled')
            self.findByText(
                'rc-link-button button span', 'Cancel')
        else:
            # clickabled: button.ui-button.ui-widget.ui-state-default.ui-corner-all.ui-button-text-only span.ui-button-text.ui-clickable
            self.findByText(
                'button.ui-button.ui-widget.ui-state-default.ui-corner-all.ui-button-text-only span.ui-button-text.ui-clickable', 'Create')

        sleep(5)

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
