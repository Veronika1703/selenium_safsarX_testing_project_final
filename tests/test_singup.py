from pages.singup_page import SingUp as Lp
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait


def test_valid_singup(driver):
    base_url = 'https://www.demoblaze.com/index.html'
    driver.get(base_url)
    lp = Lp(driver)
    driver.get(base_url)
    lp.click_singup_button()
    time.sleep(10)
    lp.enter_username('veronika2030')
    lp.enter_password('vera203050')
    lp.click_singup()
    time.sleep(10)
    wait = WebDriverWait(driver, 10)
    alert = wait.until(EC.alert_is_present())  # מחכה לאלרט
    assert alert.text == "Sign up successful."
    alert.accept()
    time.sleep(10)

def test_empty_username_and_password_singup(driver):
    base_url = 'https://www.demoblaze.com/index.html'
    driver.get(base_url)
    lp = Lp(driver)
    driver.get(base_url)
    lp.click_singup_button()
    time.sleep(10)
    lp.click_singup()
    wait = WebDriverWait(driver, 10)
    alert = wait.until(EC.alert_is_present())  # מחכה לאלרט
    assert alert.text == "Please fill out Username and Password."
    alert.accept()
    time.sleep(10)


def test_invalid_login_used_username(driver):
    base_url = 'https://www.demoblaze.com/index.html'
    driver.get(base_url)
    lp = Lp(driver)
    driver.get(base_url)
    lp.click_singup_button()
    time.sleep(10)
    lp.enter_username('veronika170300')
    lp.enter_password('vera170300')
    lp.click_singup()
    time.sleep(10)
    wait = WebDriverWait(driver, 10)
    alert = wait.until(EC.alert_is_present())  # מחכה לאלרט
    assert alert.text == "This user already exist."
    alert.accept()

def test_singup_new_user_used_password(driver):
    base_url = 'https://www.demoblaze.com/index.html'
    driver.get(base_url)
    lp = Lp(driver)
    driver.get(base_url)
    lp.click_singup_button()
    time.sleep(10)
    lp.enter_username('veronika177777')
    lp.enter_password('vera170300')
    lp.click_singup()
    time.sleep(10)
    wait = WebDriverWait(driver, 10)
    alert = wait.until(EC.alert_is_present())  # מחכה לאלרט
    assert alert.text == "Sign up successful."
    alert.accept()

def test_singup_long_user_long_password(driver):
    base_url = 'https://www.demoblaze.com/index.html'
    driver.get(base_url)
    lp = Lp(driver)
    driver.get(base_url)
    lp.click_singup_button()
    time.sleep(10)
    lp.enter_username('veronikaveronikaveronikaveronikaveronikaveronika')
    lp.enter_password('veronikaveronikaveronikaveronikaveronikaveronika')
    lp.click_singup()
    time.sleep(10)
    wait = WebDriverWait(driver, 10)
    alert = wait.until(EC.alert_is_present())  # מחכה לאלרט
    assert alert.text == "A username cannot contain more than 10 threads and passwors cannot contain more than 12 threads "
    alert.accept()

def test_onechar__user_and_password(driver):
    base_url = 'https://www.demoblaze.com/index.html'
    driver.get(base_url)
    lp = Lp(driver)
    driver.get(base_url)
    lp.click_singup_button()
    time.sleep(10)
    lp.enter_username('veronika5080907777')
    lp.enter_password('0000')
    lp.click_singup()
    time.sleep(10)
    wait = WebDriverWait(driver, 10)
    alert = wait.until(EC.alert_is_present())  # מחכה לאלרט
    assert alert.text == "Your password is too easy"
    alert.accept()