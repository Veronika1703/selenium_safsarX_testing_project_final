from selenium.webdriver.common.by import By
from .base_page import BasePage

class TicketSales(BasePage):
    TIKET_SELING_HOME_BUTTON=(By.CSS_SELECTOR,'#root > div.w-full.navbar.bg-primaryDark.bg-primaryDark.sm\:px-16.px-6.flex.justify-center.items-center.z-30 > div > nav > p')
    LOGIN_BUTTON_HOME = (By.CSS_SELECTOR, '#root > div.w-full.navbar.bg-primaryDark.bg-primaryDark.sm\:px-16.px-6.flex.justify-center.items-center.z-30 > div > nav > div:nth-child(1) > ul > a')
    INPUT_PHONE_NUMBER=(By.XPATH,'//*[@id="root"]/main/div/div[2]/div/form/input')
    ENTER_BUTTON=(By.CSS_SELECTOR,'#root > main > div > div.h-\[91\.4vh\].md\:h-\[88vh\].grid.grid-cols-2.bg-primaryDark.text-white.gap-4.auth-content > div > form > button')
    ENTER_OTP_CODE=(By.XPATH,'//*[@id="root"]/main/div/div[2]/div/form/input')
    SUBMIT_BUTTON=(By.CSS_SELECTOR,'#root > main > div > div.h-\[91\.4vh\].md\:h-\[88vh\].grid.grid-cols-2.bg-primaryDark.text-white.gap-4.auth-content > div > form > button')
    MY_ACAUNT_HOME_BUTTON=(By.CSS_SELECTOR,'#root > div.w-full.navbar.bg-primaryDark.sm\:px-16.px-6.flex.justify-center.items-center.z-30 > div > nav > div:nth-child(1) > ul > button')
    CAT_TEATRON_BUTTON = (By.CSS_SELECTOR,
                          '#root > div.bg-primary.w-full.max-h-max.home.pt-12.md\:pt-0 > div.bg-systemLight.md\:bg-primaryDark.flex.justify-center.items-start > div > div > div.hiddenScrollbar.flex.justify-between.overflow-x-auto.pl-0.ml-0.md\:space-x-4 > a.font-Zvulun.md\:w-\[180px\].md\:h-\[62px\].flex.items-center.justify-center.text-PrimaryDark.md\:text-white.text-\[22\.92px\].md\:text-lg.lg\:text-4xl.pl-1.md\:px-4.py-2.m-1.md\:my-2.md\:ml-2.transition.duration-300.ease-in-out.transform.hover\:border-primaryPurple.hover\:animate-border-anticlockwise.hover\:rounded-full > span')
    TEATRON_HEADER = (By.CSS_SELECTOR,
                      '#root > main > div.flex.flex-col.h-full.py-8.w-full.md\:max-w-\[1355px\].mx-auto > div.sm\:px-16.px-6.grid.grid-cols-3.md\:grid-cols-3.gap-4.px-4.md\:px-2 > div.col-span-2.md\:col-span-1 > h1')
    CAT_MUSIC_BUTTON = (By.CSS_SELECTOR,
                        '#root > div.bg-primary.w-full.max-h-max.home.pt-12.md\:pt-0 > div.bg-systemLight.md\:bg-primaryDark.flex.justify-center.items-start > div > div > div.hiddenScrollbar.flex.justify-between.overflow-x-auto.pl-0.ml-0.md\:space-x-4 > a.font-Zvulun.md\:w-\[160px\].md\:h-\[62px\].flex.items-center.justify-center.text-PrimaryDark.md\:text-white.text-\[22\.92px\].md\:text-lg.lg\:text-4xl.px-1.md\:px-4.py-2.m-1.md\:m-2.transition.duration-300.ease-in-out.transform.hover\:border-secondaryBlue.hover\:animate-border-anticlockwise > span')
    MUSIC_HEADER = (By.CSS_SELECTOR,
                    '#root > main > div.flex.flex-col.h-full.py-8.w-full.md\:max-w-\[1355px\].mx-auto > div.sm\:px-16.px-6.grid.grid-cols-3.md\:grid-cols-3.gap-4.px-4.md\:px-2 > div.col-span-2.md\:col-span-1 > h1')
    CAT_SPORT_BUTTON = (By.CSS_SELECTOR,
                        '#root > div.bg-primary.w-full.max-h-max.home.pt-12.md\:pt-0 > div.bg-systemLight.md\:bg-primaryDark.flex.justify-center.items-start > div > div > div.hiddenScrollbar.flex.justify-between.overflow-x-auto.pl-0.ml-0.md\:space-x-4 > a.font-Zvulun.md\:w-\[160px\].md\:h-\[62px\].flex.items-center.justify-center.text-PrimaryDark.md\:text-white.text-\[22\.92px\].md\:text-lg.lg\:text-4xl.px-1.md\:px-4.py-2.m-1.md\:m-2.transition.duration-300.ease-in-out.transform.hover\:border-primaryGreen.hover\:animate-border-anticlockwise > span')
    SPORT_HEADER = (By.CSS_SELECTOR,
                    '#root > main > div.flex.flex-col.h-full.py-8.w-full.md\:max-w-\[1355px\].mx-auto > div.sm\:px-16.px-6.grid.grid-cols-3.md\:grid-cols-3.gap-4.px-4.md\:px-2 > div.col-span-2.md\:col-span-1 > h1')
    CAT_STENDUP_BUTTON = (By.CSS_SELECTOR,
                          '#root > div.bg-primary.w-full.max-h-max.home.pt-12.md\:pt-0 > div.bg-systemLight.md\:bg-primaryDark.flex.justify-center.items-start > div > div > div.hiddenScrollbar.flex.justify-between.overflow-x-auto.pl-0.ml-0.md\:space-x-4 > a.font-Zvulun.md\:w-\[210px\].md\:h-\[62px\].flex.items-center.justify-center.text-PrimaryDark.md\:text-white.text-\[22\.92px\].md\:text-lg.lg\:text-4xl.px-1.md\:px-4.py-2.m-1.md\:m-2.transition.duration-300.ease-in-out.transform.hover\:border-secondaryOrange.hover\:animate-border-anticlockwise > span')
    STENDUP_HEADER = (By.CSS_SELECTOR,
                      '#root > main > div.flex.flex-col.h-full.py-8.w-full.md\:max-w-\[1355px\].mx-auto > div.sm\:px-16.px-6.grid.grid-cols-3.md\:grid-cols-3.gap-4.px-4.md\:px-2 > div.col-span-2.md\:col-span-1 > h1')
    CAT_KIDS_BUTTON = (By.CSS_SELECTOR,
                       '#root > div.bg-primary.w-full.max-h-max.home.pt-12.md\:pt-0 > div.bg-systemLight.md\:bg-primaryDark.flex.justify-center.items-start > div > div > div.hiddenScrollbar.flex.justify-between.overflow-x-auto.pl-0.ml-0.md\:space-x-4 > a.font-Zvulun.md\:w-\[130px\].md\:h-\[62px\].flex.items-center.justify-center.text-PrimaryDark.md\:text-white.text-\[22\.92px\].md\:text-lg.lg\:text-4xl.pr-1.pl-2.md\:px-6.py-2.m-1.md\:m-2.transition.duration-300.ease-in-out.transform.hover\:border-secondaryYellow.hover\:animate-border-anticlockwise > span')
    KIDS_HEADER = (By.CSS_SELECTOR,
                   '#root > main > div.flex.flex-col.h-full.py-8.w-full.md\:max-w-\[1355px\].mx-auto > div.sm\:px-16.px-6.grid.grid-cols-3.md\:grid-cols-3.gap-4.px-4.md\:px-2 > div.col-span-2.md\:col-span-1 > h1')
    SAFSAR_LOGO_BUTTON = (By.CSS_SELECTOR,
                          '#root > main > div.w-full.navbar.bg-primaryLight.sm\:px-16.px-6.flex.justify-center.items-center.z-30 > div > nav > div.hidden.md\:flex.space-x-10.md\:w-\[500px\] > a > img')
    SIGHNUP_BUTTON_TICKET_SELING=(By.CSS_SELECTOR,'#root > main > div > div.h-\[91\.4vh\].md\:h-\[88vh\].grid.grid-cols-1.md\:grid-cols-2.bg-primaryDark.text-white.gap-4.auth-content > div.w-full.md\:w-\[704px\].col-span-1.md\:col-span-1.flex.flex-col.text-center.justify-center.items-center.px-4.auth.undefined > button:nth-child(4)')
    TICKET_SELING_LOGIN_HEADER=(By.CSS_SELECTOR,'#root > main > div > div.h-\[91\.4vh\].md\:h-\[88vh\].grid.grid-cols-1.md\:grid-cols-2.bg-primaryDark.text-white.gap-4.auth-content > div.w-full.md\:w-\[704px\].col-span-1.md\:col-span-1.flex.flex-col.text-center.justify-center.items-center.px-4.auth.undefined > h2')
    SIGHNUP_FIELD=(By.XPATH,'//*[@id="root"]/main/div[2]/div/div/form/input')
    LOGIN_BUTTON_TICKET_SELING =(By.CSS_SELECTOR,'#root > main > div > div.h-\[91\.4vh\].md\:h-\[88vh\].grid.grid-cols-1.md\:grid-cols-2.bg-primaryDark.text-white.gap-4.auth-content > div.w-full.md\:w-\[704px\].col-span-1.md\:col-span-1.flex.flex-col.text-center.justify-center.items-center.px-4.auth.undefined > button:nth-child(5)')







    def click_login_home(self):
        self.click_element(self.LOGIN_BUTTON_HOME)
    def click_enter_button(self):
        self.click_element(self.ENTER_BUTTON)

    def enter_otp_code(self, otp_code):
        otp_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.ENTER_OTP_CODE))
        otp_input.clear()  # מנקה שדה קיים במקרה הצורך
        otp_input.send_keys(otp_code)  # מזין את קוד ה-OTP בשדה
    def click_submit_button(self):
        self.click_element(self.SUBMIT_BUTTON)
    def click_cat_teatron_button(self):
        self.click_element(self.CAT_TEATRON_BUTTON)
    def click_cat_music_button(self):
        self.click_element(self.CAT_MUSIC_BUTTON)
    def click_cat_sport_button(self):
        self.click_element(self.CAT_SPORT_BUTTON)
    def click_cat_stendup_button(self):
        self.click_element(self.CAT_STENDUP_BUTTON)
    def click_cat_kids_button(self):
        self.click_element(self.CAT_KIDS_BUTTON)
    def click_safsar_logo(self):
        self.click_element(self.SAFSAR_LOGO_BUTTON)
    def click_ticket_seling_home(self):
        self.click_element(self.TIKET_SELING_HOME_BUTTON)
    def click_sighnup_button_after_ticket_seling(self):
        self.click_element(self.SIGHNUP_BUTTON_TICKET_SELING)
    def click_login_button_after_ticket_seling(self):
        self.click_element(self.LOGIN_BUTTON_TICKET_SELING)