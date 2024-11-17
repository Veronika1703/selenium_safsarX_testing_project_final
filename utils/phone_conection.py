import subprocess
import re


def get_latest_sms_code():
    try:
        # הפקודה לשליפת הודעות ה-SMS האחרונות מהטלפון
        result = subprocess.run(
            ['adb', 'shell',
             'content query --uri content://sms/inbox --projection body --sort_order date DESC limit 1'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # בדיקת הצלחת הביצוע
        if result.returncode != 0:
            print("Error fetching SMS:", result.stderr)
            return None

        # התוצאה מכילה את ההודעה האחרונה
        message = result.stdout
        print("Fetched SMS:", message)  # הדפסה לבדיקת תוכן ההודעה

        # שליפת קוד האימות מתוך ההודעה באמצעות ביטוי רגולרי (לדוגמה, אם הקוד הוא מספר בן 4-6 ספרות)
        otp_match = re.search(r'\b\d{4,6}\b', message)

        # בדיקה אם נמצא קוד
        if otp_match:
            return otp_match.group(0)
        else:
            print("No OTP code found in the SMS.")
            return None

    except Exception as e:
        print("An error occurred:", str(e))
        return None