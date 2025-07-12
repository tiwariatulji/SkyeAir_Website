from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    SEARCH_BOX = (By.ID, "search")

    def search(self, text):
        self.enter_text(self.SEARCH_BOX, text)




        teddf        self.submit_search()    def submit_search(self):
        search_button = (By.ID, "search-button")


        
