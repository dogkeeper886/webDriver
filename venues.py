import alto
import time


class venue(alto.web):
    def venues(self):
        self.browser.find_element_by_css_selector(
            '<div.widget-caption.properties-headline-cell').click()
        time.sleep(3)
