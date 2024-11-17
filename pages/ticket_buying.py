from selenium.webdriver.common.by import By
from .base_page import BasePage

CHOSEN_TICKETS_INFO = (By.CSS_SELECTOR, "#root > main > div.lg\:flex > div.md\:h-\[88vh\].w-full.md\:w-3\/4.md\:p-4.md\:overflow-y-auto > div > div > div.flex.md\:mx-12.md\:my-12.p-4.md\:p-0")
CANCEL_TICKETS = (By.CSS_SELECTOR, "#root > main > div.lg\:flex > div.md\:h-\[88vh\].w-full.md\:w-3\/4.md\:p-4.md\:overflow-y-auto > div > div > div.md\:mx-12.md\:mt-16 > p.w-full.md\:w-\[402px\].pr-2.bg-secondaryYellow.-mt-4.mb-4.md\:mb-0.text-\[14px\].text-center > span")
NEXT_BUTTON = (By.CSS_SELECTOR, "#root > main > div.lg\:flex > div.md\:h-\[88vh\].w-full.md\:w-3\/4.md\:p-4.md\:overflow-y-auto > div > div > div.flex.md\:justify-end.flex-col.md\:flex-row.md\:mx-8.bottom-0 > button")
PHONE_NUMBER_VIR = (By.CSS_SELECTOR, "#root > main > div.lg\:flex > div.md\:h-\[88vh\].w-full.md\:w-3\/4.md\:p-4.md\:overflow-y-auto > div > div > div.fixed.inset-0.flex.items-center.justify-center.z-50 > div.modal.w-\[350px\].h-\[500px\].md\:w-\[570px\].md\:h-\[500px\].p-4.bg-systemLight.rounded-lg.shadow-lg.text-center.relative.flex.flex-col.items-center")
ENTER_CODE = (By.CSS_SELECTOR, "#root > main > div.lg\:flex > div.md\:h-\[88vh\].w-full.md\:w-3\/4.md\:p-4.md\:overflow-y-auto > div > div > div.fixed.inset-0.flex.items-center.justify-center.z-50 > div.modal.w-\[350px\].h-\[500px\].md\:w-\[570px\].md\:h-\[500px\].p-4.bg-systemLight.rounded-lg.shadow-lg.text-center.relative.flex.flex-col.items-center > form > input")
OK_BUTTON = (By.CSS_SELECTOR, "#root > main > div.lg\:flex > div.md\:h-\[88vh\].w-full.md\:w-3\/4.md\:p-4.md\:overflow-y-auto > div > div > div.fixed.inset-0.flex.items-center.justify-center.z-50 > div.modal.w-\[350px\].h-\[500px\].md\:w-\[570px\].md\:h-\[500px\].p-4.bg-systemLight.rounded-lg.shadow-lg.text-center.relative.flex.flex-col.items-center > form > button")
SEND_AGAIN = (By.XPATH, "#root > main > div.lg\:flex > div.md\:h-\[88vh\].w-full.md\:w-3\/4.md\:p-4.md\:overflow-y-auto > div > div > div.fixed.inset-0.flex.items-center.justify-center.z-50 > div.modal.w-\[350px\].h-\[500px\].md\:w-\[570px\].md\:h-\[500px\].p-4.bg-systemLight.rounded-lg.shadow-lg.text-center.relative.flex.flex-col.items-center > button")
PAYMENT_INFO = (By.CSS_SELECTOR, "#root > main > div.lg\:flex > div.md\:h-\[88vh\].w-full.md\:w-3\/4.md\:p-4.md\:overflow-y-auto > div > div > h2")
CARD_NUB_BOX = (By.CSS_SELECTOR, "#cardNumber")
EXP_MONTH_LIST = (By.CSS_SELECTOR, "#expmonth")
EXP_YEAR_LIST = (By.CSS_SELECTOR, "#expyear")
SECURITY_CODE_BOX = (By.CSS_SELECTOR, "#mycvv")
QUESTION_BUTTON = (By.CSS_SELECTOR, "#myBtn")
TOTAL_PRICE = (By.CSS_SELECTOR, "#total_sum")
PAY_BUTTON = (By.CSS_SELECTOR, "#submitbtn")
PAY_WITH_PAYPAL = (By.CSS_SELECTOR, "#payPaypal")
TIME_UP = (By.CSS_SELECTOR, "#root > main > div.lg\:flex > div.md\:h-\[88vh\].w-full.md\:w-3\/4.md\:p-4.md\:overflow-y-auto > div > div > div.fixed.inset-0.flex.items-center.justify-center.z-50 > div.modal.w-\[350px\].h-\[500px\].md\:w-\[570px\].md\:h-\[500px\].p-4.bg-systemLight.rounded-lg.shadow-lg.text-center.relative.flex.flex-col.items-center > button")
COMPLETE_PURCHASE = (By.CSS_SELECTOR, "#root > main > div.lg\:flex > div.md\:h-\[88vh\].w-full.md\:w-3\/4.md\:p-4.md\:overflow-y-auto > div > div > div.fixed.inset-0.flex.items-center.justify-center.z-50 > div.modal.w-\[350px\].h-\[407px\].md\:w-\[570px\].md\:h-\[400px\].p-4.bg-systemLight.rounded-lg.shadow-lg.text-center.relative.flex.flex-col.items-center > div.w-full.flex.flex-col.md\:hidden > button.md\:w-\[200px\].m-4.text-lg.bg-primaryPurple.text-white.font-bold.p-2.rounded-full.auth-button")
CANCEL_PURCHASE = (By.CSS_SELECTOR, "#root > main > div.lg\:flex > div.md\:h-\[88vh\].w-full.md\:w-3\/4.md\:p-4.md\:overflow-y-auto > div > div > div.fixed.inset-0.flex.items-center.justify-center.z-50 > div.modal.w-\[350px\].h-\[407px\].md\:w-\[570px\].md\:h-\[400px\].p-4.bg-systemLight.rounded-lg.shadow-lg.text-center.relative.flex.flex-col.items-center > div.w-full.flex.flex-col.md\:hidden > button.md\:w-\[200px\].m-4.text-lg.border.border-primaryDark.border-solid.text-primaryDark.font-bold.p-2.rounded-full.auth-button")

def chosen_tickets_info(self):
    self.find_element(self.CHOSEN_TICKETS_INFO)

def cancel_tickets(self):
    self.click_element(self.CANCEL_TICKETS)

def next_button(self):
    self.click_element(self.NEXT_BUTTON)

def Phone_number_verification(self):
    self.find_element(self.PHONE_NUMBER_VIR)

def enter_code(self):
    self.click_element(self.ENTER_CODE)

def ok_button(self):
    self.click_element(self.OK_BUTTON)

def send_again(self):
    self.click_element(self.SEND_AGAIN)

def payment_info(self):
    self.find_element(self.PAYMENT_INFO)

def card_num_box(self):
    self.click_element(self.CARD_NUB_BOX)

def exp_month(self):
    self.click_element(self.EXP_MONTH_LIST)

def exp_year(self):
    self.click_element(self.EXP_YEAR_LIST)

def security_code(self):
    self.click_element(self.SECURITY_CODE_BOX)

def question_button(self):
    self.click_element(self.QUESTION_BUTTON)

def total_price(self):
    self.find_element(self.TOTAL_PRICE)

def pay_button(self):
    self.click_element(self.PAY_BUTTON)

def pay_with_paypal(self):
    self.click_element(self.PAY_WITH_PAYPAL)

def time_up(self):
    self.find_element(self.TIME_UP)

def complete_purchase(self):
    self.click_element(self.COMPLETE_PURCHASE)
