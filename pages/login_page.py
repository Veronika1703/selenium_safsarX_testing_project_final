from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):
    LOGIN_BUTTON_HOME = (By.XPATH, '//*[@id="login2"]')
    USERNAME_FIELD=(By.ID,'loginusername')
    PASSWORD_FIELD=(By.ID,'loginpassword')
    LOGIN_BUTTON=(By.CSS_SELECTOR,'#logInModal > div > div > div.modal-footer > button.btn.btn-primary')
    CLOSE_BUTTON=(By.CSS_SELECTOR,'#logInModal > div > div > div.modal-footer > button.btn.btn-secondary')
    WELCOME_USERNAME=(By.ID,'nameofuser')
    LOGOUT_BUTTON=(By.ID,'logout2')

    def click_login_home(self):
        self.click_element(self.LOGIN_BUTTON_HOME)

    def enter_username(self,username):
        self.enter_text(self.USERNAME_FIELD,username)

    def enter_password(self,password):
        self.enter_text(self.PASSWORD_FIELD,password)

    def click_login(self):
        self.click_element(self.LOGIN_BUTTON)

    def click_close(self):
        self.click_element(self.CLOSE_BUTTON)

    def click_logout(self):
        self.click_element(self.LOGOUT_BUTTON)