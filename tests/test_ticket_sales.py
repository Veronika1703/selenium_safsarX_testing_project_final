from pages.ticket_sales_page import TicketSales as Lp
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait

def test_ticket_sales_first_test(driver):
    base_url = 'https://portal-dev.safsarglobal.link/'
    driver.get(base_url)
    lp = Lp(driver)
    driver.get(base_url)
    lp.click_ticket_sales()
    time.sleep(10)