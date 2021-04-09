# any css selector , any id we should keep in one location
# allowing for code reusability

from selenium.webdriver.common.by import By

# make classes that represent object that we wanna find
# CONSTANT = ( how u wanna access , property )

# all the main class locators shall be here
class MainPageLocators(object):
    GO_BUTTON = (By.ID, "submit")


# will add stuff later on in this class
class SearchResultsPageLocators(object):
    pass

