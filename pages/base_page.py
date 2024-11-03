from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """class to represent the base page that other pages can inherit from"""
    def __init__(self,driver:WebDriver):
        self.driver=driver
    def find_element(self, locator):
        return WebDriverWait(self.driver,10).until(EC.presence_of_element_located(locator))
    def click_element(self,locator):
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located(locator)).click()
    def enter_text(self,locator,text):
        element=self.find_element(locator)
        element.clear()
        element.send_keys(text)


