from selenium.webdriver.common.by import By
from .base_page import BasePage

class TicketSales(BasePage):
    TICKET_SALES_HOME=(By.CSS_SELECTOR,'#root > div.w-full.navbar.bg-primaryDark.bg-primaryDark.sm\:px-16.px-6.flex.justify-center.items-center.z-30 > div > nav > p')


    def click_ticket_sales(self):
        self.click_element(self.TICKET_SALES_HOME)