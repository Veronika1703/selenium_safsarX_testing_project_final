from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException


chromedriver_path = 'C:\\webdrivers\\chromedriver.exe'



api_urls = [
    "https://portal-dev.safsarglobal.link/",
    "https://portal-dev.safsarglobal.link/signin",
    "https://portal-dev.safsarglobal.link/register",
    "https://portal-dev.safsarglobal.link/start-ticket-sell",
    "https://portal-dev.safsarglobal.link/category-search-results/5/%D7%AA%D7%99%D7%90%D7%98%D7%A8%D7%95%D7%9F",
    "https://portal-dev.safsarglobal.link/category-search-results/4/%D7%9E%D7%95%D7%96%D7%99%D7%A7%D7%94",
    "https://portal-dev.safsarglobal.link/category-search-results/1/%D7%A1%D7%A4%D7%95%D7%A8%D7%98",
    "https://portal-dev.safsarglobal.link/category-search-results/3/%D7%A1%D7%98%D7%90%D7%A0%D7%93%D7%90%D7%A4",
    "https://portal-dev.safsarglobal.link/category-search-results/2/%D7%99%D7%9C%D7%93%D7%99%D7%9D"
]


chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (optional)
chrome_options.add_argument("--disable-gpu")  # For headless mode
chrome_options.add_argument("--no-sandbox")

service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

for url in api_urls:
    try:
        print(f"Testing URL: {url}")
        driver.get(url)
        driver.implicitly_wait(10)

        current_url = driver.current_url
        if current_url == url:
            print(f"Success: Reached the desired URL - {url}")
        else:
            print(f"Failure: Expected URL - {url}, but got - {current_url}")

    except TimeoutException:
        print(f"Timeout: Failed to load the URL - {url}")

    except Exception as e:
        print(f"Error: An unexpected error occurred for URL {url}: {e}")


driver.quit()