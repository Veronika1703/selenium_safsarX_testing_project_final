from pages.login_page import LoginPage as Lp
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait

def test_valid_login(driver):
    base_url = 'https://www.demoblaze.com/index.html'
    driver.get(base_url)
    lp = Lp(driver)
    driver.get(base_url)
    lp.click_login_home()
    time.sleep(10)
    lp.enter_username('veronika170300')
    lp.enter_password('vera170300')
    lp.click_login()
    time.sleep(10)
    welcome_message = driver.find_element(*lp.WELCOME_USERNAME).text
    assert welcome_message == "Welcome veronika170300"
    assert driver.find_element(*lp.LOGOUT_BUTTON).is_displayed()
    lp.click_logout()
    time.sleep(10)
   # assert driver.current_url == "https://www.demoblaze.com/index.html"

def test_empty_username_and_password(driver):
    base_url = 'https://www.demoblaze.com/index.html'
    driver.get(base_url)
    lp = Lp(driver)
    driver.get(base_url)
    lp.click_login_home()
    time.sleep(10)
    lp.click_login()
    wait = WebDriverWait(driver, 10)
    alert = wait.until(EC.alert_is_present())  # מחכה לאלרט
    assert alert.text == "Please fill out Username and Password."
    time.sleep(5)
    alert.accept()
    time.sleep(10)

def test_invalid_login_incorrect_username(driver):
    base_url = 'https://www.demoblaze.com/index.html'
    driver.get(base_url)
    lp = Lp(driver)
    driver.get(base_url)
    lp.click_login_home()
    time.sleep(10)
    lp.enter_username('ver')
    lp.enter_password('vera170300')
    lp.click_login()
    time.sleep(10)
    wait = WebDriverWait(driver, 10)
    alert = wait.until(EC.alert_is_present())  # מחכה לאלרט
    assert alert.text == "User does not exist."
    alert.accept()


def test_invalid_login_incorrect_password(driver):
    base_url = 'https://www.demoblaze.com/index.html'
    driver.get(base_url)
    lp = Lp(driver)
    driver.get(base_url)
    lp.click_login_home()
    time.sleep(10)
    lp.enter_username('veronika170300')
    lp.enter_password('123456')
    lp.click_login()
    time.sleep(10)
    wait = WebDriverWait(driver, 10)
    alert = wait.until(EC.alert_is_present())  # מחכה לאלרט
    assert alert.text == "Wrong password."
    alert.accept()

def test_invalid_login_incorrect_username_and_password(driver):
    base_url = 'https://www.demoblaze.com/index.html'
    driver.get(base_url)
    lp = Lp(driver)
    driver.get(base_url)
    lp.click_login_home()
    time.sleep(10)
    lp.enter_username('ver')
    lp.enter_password('123456')
    lp.click_login()
    time.sleep(10)
    wait = WebDriverWait(driver, 10)
    alert = wait.until(EC.alert_is_present())  # מחכה לאלרט
    assert alert.text == "User does not exist."
    alert.accept()

def test_close_button(driver):
    base_url = 'https://www.demoblaze.com/index.html'
    driver.get(base_url)
    lp = Lp(driver)
    driver.get(base_url)
    lp.click_login_home()
    time.sleep(10)
    lp.enter_username('veronika170300')
    lp.enter_password('vera170300')
    time.sleep(3)
    lp.click_close()
    time.sleep(10)


