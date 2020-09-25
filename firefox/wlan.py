class wlans(web):
    def goToWlan(self):
        self.driver.find_element_by_css_selector(
            'em.menu-icon.menu-wlans').click()

    def addWlan(self, name):
        # click add network
        self.findByText(
            'span.ng-star-inserted rc-link-button.left button span', 'Add Network')

        # input network name
        networkNameInput = self.driver.find_element_by_css_selector(
            'input#networkName')
        print('input', name)
        networkNameInput.send_keys(name)

    def psk(self):
        # select network type
        self.driver.find_element_by_css_selector('input[value="psk"]').click()


class dhcp(venues):
    def goDhcp(self):
        self.goToVenues()
