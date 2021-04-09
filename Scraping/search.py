from selenium import webdriver
# gives access to keys that will allow to type/click enter /esc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

PATH = 'C:\Program Files (x86)\chromedriver.exe'

# browser that we want to use is Chrome and the driver is stored in the PATH
driver = webdriver.Chrome(PATH)
# open Google Chrome with given URL
driver.get('https://www.techwithtim.net/')
# driver.title gives us the of the page opened
print(driver.title)

# the most common name to access is id/name/class//tag type
# selenium returns the first element it finds on the page / or search through all as well

# searching using name
search = driver.find_element_by_name("s")
# wipe the data off the input box
search.clear()
# the data that we want to type in the search bar
search.send_keys("test")
# pressing return / enter
search.send_keys(Keys.RETURN)

# we can printout the entire page source
# print(driver.page_source)

# doing an explicit wait here so as to wait until the presence of
# an element with id main is felt on the screen
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    # will give a list of all article tags
    articles = main.find_elements_by_tag_name('article')
    for article in articles:
        header = article.find_element_by_class_name('entry-summary')
        print(header.text)
finally:
    driver.quit()

time.sleep(10)
# driver.quit() exits from Google Chrome -> to close a tab we can use driver.close()
driver.quit()
