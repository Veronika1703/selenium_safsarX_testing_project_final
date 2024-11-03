from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    LOGO=(By.ID,'nava')
    HOME_BUTTOM=(By.CSS_SELECTOR,'#navbarExample > ul > li.nav-item.active > a')
    CONTACTS_BUTTON=(By.XPATH,'//*[@id="navbarExample"]/ul/li[2]/a')
    ABOUTUS_BUTTON=(By.XPATH,'//*[@id="navbarExample"]/ul/li[3]/a')
    CART_BUTTON=(By.XPATH,'//*[@id="cartur"]')
    LOGIN_BUTTON=(By.XPATH,'//*[@id="login2"]')
    SINGUP_BUTTON=(By.XPATH,'//*[@id="signin2"]')
    LEFT_ARROW_BUTTON=(By.XPATH,'//*[@id="carouselExampleIndicators"]/a[1]/span[1]')
    RIGHT_ARROW_BUTTON=(By.XPATH,'//*[@id="carouselExampleIndicators"]/a[2]/span[1]')
    PICK_SLIDE1=(By.XPATH,'/html/body/nav/div[2]/div/div/div[1]/img')
    PICK_SLIDE2 = (By.XPATH, '/html/body/nav/div[2]/div/div/div[2]/img')
    PICK_SLIDE3 = (By.XPATH, '/html/body/nav/div[2]/div/div/div[3]/img')
    CATEGORIES_PHONES_BUTTON=(By.XPATH,'/html/body/div[5]/div/div[1]/div/a[2]')
    CATEGORIES_LAPTOPS_BUTTON = (By.XPATH,'/html/body/div[5]/div/div[1]/div/a[3]')
    CATEGORIES_MONITORS_BUTTON = (By.XPATH, '/html/body/div[5]/div/div[1]/div/a[4]')
    PIC_SAMSUNG_GALACSY_S6=(By.XPATH,'/html/body/div[5]/div/div[2]/div/div[1]/div/a/img')
    HEADER_SAMSUNG_GALACSY_S6=(By.XPATH,'/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a')
    DESCRIPTION_SAMSUNG_GALACSY_S6=(By.XPATH,'/html/body/div[5]/div/div[2]/div/div[1]/div/div/p')
    PIC_NOKIA_LUMIA_1520=(By.XPATH,'/html/body/div[5]/div/div[2]/div/div[1]/div/a/img')
    HEADER_NOKIA_LUMIA_1520=(By.XPATH,'/html/body/div[5]/div/div[2]/div/div[2]/div/div/h4/a')
    DESCRIPTION_NOKIA_LUMIA_1520 = (By.XPATH, '/html/body/div[5]/div/div[2]/div/div[2]/div/div/p')
    PIC_NEXUS_6=(By.XPATH,'/html/body/div[5]/div/div[2]/div/div[2]/div/a/img')
    HEADER_NEXUS_6=(By.XPATH,'/html/body/div[5]/div/div[2]/div/div[3]/div/div/h4/a')
    DESCRIPTION_NEXUS_6 = (By.XPATH, '/html/body/div[5]/div/div[2]/div/div[3]/div/div/p')
    PIC_SAMSUNGGALUCSY_S7=(By.XPATH,'/html/body/div[5]/div/div[2]/div/div[3]/div/a/img')
    HEADER_SAMSUNGGALUCSY_S7=(By.XPATH,'/html/body/div[5]/div/div[2]/div/div[4]/div/div/h4/a')
    DESCRIPTION_SAMSUNGGALUCSY_S7 = (By.XPATH, '/html/body/div[5]/div/div[2]/div/div[4]/div/div/p')
    PIC_IPHON6_32g=(By.XPATH,'/html/body/div[5]/div/div[2]/div/div[4]/div/a/img')
    HEADER_IPHON6_32g=(By.XPATH,'/html/body/div[5]/div/div[2]/div/div[5]/div/div/h4/a')
    DESCRIPTION_IPHON6_32g = (By.XPATH, '/html/body/div[5]/div/div[2]/div/div[5]/div/div/p')
    PIC_SONY_XPERIA_Z5=(By.XPATH,'/html/body/div[5]/div/div[2]/div/div[5]/div/a/img')
    HEADER_SONY_XPERIA_Z5=(By.XPATH,'/html/body/div[5]/div/div[2]/div/div[6]/div/div/h4/a')
    DESCRIPTION_SONY_XPERIA_Z5 = (By.XPATH, '/html/body/div[5]/div/div[2]/div/div[6]/div/div/p')
    PIC_HTC_ONE_M9=(By.XPATH,'/html/body/div[5]/div/div[2]/div/div[6]/div/a/img')
    HEADER_HTC_ONE_M9=(By.XPATH,'/html/body/div[5]/div/div[2]/div/div[7]/div/div/h4/a')
    DESCRIPTION_HTC_ONE_M9 = (By.XPATH, '/html/body/div[5]/div/div[2]/div/div[7]/div/div/p')
    PIC_SONY_VAIO_I5=(By.XPATH,'/html/body/div[5]/div/div[2]/div/div[1]/div/a/img')
    HEADER_SONY_VAIO_I5=(By.XPATH,'/html/body/div[5]/div/div[2]/div/div[8]/div/div/h4/a')
    DESCRIPTION_SONY_VAIO_I5 = (By.XPATH, '/html/body/div[5]/div/div[2]/div/div[8]/div/div/p')
    PIC_SONY_VAIO_I7 = (By.XPATH, '/html/body/div[5]/div/div[2]/div/div[2]/div/a/img')
    HEADER_SONY_VAIO_I7 = (By.XPATH, '/html/body/div[5]/div/div[2]/div/div[9]/div/div/h4/a')
    DESCRIPTION_SONY_VAIO_I7 = (By.XPATH, '/html/body/div[5]/div/div[2]/div/div[9]/div/div/p')
    PIC_APPLE_MONITOR_24=(By.XPATH,'/html/body/div[5]/div/div[2]/div/div[1]/div/a/img')
    HEADER_APPLE_MONITOR_24=(By.XPATH,'/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a')
    DESCRIPTION_APPLE_MONITOR_24 = (By.XPATH, '/html/body/div[5]/div/div[2]/div/div[1]/div/div/p')
    PIC_MACBOOK_AIR=(By.XPATH,'/html/body/div[5]/div/div[2]/div/div[3]/div/a/img')
    HEADER_MACBOOK_AIR=(By.XPATH,'/html/body/div[5]/div/div[2]/div/div[2]/div/div/h4/a')
    DESCRIPTION_MACBOOK_AIR = (By.XPATH, '/html/body/div[5]/div/div[2]/div/div[2]/div/div/p')
    PIC_DELL_I7_8GB=(By.XPATH,'/html/body/div[5]/div/div[2]/div/div[4]/div/a/img')
    HEADER_DELL_I7_8GB=(By.XPATH,'/html/body/div[5]/div/div[2]/div/div[3]/div/div/h4/a')
    DESCRIPTION_DELL_I7_8GB = (By.XPATH, '/html/body/div[5]/div/div[2]/div/div[3]/div/div/p')
    PIC_2017_DELL_156_INCH=(By.XPATH,'/html/body/div[5]/div/div[2]/div/div[5]/div/a/img')
    HEADER_2017_DELL_156_INCH=(By.XPATH,'/html/body/div[5]/div/div[2]/div/div[4]/div/div/h4/a')
    DESCRIPTION_2017_DELL_156_INCH = (By.XPATH, '/html/body/div[5]/div/div[2]/div/div[4]/div/div/p')
    PIC_ASUS_FULL_HD=(By.XPATH,'/html/body/div[5]/div/div[2]/div/div[2]/div/a/img')
    HEADER_ASUS_FULL_HD=(By.XPATH,'/html/body/div[5]/div/div[2]/div/div[5]/div/div/h4/a')
    DESCRIPTION_ASUS_FULL_HD = (By.XPATH, '/html/body/div[5]/div/div[2]/div/div[5]/div/div/p')
    PIC_MACBOOK_PRO=(By.XPATH,'/html/body/div[5]/div/div[2]/div/div[6]/div/a/img')
    HEADER_MACBOOK_PRO=(By.XPATH,'/html/body/div[5]/div/div[2]/div/div[6]/div/div/h4/a')
    DESCRIPTION_MACBOOK_PRO = (By.XPATH, '/html/body/div[5]/div/div[2]/div/div[6]/div/div/p')
    NEXT_BUTTON=(By.ID,'next2')
    PREVIOUS_BUTTON=(By.ID,'prev2')
    CLOSE_CONTACTS_BUTTON=(By.XPATH,'/html/body/div[1]/div/div/div[3]/button[1]')
    CLOSE_ABOUTUS_BUTTON=(By.XPATH,'/html/body/div[4]/div/div/div[3]/button')
    HOME_CART_BUTTON=(By.XPATH,'/html/body/nav/div/div/ul/li[1]/a')
    NEW_MESSAGE=(By.ID,'exampleModalLabel')
    ABOUTUS_VIDEO=(By.XPATH,'/html/body/div[4]/div/div/div[2]/form/div/div/div[1]')
    CART_PRODUCTS_HEADER=(By.XPATH,'/html/body/div[6]/div/div[1]/h2')
    LOGIN_HEADER=(By.ID,'logInModalLabel')
    CLOSE_LOGIN_BUTTON=(By.XPATH,'/html/body/div[4]/div/div/div[3]/button[1]')
    SINGUP_HEADER=(By.ID,'signInModalLabel')
    CLOSE_SINGUP_BUTTON=(By.XPATH,'/html/body/div[2]/div/div/div[3]/button[1]')
    def click_logo(self):
        self.click_element(self.LOGO)
    def click_home(self):
        self.click_element(self.HOME_BUTTOM)
    def click_contacts(self):
        self.click_element(self.CONTACTS_BUTTON)
    def click_aboutus(self):
        self.click_element(self.ABOUTUS_BUTTON)
    def click_cart(self):
        self.click_element(self.CART_BUTTON)
    def click_login(self):
        self.click_element(self.LOGIN_BUTTON)
    def click_singup(self):
        self.click_element(self.SINGUP_BUTTON)
    def click_left_arrow(self):
        self.click_element(self.LEFT_ARROW_BUTTON)
    def click_right_arrow(self):
        self.click_element(self.RIGHT_ARROW_BUTTON)
    def click_phones(self):
        self.click_element(self.CATEGORIES_PHONES_BUTTON)
    def click_laptops(self):
        self.click_element(self.CATEGORIES_LAPTOPS_BUTTON)
    def click_monitors(self):
        self.click_element(self.CATEGORIES_MONITORS_BUTTON)
    def click_pic_nokia_lumia_1520(self):
        self.click_element(self.CATEGORIES_PIC_NOKIA_LUMIA_1520)
    def click_header_nokia_lumia_1520(self):
        self.click_element(self.CATEGORIES_HEADER_NOKIA_LUMIA_1520)
    def click_pic_sony_vaio_i5(self):
        self.click_element(self.PIC_SONY_VAIO_I5)
    def click_header_sony_vaio_i5(self):
        self.click_element(self.HEADER_SONY_VAIO_I5)
    def click_pic_apple_monitor_24(self):
        self.click_element(self.PIC_APPLE_MONITOR_24)
    def click_header_apple_monitor_24(self):
        self.click_element(self.HEADER_APPLE_MONITOR_24)
    def click_next_button(self):
        self.click_element(self.NEXT_BUTTON)
    def click_previous_button(self):
        self.click_element(self.PREVIOUS_BUTTON)
    def click_close_contacts(self):
        self.click_element(self.CLOSE_CONTACTS_BUTTON)
    def click_close_aboutus(self):
        self.click_element(self.CLOSE_ABOUTUS_BUTTON)
    def click_home_cart(self):
        self.click_element(self.HOME_CART_BUTTON)
    def click_close_login_button(self):
        self.click_element(self.CLOSE_LOGIN_BUTTON)
    def click_close_singup_button(self):
        self.click_element(self.CLOSE_SINGUP_BUTTON)