import unittest
from selenium import webdriver
import TestCase.page as page


# each class stands for a particular test case , inherit TestCase ,
# which will give access to certain methods
class PythonOrgSearch(unittest.TestCase):

    # setting up before every test case
    def setUp(self):
        PATH = 'C:\Program Files (x86)\chromedriver.exe'
        self.driver = webdriver.Chrome(PATH)
        self.driver.get("https://www.python.org/")

    def test_search_python(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()

        mainPage.search_text_element = "pycon"
        mainPage.click_go_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_results_found()

    # using test as a keyword will enable the function to be automatically be run
    def test_work(self):
        print(" Test ")
        assert True

    # runs after test case is finished
    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    # run all the unit tests that we have defined
    unittest.main()
