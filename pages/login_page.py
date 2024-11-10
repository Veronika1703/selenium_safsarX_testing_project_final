from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):
    LOGIN_BUTTON_HOME = (By.CSS_SELECTOR, '#root > div.w-full.navbar.bg-primaryDark.bg-primaryDark.sm\:px-16.px-6.flex.justify-center.items-center.z-30 > div > nav > div:nth-child(1) > ul > a')

    def click_login_home(self):
        self.click_element(self.LOGIN_BUTTON_HOME)

