# each page inside a class for better code, more selenium code
# import everything from locators
from TestCase.locator import *
from TestCase.element import BasePageElement

# inherit all the functionality from basepage element
class SearchTextElement(BasePageElement):
    # will use this locator
    locator = "q"


# inheritance object is optional
class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

# inherits from BasePage hence init is used from BasePage
class MainPage(BasePage):

    # when this search_text_element = 5, set method is called
    # 5 is sent as the value , MainPage is sent
    # as object , object.driver is the inherited driver , locator is defined inside the
    # search text element class

    # similarly if we do x = search_text_element , get method is called

    # this is a descriptor
    search_text_element = SearchTextElement()


    # check if title matches
    def is_title_matches(self):
        # whether or not string Python is in the driver or not
        return  "Python" in self.driver.title

    def click_go_button(self):
        # search using locator defined in locators.py
        # unpack the tuple using a * therefore changing (1,2)-> 1 object
        # to 1 , 2 -> 2 objects
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()

class SearchResultPage(BasePage):

    def is_results_found(self):
        # if the given string doesnt exist then return true else false
        return "No results found." not in self.driver.page_source

