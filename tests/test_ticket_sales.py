from pages.ticket_sales_page import TicketSales as Lp
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait

def test_login_process_4_2_1(driver):
    base_url = 'https://portal-dev.safsarglobal.link/'
    driver.get(base_url)
    lp = Lp(driver)
    driver.get(base_url)
    lp.click_ticket_seling_home()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(lp.TICKET_SELING_LOGIN_HEADER))
    lp.click_login_button_after_ticket_seling()
    phone_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(lp.INPUT_PHONE_NUMBER))
    assert phone_input.is_displayed()