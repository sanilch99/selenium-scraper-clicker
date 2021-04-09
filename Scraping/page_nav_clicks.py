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

# we can search for elements on page using various methods, tags,class,name,id
# here we will use link text -> the text on a tags
link = driver.find_element_by_link_text("Python Programming")
# now to open that page we have to click
link.click()

# now we on a new screen hence we shall wait
try:
    # go to beginner pyhton tutorials
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT,"Beginner Python Tutorials"))
    )
    element.click()

    # go to get started
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "sow-button-19310003"))
    )
    element.click()
    time.sleep(2.5)

    # head back to home page
    driver.back()
    driver.back()
    driver.back()
    time.sleep(2.5)

    # go to next page
    driver.forward()
    driver.forward()
    time.sleep(2.5)

except:
    driver.quit()


