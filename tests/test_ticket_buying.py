from operator import is_not
from re import search
from selenium.webdriver.common.keys import Keys
from pages.home_page import HomePage as Lp
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

def test_ticket_buying_1_1_1(driver):
    base_url = 'https://portal-dev.safsarglobal.link/'
    lp = Lp(driver)
    driver.get(base_url)
    assert "This site can’t be reached" not in driver.page_source, "The website failed to load (site unreachable)."
    assert "Error" not in driver.page_source, "Error message found on the website."
    assert "Exception" not in driver.page_source, "Exception found on the website."


def test_ticket_buying_2_1_1(driver):
    base_url = 'https://portal-dev.safsarglobal.link/'
    lp = Lp(driver)
    driver.get(base_url)



from playwright.sync_api import sync_playwright

def test_script_2_1_2_2_1_3_2_2_1_2_5_1():
    with sync_playwright() as p:
        # Launch browser and open a new page
        browser = p.chromium.launch(headless=False)  # Set headless=True for headless mode
        context = browser.new_context()
        page = context.new_page()

        # Navigate to the URL
        page.goto('https://portal-dev.safsarglobal.link/')

        # Interact with elements
        page.get_by_role('link', name='תיאטרון').click()
        page.get_by_role('link', name='Safsar X').click()
        page.get_by_role('combobox').click()
        page.get_by_role('combobox').fill('אושר כהן')
        page.get_by_role('link', name='Event Image היכל מנורה מבטחים | 14.8.24 | יום שלישי').click()
        page.get_by_role('link', name='Safsar X').click()
        page.get_by_role('link', name='מכבי תל אביב בר - מכבי פתח תקווה כדורסל - גמר גביע המדינה 8.3.25').click()
        page.get_by_text('אין מידע על ישיבה').first.click()

        # Close the browser
        browser.close()

# Ru0n the script
if __name__ == "_main_":
    test_ticket_buying_1_1_1()
