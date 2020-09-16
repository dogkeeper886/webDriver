from alto import altoWeb
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions


class addNetDevice(altoWeb):
    def addNetDevice(self, device, name, serial):
        # find add net device link at dash board
        addNetDevLink = self.findByText(
            'div rc-dropdown-button div span', 'Add Net. Device')
        try:
            addNetDevLink.click()
        except exceptions.ElementClickInterceptedException as clickErr:
            print('Click addNetDevLink error.', clickErr)
            exit(1)

        if device == 'switch':
            # click add switch link
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, 'rc-link-button[buttontext="Switch"]'))).click()
        if device == 'ap':
            # click add wifi ap link
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, 'rc-link-button[buttontext="Wi-Fi AP"]'))).click()
            self.driver.find_element_by_id('apName').send_keys(name)
            self.driver.find_element_by_id('apSerialNumber').send_keys(serial)
            createButton = self.findByText('p-button button span', 'Create')
            createButton.click()

        else:
            print('device selection err')
            exit(1)
