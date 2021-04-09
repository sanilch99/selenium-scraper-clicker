# will represent a certain element from a page

from selenium.webdriver.support.ui import WebDriverWait

class BasePageElement(object):

    # SETTING THE VALUE
    # for any element that we want to set the value for we use these sets
    def __set__(self, obj, value):
        driver = obj.driver
        # wait until the lamda is true, driver is the element
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator))
        driver.find_element_by_name(self.locator).clear()
        driver.find_element_by_name(self.locator).send_keys(value)

    # GETTING THE VALUE
    # anytime we try to access value of element, automatically implement these steps
    def __get__(self, obj, owner):
        driver = obj.driver
        # wait until the lamda is true, driver is the element
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator))
        element = driver.find_element_by_name(self.locator)
        return element.get_attribute('value')
