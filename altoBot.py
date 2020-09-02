import selenium.webdriver
import time
import sys


class deepTools:
    browser = selenium.webdriver.Edge(executable_path='msedgedriver.exe')

    def __init__(self, url):
        # setup browser
        self.browser.delete_all_cookies()
        self.browser.set_window_size(1366, 768)
        self.browser.get(url)
        time.sleep(3)

    def deleteByIdmId(self, idmId):
        inputField = self.browser.find_element_by_css_selector(
            'input#tenantId')
        inputField.send_keys(idmId)
        buttinDelete = self.browser.find_element_by_css_selector(
            'button#deleteButton')
        buttinDelete.click()

    #def status(self):
    #    self.browser.find_element_by_css_selector()


if len(sys.argv) != 3:
    print('[DEEPTOOLS_URL][IDMID]')
    exit(1)

# go to url
myUrl = sys.argv[1]
myIdmId = sys.argv[2]

# go to venues
myTool = deepTools(myUrl)
myTool.deleteByIdmId(myIdmId)
