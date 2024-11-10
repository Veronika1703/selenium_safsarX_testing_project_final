from pages.home_page import HomePage as Lp
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

def test_search_field(driver):
    base_url = 'https://portal-dev.safsarglobal.link/'
    lp = Lp(driver)
    driver.get(base_url)
    lp.click_search_field()
    time.sleep(10)


# def test_header_elements(driver):
#     base_url = 'https://www.demoblaze.com/index.html'
#     driver.get(base_url)
#     lp = Lp(driver)
#     header_elements = [
#         ('Home',lp.HOME_BUTTOM),
#         ('Contacts',lp.CONTACTS_BUTTON),
#         ('About Us',lp.ABOUTUS_BUTTON),
#         ('Cart',lp.CART_BUTTON),
#         ('Login',lp.LOGIN_BUTTON),
#         ('Sign Up',lp.SINGUP_BUTTON),
#         ('Logo',lp.LOGO)
#     ]
#     for name, locator in header_elements:
#         try:
#             element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(locator))
#             assert element.is_displayed(), f"{name} is not displayed."
#             print(f"{name} is clickable and displayed.")
#         except Exception as e:
#             print(f"Error checking {name}: {e}")
#

# def test_carusela_element(driver):
#     base_url = 'https://www.demoblaze.com/index.html'
#     driver.get(base_url)
#     lp = Lp(driver)
#
#     carusela = [
#         ('1pick', lp.PICK_SLIDE1),
#         ('2pick', lp.PICK_SLIDE2),
#         ('3pick', lp.PICK_SLIDE3)
#     ]
#
#     results = []
#
#     for i in range(len(carusela)):
#         time.sleep(5)
#         current_image = carusela[i][1]
#         is_displayed = driver.find_element(*current_image).is_displayed()
#         results.append(is_displayed)
#
#     assert all(results), "Not all carousel images are displayed."
#     time.sleep(5)
#
#     for i in range(len(carusela) - 1):
#         lp.click_right_arrow()
#         time.sleep(3)
#         assert driver.find_element(*carusela[i + 1][1]).is_displayed(), f"Image at index {i + 1} is not displayed."
#
#     for i in range(len(carusela) - 1, 0, -1):
#         lp.click_left_arrow()
#         time.sleep(3)
#         assert driver.find_element(*carusela[i - 1][1]).is_displayed(), f"Image at index {i - 1} is not displayed."
#
#     print("Carousel navigation test passed successfully!")
#
# #למצוא איך משתמשים ב headless
# # mark
#
# def test_categories(driver):
#     base_url = 'https://www.demoblaze.com/index.html'
#     driver.get(base_url)
#     lp = Lp(driver)
#
#     # הגדרת הקטגוריות והאלמנטים שלהן
#     categories_elements = {
#         'phones': [
#             (lp.CATEGORIES_PHONES_BUTTON, [
#                 (lp.PIC_SAMSUNG_GALACSY_S6, lp.HEADER_SAMSUNG_GALACSY_S6),
#                 (lp.PIC_NOKIA_LUMIA_1520, lp.HEADER_NOKIA_LUMIA_1520),
#                 (lp.PIC_NEXUS_6, lp.HEADER_NEXUS_6),
#                 (lp.PIC_SAMSUNGGALUCSY_S7, lp.HEADER_SAMSUNGGALUCSY_S7),
#                 (lp.PIC_IPHON6_32g, lp.HEADER_IPHON6_32g),
#                 (lp.PIC_SONY_XPERIA_Z5, lp.HEADER_SONY_XPERIA_Z5),
#                 (lp.PIC_HTC_ONE_M9, lp.HEADER_HTC_ONE_M9),
#             ]),
#         ],
#         'notebooks': [
#             (lp.CATEGORIES_LAPTOPS_BUTTON, [
#                 (lp.PIC_SONY_VAIO_I5, lp.HEADER_SONY_VAIO_I5),
#                 (lp.PIC_SONY_VAIO_I7, lp.HEADER_SONY_VAIO_I7),
#                 (lp.PIC_MACBOOK_AIR, lp.HEADER_MACBOOK_AIR),
#                 (lp.PIC_DELL_I7_8GB, lp.HEADER_DELL_I7_8GB),
#                 (lp.PIC_2017_DELL_156_INCH, lp.HEADER_2017_DELL_156_INCH),
#                 (lp.PIC_MACBOOK_PRO, lp.HEADER_MACBOOK_PRO),
#             ]),
#         ],
#         'monitors': [
#             (lp.CATEGORIES_MONITORS_BUTTON, [
#                 (lp.PIC_APPLE_MONITOR_24, lp.HEADER_APPLE_MONITOR_24),
#                 (lp.PIC_ASUS_FULL_HD, lp.HEADER_ASUS_FULL_HD),
#             ]),
#         ],
#     }
#
#     # בדוק את הקטגוריות
#     for category, elements in categories_elements.items():
#         button_locator, items = elements[0]
#
#         # בדוק שהקטגוריה לחיצה ומוצגת
#         element = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(button_locator))
#         assert element.is_displayed(), f"{category} button is not displayed."
#         print(f"{category} button is clickable and displayed.")
#         lp.click_element(button_locator)  # לחץ על הקטגוריה
#
#         # בדוק את התמונות והכותרות בקטגוריה
#         for img_locator, header_locator in items:
#             img_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(img_locator))
#             header_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(header_locator))
#             assert img_element.is_displayed(), f"{category} image is not displayed."
#             assert header_element.is_displayed(), f"{category} header is not displayed."
#             print(f"{category} image and header are clickable and displayed.")
#
#     print("All categories and their items are displayed correctly!")
#
#
#
# def test_pages_navigation(driver):
#     base_url = 'https://www.demoblaze.com/index.html'
#     driver.get(base_url)
#     lp = Lp(driver)
#
#     # Navigate to home
#     lp.click_home()
#     time.sleep(10)
#
#     # Define products for each page
#     pages = {
#         'page1': [
#             (lp.PIC_SAMSUNG_GALACSY_S6, lp.HEADER_SAMSUNG_GALACSY_S6),
#             (lp.PIC_NOKIA_LUMIA_1520, lp.HEADER_NOKIA_LUMIA_1520),
#             (lp.PIC_NEXUS_6, lp.HEADER_NEXUS_6),
#             (lp.PIC_SAMSUNGGALUCSY_S7, lp.HEADER_SAMSUNGGALUCSY_S7),
#             (lp.PIC_IPHON6_32g, lp.HEADER_IPHON6_32g),
#             (lp.PIC_SONY_XPERIA_Z5, lp.HEADER_SONY_XPERIA_Z5),
#             (lp.PIC_HTC_ONE_M9, lp.HEADER_HTC_ONE_M9),
#             (lp.PIC_SONY_VAIO_I5, lp.HEADER_SONY_VAIO_I5),
#             (lp.PIC_SONY_VAIO_I7, lp.HEADER_SONY_VAIO_I7)
#         ],
#         'page2': [
#             (lp.PIC_APPLE_MONITOR_24, lp.HEADER_APPLE_MONITOR_24),
#             (lp.PIC_MACBOOK_AIR, lp.HEADER_MACBOOK_AIR),
#             (lp.PIC_DELL_I7_8GB, lp.HEADER_DELL_I7_8GB),
#             (lp.PIC_2017_DELL_156_INCH, lp.HEADER_2017_DELL_156_INCH),
#             (lp.PIC_ASUS_FULL_HD, lp.HEADER_ASUS_FULL_HD),
#             (lp.PIC_MACBOOK_PRO, lp.HEADER_MACBOOK_PRO)
#         ]
#     }
#
#     # Check products on page 1
#     for img_locator, header_locator in pages['page1']:
#         img_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(img_locator))
#         header_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(header_locator))
#         assert img_element.is_displayed(), f"Image for {header_element.text} is not displayed on page 1."
#         assert header_element.is_displayed(), f"Header for {header_element.text} is not displayed on page 1."
#         print(f"{header_element.text} is displayed on page 1.")
#
#     # Click NEXT button
#     lp.click_next_button()
#     time.sleep(2)  # Wait for page load
#
#     # Check products on page 2
#     for img_locator, header_locator in pages['page2']:
#         img_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(img_locator))
#         header_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(header_locator))
#         assert img_element.is_displayed(), f"Image for {header_element.text} is not displayed on page 2."
#         assert header_element.is_displayed(), f"Header for {header_element.text} is not displayed on page 2."
#         print(f"{header_element.text} is displayed on page 2.")
#
#     # Click PREVIOUS button
#     lp.click_previous_button()
#     time.sleep(2)  # Wait for page load
#
#     # Check products on page 1 again
#     for img_locator, header_locator in pages['page1']:
#         img_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(img_locator))
#         header_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(header_locator))
#         assert img_element.is_displayed(), f"Image for {header_element.text} is not displayed after going back to page 1."
#         assert header_element.is_displayed(), f"Header for {header_element.text} is not displayed after going back to page 1."
#         print(f"{header_element.text} is displayed on page 1 after going back.")
#
#     print("All pages navigated and products displayed successfully!")
#
#
# def test_product_navigation(driver):
#     base_url = 'https://www.demoblaze.com/index.html'
#     driver.get(base_url)
#     lp = Lp(driver)
#
#     lp.click_home()
#     time.sleep(2)
#
#     # Define all products with their expected URLs
#     products = {
#         'first_page': [
#             (lp.HEADER_SAMSUNG_GALACSY_S6, 'https://www.demoblaze.com/prod.html?idp_=1'),
#             (lp.HEADER_NOKIA_LUMIA_1520, 'https://www.demoblaze.com/prod.html?idp_=2'),
#             (lp.HEADER_NEXUS_6, 'https://www.demoblaze.com/prod.html?idp_=3'),
#             (lp.HEADER_SAMSUNGGALUCSY_S7, 'https://www.demoblaze.com/prod.html?idp_=4'),
#             (lp.HEADER_IPHON6_32g, 'https://www.demoblaze.com/prod.html?idp_=5'),
#             (lp.HEADER_SONY_XPERIA_Z5, 'https://www.demoblaze.com/prod.html?idp_=6'),
#             (lp.HEADER_HTC_ONE_M9, 'https://www.demoblaze.com/prod.html?idp_=7'),
#             (lp.HEADER_SONY_VAIO_I5,'https://www.demoblaze.com/prod.html?idp_=8'),
#             (lp.HEADER_SONY_VAIO_I7,'https://www.demoblaze.com/prod.html?idp_=9')
#         ],
#         'second_page': [
#             (lp.HEADER_APPLE_MONITOR_24,'https://www.demoblaze.com/prod.html?idp_=10'),
#             (lp.HEADER_MACBOOK_AIR, 'https://www.demoblaze.com/prod.html?idp_=11'),
#             (lp.HEADER_DELL_I7_8GB, 'https://www.demoblaze.com/prod.html?idp_=12'),
#             (lp.HEADER_2017_DELL_156_INCH, 'https://www.demoblaze.com/prod.html?idp_=13'),
#             (lp.HEADER_ASUS_FULL_HD, 'https://www.demoblaze.com/prod.html?idp_=14'),
#             (lp.HEADER_MACBOOK_PRO, 'https://www.demoblaze.com/prod.html?idp_=15'),
#         ]
#     }
#
#     for header, url in products['first_page']:
#         lp.click_element(header)  # לחץ על הכותרת
#         time.sleep(2)  # המתן לטעינת העמוד
#
#         # בדוק שהכתובת השתנתה לכתובת הרצויה
#         current_url = driver.current_url
#         assert current_url == url
#
#         # לחיצה על כפתור HOME שוב
#         # driver.back()  # חזור לעמוד הקודם
#         # time.sleep(2)  # המתן לטעינת העמוד
#         lp.click_home()  # לחיצה על כפתור הבית
#         time.sleep(2)  # המתן לטעינת העמוד
#     for header, url in products['second_page']:
#         lp.click_next_button()
#         time.sleep(2)
#         lp.click_element(header)  # לחץ על הכותרת
#         time.sleep(2)  # המתן לטעינת העמוד
#
#         # בדוק שהכתובת השתנתה לכתובת הרצויה
#         current_url = driver.current_url
#         assert current_url == url
#
#         # לחיצה על כפתור HOME שוב
#
#         lp.click_home()  # לחיצה על כפתור הבית
#         time.sleep(2)  # המתן לטעינת העמוד
#
#
# def test_header_in_description(driver):
#     """אליק זאת הבדיקה שבקשת להוסיף היא לא עובדת לי לא הצלחתי לסדר את זה """
#     base_url = 'https://www.demoblaze.com/index.html'
#     driver.get(base_url)
#     lp = Lp(driver)
#     time.sleep(2)
#     products = {
#         'first_page': [
#             (lp.HEADER_SAMSUNG_GALACSY_S6,lp.DESCRIPTION_SAMSUNG_GALACSY_S6),
#             (lp.HEADER_NOKIA_LUMIA_1520,lp.DESCRIPTION_NOKIA_LUMIA_1520),
#             (lp.HEADER_NEXUS_6, lp.DESCRIPTION_NEXUS_6),
#             (lp.HEADER_SAMSUNGGALUCSY_S7, lp.DESCRIPTION_SAMSUNGGALUCSY_S7),
#             (lp.HEADER_IPHON6_32g, lp.DESCRIPTION_IPHON6_32g),
#             (lp.HEADER_SONY_XPERIA_Z5, lp.DESCRIPTION_SONY_XPERIA_Z5),
#             (lp.HEADER_HTC_ONE_M9, lp.DESCRIPTION_HTC_ONE_M9),
#             (lp.HEADER_SONY_VAIO_I5, lp.DESCRIPTION_SONY_VAIO_I5),
#             (lp.HEADER_SONY_VAIO_I7, lp.DESCRIPTION_SONY_VAIO_I7)
#         ],
#         'second_page': [
#             (lp.HEADER_APPLE_MONITOR_24, 'https://www.demoblaze.com/prod.html?idp_=10'),
#             (lp.HEADER_MACBOOK_AIR, 'https://www.demoblaze.com/prod.html?idp_=11'),
#             (lp.HEADER_DELL_I7_8GB, 'https://www.demoblaze.com/prod.html?idp_=12'),
#             (lp.HEADER_2017_DELL_156_INCH, 'https://www.demoblaze.com/prod.html?idp_=13'),
#             (lp.HEADER_ASUS_FULL_HD, 'https://www.demoblaze.com/prod.html?idp_=14'),
#             (lp.HEADER_MACBOOK_PRO, 'https://www.demoblaze.com/prod.html?idp_=15'),
#         ]
#     }
#     description_element = driver.find_element(By.CLASS_NAME, 'card-text')  # שנה את ה-Class Name לפי הצורך
#     description_text = description_element.get_attribute('innerText')
#
#     for header, expected_description in products['first_page']:
#         assert header in description_text
#         assert expected_description in description_text
#
#
#     for header, url in products['second_page']:
#         lp.click_next_button()
#         time.sleep(2)
#         assert header in description_text
#         assert expected_description in description_text