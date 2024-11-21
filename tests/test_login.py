from pages.login_page import LoginPage as Lp
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from tests.conftest import driver
from selenium.webdriver.common.keys import Keys
from utils.phone_conection import get_latest_sms_code

def test_sanity_login(driver):
    """
    Perform the sanity login test: enter phone number, fetch OTP, and verify login.
    """
    # from lp_module import Lp  # Replace with the actual import for your page object class

    base_url = 'https://portal-dev.safsarglobal.link/'
    driver.get(base_url)

    lp = Lp(driver)
    lp.click_login_home()

    # Enter phone number
    phone_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(lp.INPUT_PHONE_NUMBER)
    )
    phone_input.send_keys("0542400813")
    time.sleep(5)
    lp.click_enter_button()
    time.sleep(20)

    # Fetch OTP from the latest SMS
    otp_code = None
    try:
        result = subprocess.run(
            ["adb", "shell", "content", "query", "--uri", "content://sms/inbox", "--projection", "body,date"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            encoding='utf-8'
        )

        if result.returncode != 0:
            print(f"Error fetching SMS: {result.stderr}")
        elif result.stdout:
            messages = result.stdout.splitlines()
            parsed_messages = []

            for message in messages:
                parts = message.split(", ")
                if len(parts) >= 2:
                    try:
                        body_part = parts[0].split("=", 1)[1].strip()
                        date_part = parts[1].split("=", 1)[1].strip()

                        if date_part.isdigit():
                            timestamp = int(date_part)
                            if 0 <= timestamp <= 2000000000000:
                                parsed_messages.append((body_part, timestamp))
                    except IndexError:
                        continue

            if parsed_messages:
                parsed_messages.sort(key=lambda x: x[1], reverse=True)
                latest_sms = parsed_messages[0]
                print(f"Latest SMS: {latest_sms[0]}")

                import re
                match = re.search(r'\b\d{4,6}\b', latest_sms[0])  # Adjust regex if needed
                if match:
                    otp_code = match.group(0)
    except subprocess.SubprocessError as e:
        print(f"An error occurred while running ADB command: {e}")

    # Verify OTP code retrieval
    if otp_code:
        print(f"Retrieved OTP Code: {otp_code}")
        lp.enter_otp_code(otp_code)
    else:
        print("Failed to retrieve OTP code.")
        assert False, "OTP code retrieval failed"

    time.sleep(5)
    lp.click_submit_button()
    time.sleep(10)
    # Assertions to verify successful login
    assert driver.current_url == base_url, "Login failed; URL mismatch."
    assert driver.find_element(*lp.MY_ACCOUNT_HOME_BUTTON).is_displayed(), "My Account button is not visible."

#1.21.3-1.21.6
def test_sanity_login_2(driver):
    """
    Perform the sanity login test: enter phone number, fetch OTP, and verify login.
    """
    # from lp_module import Lp  # Replace with the actual import for your page object class

    base_url = 'https://portal-dev.safsarglobal.link/'
    driver.get(base_url)

    lp = Lp(driver)
    lp.click_login_home()

    # Enter phone number
    phone_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(lp.INPUT_PHONE_NUMBER)
    )
    phone_input.send_keys("0542400813")
    time.sleep(5)
    lp.click_enter_button()
    time.sleep(20)

    # Fetch OTP from the latest SMS
    otp_code = None
    try:
        result = subprocess.run(
            ["adb", "shell", "content", "query", "--uri", "content://sms/inbox", "--projection", "body,date"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            encoding='utf-8'
        )

        if result.returncode != 0:
            print(f"Error fetching SMS: {result.stderr}")
        elif result.stdout:
            messages = result.stdout.splitlines()
            parsed_messages = []

            for message in messages:
                parts = message.split(", ")
                if len(parts) >= 2:
                    try:
                        body_part = parts[0].split("=", 1)[1].strip()
                        date_part = parts[1].split("=", 1)[1].strip()

                        if date_part.isdigit():
                            timestamp = int(date_part)
                            if 0 <= timestamp <= 2000000000000:
                                parsed_messages.append((body_part, timestamp))
                    except IndexError:
                        continue

            if parsed_messages:
                parsed_messages.sort(key=lambda x: x[1], reverse=True)
                latest_sms = parsed_messages[0]
                print(f"Latest SMS: {latest_sms[0]}")

                import re
                match = re.search(r'\b\d{4,6}\b', latest_sms[0])  # Adjust regex if needed
                if match:
                    otp_code = match.group(0)
    except subprocess.SubprocessError as e:
        print(f"An error occurred while running ADB command: {e}")

    # Verify OTP code retrieval
    if otp_code:
        print(f"Retrieved OTP Code: {otp_code}")
        lp.enter_otp_code(otp_code)
    else:
        print("Failed to retrieve OTP code.")
        assert False, "OTP code retrieval failed"

    time.sleep(5)
    lp.click_submit_button()
    time.sleep(10)
    # Assertions to verify successful login
    assert driver.current_url == base_url, "Login failed; URL mismatch."
    assert driver.find_element(*lp.MY_ACCOUNT_HOME_BUTTON).is_displayed(), "My Account button is not visible."


def test_sanity_login_3(driver):
    """
    Perform the sanity login test: enter phone number, fetch OTP, and verify login.
    """
    # from lp_module import Lp  # Replace with the actual import for your page object class

    base_url = 'https://portal-dev.safsarglobal.link/'
    driver.get(base_url)

    lp = Lp(driver)
    lp.click_login_home()

    # Enter phone number
    phone_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(lp.INPUT_PHONE_NUMBER)
    )
    phone_input.send_keys("0542400813")
    time.sleep(5)
    lp.click_enter_button()
    time.sleep(20)
    lp.enter_otp_code("762351")
    time.sleep(5)
    lp.click_submit_button()
    time.sleep(10)


def test_sanity_login_4(driver):
    """
    Perform the sanity login test: enter phone number, fetch OTP, and verify login.
    """
    # from lp_module import Lp  # Replace with the actual import for your page object class

    base_url = 'https://portal-dev.safsarglobal.link/'
    driver.get(base_url)

    lp = Lp(driver)
    lp.click_login_home()

    # Enter phone number
    phone_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(lp.INPUT_PHONE_NUMBER)
    )
    phone_input.send_keys("0542400813")
    time.sleep(5)
    lp.click_enter_button()
    time.sleep(20)
    lp.enter_otp_code(" ")
    time.sleep(5)
    lp.click_submit_button()
    time.sleep(10)

#הכנס לאתר נסה לעבור בין עמודים ללא ביצוע תהליך ההרשמה
def test_login_process_4_1_1(driver):
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

# "היכנס לאתר ממחשב שולחני
# לחץ על כפתור ההרשמה ובדוק את הופעת תהליך ההרשמה
# היכנס לאתר ממכשיר נייד וחזור על הפעולה"
def test_login_process_4_1_2(driver):
    base_url = 'https://portal-dev.safsarglobal.link/'
    driver.get(base_url)
    lp = Lp(driver)
    driver.get(base_url)
    lp.click_login_home()
    phone_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(lp.INPUT_PHONE_NUMBER))
    assert phone_input.is_displayed()


def test_login_process_4_1_3(driver):
    base_url = 'https://portal-dev.safsarglobal.link/'
    driver.get(base_url)
    lp = Lp(driver)
    driver.get(base_url)
    lp.click_login_home()
    phone_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(lp.INPUT_PHONE_NUMBER))
    assert phone_input.is_displayed()

#בדיקת זמינת מעבר לתהליך ההתחברות מעמוד מכירת הכרטיסים
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
#בדיקת זמינות מעבר לתהליך ההרשמה מעמוד מכירת הכרטיסים
def test_login_process_4_2_3(driver):
    base_url = 'https://portal-dev.safsarglobal.link/'
    driver.get(base_url)
    lp = Lp(driver)
    driver.get(base_url)
    lp.click_ticket_seling_home()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(lp.TICKET_SELING_LOGIN_HEADER))
    lp.click_sighnup_button_after_ticket_seling()
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(lp.SIGHNUP_FIELD))
    assert email_input.is_displayed()













#     lp.enter_username('veronika170300')
#     lp.enter_password('vera170300')
#     lp.click_login()
#     time.sleep(10)
#     welcome_message = driver.find_element(*lp.WELCOME_USERNAME).text
#     assert welcome_message == "Welcome veronika170300"
#     assert driver.find_element(*lp.LOGOUT_BUTTON).is_displayed()
#     lp.click_logout()
#     time.sleep(10)
#    # assert driver.current_url == "https://www.demoblaze.com/index.html"
#
# def test_empty_username_and_password(driver):
#     base_url = 'https://www.demoblaze.com/index.html'
#     driver.get(base_url)
#     lp = Lp(driver)
#     driver.get(base_url)
#     lp.click_login_home()
#     time.sleep(10)
#     lp.click_login()
#     wait = WebDriverWait(driver, 10)
#     alert = wait.until(EC.alert_is_present())  # מחכה לאלרט
#     assert alert.text == "Please fill out Username and Password."
#     time.sleep(5)
#     alert.accept()
#     time.sleep(10)
#
# def test_invalid_login_incorrect_username(driver):
#     base_url = 'https://www.demoblaze.com/index.html'
#     driver.get(base_url)
#     lp = Lp(driver)
#     driver.get(base_url)
#     lp.click_login_home()
#     time.sleep(10)
#     lp.enter_username('ver')
#     lp.enter_password('vera170300')
#     lp.click_login()
#     time.sleep(10)
#     wait = WebDriverWait(driver, 10)
#     alert = wait.until(EC.alert_is_present())  # מחכה לאלרט
#     assert alert.text == "User does not exist."
#     alert.accept()
#
#
# def test_invalid_login_incorrect_password(driver):
#     base_url = 'https://www.demoblaze.com/index.html'
#     driver.get(base_url)
#     lp = Lp(driver)
#     driver.get(base_url)
#     lp.click_login_home()
#     time.sleep(10)
#     lp.enter_username('veronika170300')
#     lp.enter_password('123456')
#     lp.click_login()
#     time.sleep(10)
#     wait = WebDriverWait(driver, 10)
#     alert = wait.until(EC.alert_is_present())  # מחכה לאלרט
#     assert alert.text == "Wrong password."
#     alert.accept()
#
# def test_invalid_login_incorrect_username_and_password(driver):
#     base_url = 'https://www.demoblaze.com/index.html'
#     driver.get(base_url)
#     lp = Lp(driver)
#     driver.get(base_url)
#     lp.click_login_home()
#     time.sleep(10)
#     lp.enter_username('ver')
#     lp.enter_password('123456')
#     lp.click_login()
#     time.sleep(10)
#     wait = WebDriverWait(driver, 10)
#     alert = wait.until(EC.alert_is_present())  # מחכה לאלרט
#     assert alert.text == "User does not exist."
#     alert.accept()
#
# def test_close_button(driver):
#     base_url = 'https://www.demoblaze.com/index.html'
#     driver.get(base_url)
#     lp = Lp(driver)
#     driver.get(base_url)
#     lp.click_login_home()
#     time.sleep(10)
#     lp.enter_username('veronika170300')
#     lp.enter_password('vera170300')
#     time.sleep(3)
#     lp.click_close()
#     time.sleep(10)


