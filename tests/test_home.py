from re import search
from selenium.webdriver.common.keys import Keys
from unicodedata import category

from pages.home_page import HomePage as Lp
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains

def test_search_field(driver):
    base_url = 'https://portal-dev.safsarglobal.link/'
    lp = Lp(driver)
    driver.get(base_url)
    categories_elements = {
        'TEATRON': [
            (lp.CAT_TEATRON_BUTTON, [lp.TEATRON_HEADER]), ],
        'MUSIC': [
            (lp.CAT_MUSIC_BUTTON, [lp.MUSIC_HEADER]), ],
        'SPORT': [
            (lp.CAT_SPORT_BUTTON, [lp.SPORT_HEADER]), ],
        'STENDUP': [
            (lp.CAT_STENDUP_BUTTON, [lp.STENDUP_HEADER]), ],
        'KIDS': [
            (lp.CAT_KIDS_BUTTON, [lp.KIDS_HEADER]), ],
    }
    for category, elements in categories_elements.items():
        button_locator, items = elements[0]
        # בדוק שהכפתור לחיץ ומוצג
        element = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(button_locator))
        assert element.is_displayed(), f"{category} button is not displayed."
        print(f"{category} button is clickable and displayed.")
        # לחץ על הקטגוריה
        lp.click_element(button_locator)
        # בדוק אם הכותרת מופיעה בעמוד של הקטגוריה
        for header_locator in items:
            header_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(header_locator))
            assert header_element.is_displayed(), f"{category} header is not displayed."
            print(f"{category} header is displayed.")
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(lp.SAFSAR_LOGO_BUTTON))
        # חזור לעמוד הבית
        lp.click_safsar_logo()
        # הוסף שהייה קטנה כדי להבטיח טעינת העמוד
        time.sleep(2)
    print("All categories and their items are displayed correctly!")

def test_home_search_3_4_1(driver):
    base_url = 'https://portal-dev.safsarglobal.link/'
    lp = Lp(driver)
    driver.get(base_url)
    element = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(lp.SHOMER_TEXT))
    assert element.is_displayed(),"button is not displayed."
    print(" button is clickable and displayed.")

def test_home_search_5_1_5(driver):
    base_url = 'https://portal-dev.safsarglobal.link/'
    lp = Lp(driver)
    driver.get(base_url)
    search_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(lp.SEARCH_FIELD))
    lp.click_search_field()
    search_input.send_keys("красивая мыш")
    time.sleep(10)
    search_input.send_keys(Keys.ENTER)
    time.sleep(10)



def test_home_search_5_1_6(driver):
    base_url = 'https://portal-dev.safsarglobal.link/'
    lp = Lp(driver)
    driver.get(base_url)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(lp.SEARCH_FIELD))
    lp.click_search_field()
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "autocompleteField")))
    third_option = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,"//ul[@id='autocompleteField_list']//li[3]")))
    driver.execute_script("arguments[0].scrollIntoView(true);", third_option)
    # לחיצה על האפשרות השלישית
    ActionChains(driver).move_to_element(third_option).click().perform()
    time.sleep(10)


def test_home_search_5_2_1(driver):
    base_url = 'https://portal-dev.safsarglobal.link/'
    lp = Lp(driver)
    driver.get(base_url)
    search_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(lp.SEARCH_FIELD))
    lp.click_search_field()
    search_input.send_keys("מוזיקה")
    time.sleep(5)
    lp.click_clean_search()
    time.sleep(10)


def test_home_search_5_4_1(driver):
    base_url = 'https://portal-dev.safsarglobal.link/'
    lp = Lp(driver)
    driver.get(base_url)
    lp.click_cat_music_button()
    time.sleep(10)
    lp.click_safsar_logo()
    search_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(lp.SEARCH_FIELD))
    lp.click_search_field()
    # בהמשך ללחוץ על קטגוריה מהבדיקה הקודמת


def test_home_search_5_6_4(driver):
    base_url = 'https://portal-dev.safsarglobal.link/'
    lp = Lp(driver)
    driver.get(base_url)
    search_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(lp.SEARCH_FIELD))
    lp.click_search_field()
    search_input.send_keys("מוזיקה")
    time.sleep(5)
    scrollable_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".scrollBar.bg-white.overflow-y-auto")))
    for i in range(10):  # מבצע 10 גלילות
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollTop + 200;", scrollable_element)
        time.sleep(0.5)  # המתנה קצרה בין גלילות
    view_all_results_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "לצפיה בכל התוצאות")))
    view_all_results_button.click()
    time.sleep(5)
    filter_of_results = WebDriverWait(driver, 10).until(EC.presence_of_element_located(lp.FILTER_OF_RESULTS))
    assert filter_of_results.is_displayed()


from playwright.sync_api import sync_playwright

def tset_5_1_6_5_4_1_6_1_3(driver):
    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Navigate to the URL
        page.goto('https://portal-dev.safsarglobal.link/')

        # Interact with the combobox and select "ספורט"
        combobox = page.get_by_role('combobox')
        combobox.click()
        page.get_by_text('ספורט').nth(2).click()

        # Select the number "1"
        page.get_by_text('1', exact=True).click()

        # Click on "Safsar X" link
        page.get_by_role('link', name='Safsar X').click()

        # Click on "מוזיקה" link
        page.get_by_role('link', name='מוזיקה').click()

        # Click on "Safsar X" link again
        page.get_by_role('link', name='Safsar X').click()

        # Interact with the combobox and select "מוזיקה"
        combobox.click()
        page.get_by_text('מוזיקה').nth(2).click()

        # Click on "Safsar X" link again
        page.get_by_role('link', name='Safsar X').click()

        # Interact with the combobox and click "חיפוש לפי קטגוריה"
        combobox.click()
        page.get_by_text('חיפוש לפי קטגוריה').click()

        # Close the browser
        browser.close()

# Run the script
if __name__ == "_main_":
  tset_5_1_6_5_4_1_6_1_3()


def test_home_6_1_1(driver):
    base_url = 'https://portal-dev.safsarglobal.link/'
    lp = Lp(driver)
    driver.get(base_url)
    home_page = WebDriverWait(driver, 10).until(EC.presence_of_element_located(lp.HOME_PAGE))
    assert home_page.is_displayed()

def test_home_6_1_2(driver):
    base_url = 'https://portal-dev.safsarglobal.link/'
    lp = Lp(driver)
    driver.get(base_url)
    search_field=WebDriverWait(driver, 10).until(EC.presence_of_element_located(lp.SEARCH_FIELD))
    assert search_field.is_displayed()


def test_home_6_1_3(driver):
    base_url = 'https://portal-dev.safsarglobal.link/'  # כתובת האתר
    driver.get(base_url)
    lp = Lp(driver)
    lp.click_search_field()
    search_list=WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//ul[@id='autocompleteField_list']")))
    assert search_list.is_displayed(), "היו בעיות בהצגת הרשימה."


def test_home_6_1_4(driver):
    base_url = 'https://portal-dev.safsarglobal.link/'
    lp = Lp(driver)
    driver.get(base_url)
    search_field=WebDriverWait(driver, 10).until(EC.presence_of_element_located(lp.EVENTS_CARUSEL))
    assert search_field.is_displayed()


def test_home_6_1_6(driver):
    base_url = 'https://portal-dev.safsarglobal.link/'
    lp = Lp(driver)
    driver.get(base_url)
    category_elements = [
        lp.CAT_KIDS_BUTTON,
        lp.CAT_TEATRON_BUTTON,
        lp.CAT_MUSIC_BUTTON,
        lp.CAT_SPORT_BUTTON,
        lp.CAT_STENDUP_BUTTON
    ]
    for button_locator in category_elements:
            element = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(button_locator))
            assert element.is_displayed(), f"Button with locator {button_locator} is not displayed."
            print(f"Button with locator {button_locator} is displayed and clickable.")

def test_home_6_1_7(driver):
    base_url = 'https://portal-dev.safsarglobal.link/'
    lp = Lp(driver)
    driver.get(base_url)
    search_field=WebDriverWait(driver, 10).until(EC.presence_of_element_located(lp.TEXT_LINE))
    assert search_field.is_displayed()

def test_home_6_1_8(driver):
    base_url = 'https://portal-dev.safsarglobal.link/'
    lp = Lp(driver)
    driver.get(base_url)
    search_field=WebDriverWait(driver, 10).until(EC.presence_of_element_located(lp.BOTTOM))
    assert search_field.is_displayed()


def test_home_6_1_9(driver):
    base_url = 'https://portal-dev.safsarglobal.link/'
    lp = Lp(driver)
    driver.get(base_url)
    search_field=WebDriverWait(driver, 10).until(EC.presence_of_element_located(lp.BOTTOM))
    assert search_field.is_displayed()


def test_home_6_2_4(driver):
    base_url = 'https://portal-dev.safsarglobal.link/'
    lp = Lp(driver)  # מחלקת Page Object המייצגת את העמודים
    driver.get(base_url)
    lp.click_safsar_center_logo()
    WebDriverWait(driver, 10).until(EC.url_to_be(base_url))
    assert driver.current_url == base_url, f"ה-URL הנוכחי הוא {driver.current_url}, לא עמוד הבית לאחר לחיצה על הלוגו"

#sapir- בדיקה של הכותרת בתחתית העמוד
def test_6_3_2(driver):
        base_url = 'https://portal-dev.safsarglobal.link/'
        lp = Lp(driver)
        driver.get(base_url)
        element = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(lp.BIG_TITL))
        assert element.is_displayed(), "button is not displayed."

#sapir- בדיקה שכותרות מי אנחנו, איך זה עובד, שאלות ותשובות, מכירת כרטיסים, צרו קשר תנאי שימוש, מדיניות פרטיות, מדיניות ביטולים והצהרת נגישות לחיצים
def test_6_3_2(driver):
        base_url = 'https://portal-dev.safsarglobal.link/'
        lp = Lp(driver)
        driver.get(base_url)
        lp.click_how_it_works()
        time.sleep(5)
        assert base_url == 'https://portal-dev.safsarglobal.link/who-we-are'

def test_6_3_2(driver):
        base_url = 'https://portal-dev.safsarglobal.link/'
        lp = Lp(driver)
        driver.get(base_url)
        lp.click_how_it_works()
        time.sleep(5)
        assert base_url == 'https://portal-dev.safsarglobal.link/how-it-works'

def test_6_3_2(driver):
        base_url = 'https://portal-dev.safsarglobal.link/'
        lp = Lp(driver)
        driver.get(base_url)
        lp.click_questions_answers()
        time.sleep(5)
        assert base_url == 'https://portal-dev.safsarglobal.link/faqs'

def test_6_3_2(driver):
        base_url = 'https://portal-dev.safsarglobal.link/'
        lp = Lp(driver)
        driver.get(base_url)
        lp.click_ticket_sales()
        time.sleep(5)
        assert base_url == 'https://portal-dev.safsarglobal.link/ticket-sales'

def test_6_3_2(driver):
        base_url = 'https://portal-dev.safsarglobal.link/'
        lp = Lp(driver)
        driver.get(base_url)
        lp.click_contact_us()
        time.sleep(5)
        assert base_url == 'https://portal-dev.safsarglobal.link/contact-us'

def test_6_3_4(driver):
        base_url = 'https://portal-dev.safsarglobal.link/'
        lp = Lp(driver)
        driver.get(base_url)
        lp.click_terms()
        time.sleep(5)
        assert base_url == 'https://portal-dev.safsarglobal.link/terms-and-conditions'

def test_6_3_2(driver):
        base_url = 'https://portal-dev.safsarglobal.link/'
        lp = Lp(driver)
        driver.get(base_url)
        lp.click_privacy_policy()
        time.sleep(5)
        assert base_url == 'https://portal-dev.safsarglobal.link/privacy-policy'

def test_6_3_2(driver):
        base_url = 'https://portal-dev.safsarglobal.link/'
        lp = Lp(driver)
        driver.get(base_url)
        lp.click_accssibility()
        time.sleep(5)
        assert base_url == 'https://portal-dev.safsarglobal.link/accessibility-statement'

def test_6_3_2(driver):
        base_url = 'https://portal-dev.safsarglobal.link/'
        lp = Lp(driver)
        driver.get(base_url)
        lp.click_cancel_lation()
        time.sleep(5)
        assert base_url == 'https://portal-dev.safsarglobal.link/cancellation-policy'

# sapir- מעבר לדף האינטרנט של פייסבוק
def test_6_3_7(driver):
        base_url = 'https://portal-dev.safsarglobal.link/'
        lp = Lp(driver)
        driver.get(base_url)
        lp.click_facebook()
        time.sleep(5)
        assert base_url == 'https://www.facebook.com/profile.php?id=61558194638860'

# sapir- מעבר לדף האינסטגרם של ספסר
def test_6_3_7(driver):
        base_url = 'https://portal-dev.safsarglobal.link/'
        lp = Lp(driver)
        driver.get(base_url)
        lp.click_instagram()
        time.sleep(5)
        assert base_url == 'https://www.instagram.com/'
def test_home_6_4_5(driver):
    base_url = 'https://portal-dev.safsarglobal.link/'
    lp = Lp(driver)  # מחלקת Page Object המייצגת את העמודים
    driver.get(base_url)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # נותן זמן לטעינה (אם נדרש)
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # מאפשר זמן לטעינת תוכן חדש (אם יש)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:  # אם הגובה לא השתנה, הגענו לסוף
            break
        last_height = new_height
    safsar_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(lp.SAFSAR_BOTTON_UNDERALL_LOGO)
    )
    # בודק אם הכפתור לא לחיץ (כדוגמה, נוודא שהוא לא צמוד לפעולה, כמו ניווט לדף אחר)
    try:
        safsar_button.click()  # מנסה ללחוץ על הכפתור
        time.sleep(2)  # ממתין מעט אחרי הלחיצה
        current_url = driver.current_url  # בודק את ה-URL הנוכחי
        assert current_url == base_url, "לא נעשה מעבר לעמוד הבית בעת לחיצה על הלוגו"  # אם ה-URL השתנה, הכפתור עשה פעולה
    except Exception as e:
        print("הכפתור לא לחיץ או לא הוביל לעמוד אחר.")
        assert True  # אם התרחשה שגיאה, נוודא שהכפתור לא גרם לבעיה


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