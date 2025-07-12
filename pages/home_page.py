from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    SEARCH_BOX = (By.ID, "search")

    def search(self, text):
        self.enter_text(self.SEARCH_BOX, text)
