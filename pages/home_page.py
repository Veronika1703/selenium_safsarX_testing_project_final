from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    SEARCH_FIELD=(By.CLASS_NAME,'ant-select-selection-search-input')


    def click_search_field(self):
        self.click_element(self.SEARCH_FIELD)
