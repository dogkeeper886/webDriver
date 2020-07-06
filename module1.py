from selenium import webdriver
import time
import sys

# setup browser
urlInput = sys.argv[1]
browser = webdriver.Edge(executable_path='msedgedriver.exe')
browser.set_window_size(1366, 768)
browser.get(urlInput)

# login
userNameInput = sys.argv[2]
userPasswordInput = sys.argv[3]
userName = browser.find_element_by_id('user_username')
userName.send_keys(userNameInput)
userPassword = browser.find_element_by_id('user_password')
userPassword.send_keys(userPasswordinput)
login = browser.find_element_by_name('commit')
login.click()
time.sleep(15)

# logout
userIcon = browser.find_elements_by_css_selector('div.icon-user')
if len(userIcon) == 1:
    userIcon[0].click()
    logout = browser.find_elements_by_css_selector('span Lo')

# browser.close()
