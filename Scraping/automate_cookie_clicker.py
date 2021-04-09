from selenium import webdriver
# gives access to keys that will allow to type/click enter /esc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

PATH = 'C:\Program Files (x86)\chromedriver.exe'

# browser that we want to use is Chrome and the driver is stored in the PATH
driver = webdriver.Chrome(PATH)
# open Google Chrome with given URL
driver.get('https://orteil.dashnet.org/cookieclicker/')

# make driver wait implicitly
driver.implicitly_wait(15)

# getting all tags
cookie = driver.find_element_by_id('bigCookie')
cookie_count = driver. find_element_by_id('cookies')
items = [driver.find_element_by_id('productPrice' + str(i)) for i in range (1, -1, -1)]

# creating instance of action chains
actions = ActionChains(driver)
actions.click(cookie)

for x in range(5000):
    actions.perform()
    count = int(cookie_count.text.split(" ")[0])
    print(count)
    for item in items:
        value = int(item.text)
        if value <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()