from selenium.webdriver.common.by import By
from .base_page import BasePage


class SingUp(BasePage):
    SINGUP_BUTTON_HOME=(By.XPATH,'//*[@id="signin2"]')
    USERNAME_FIELD_SING=(By.ID,'sign-username')
    PASSWORD_FIELD_SING=(By.ID,'sign-password')
    SINGUP_BUTTON=(By.CSS_SELECTOR,'#signInModal > div > div > div.modal-footer > button.btn.btn-primary')
    CLOSE_SING_BUTTON=(By.CSS_SELECTOR,'#signInModal > div > div > div.modal-footer > button.btn.btn-secondary')


    def click_singup_button(self):
        self.click_element(self.SINGUP_BUTTON_HOME)

    def enter_username(self,username):
        self.enter_text(self.USERNAME_FIELD_SING,username)

    def enter_password(self,password):
        self.enter_text(self.PASSWORD_FIELD_SING,password)

    def click_singup(self):
        self.click_element(self.SINGUP_BUTTON)

    def click_close(self):
        self.click_element(self.CLOSE_SING_BUTTON)

