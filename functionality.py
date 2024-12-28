from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import os 


def createDriver() -> webdriver.Chrome:
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.binary_location = "/usr/bin/google-chrome"  # Standard Linux Chrome location
    
    service = Service('/usr/local/bin/chromedriver')  # Standard Linux ChromeDriver location
    
    try:
        driver = webdriver.Chrome(
            service=service,
            options=chrome_options
        )
    except Exception as e:
        print(f"Error creating driver: {e}")
        raise e
    return driver

async def getGoogleHomepage():
    driver = createDriver()
    driver.get("https://www.google.com")
    print(driver.page_source)
    return driver.page_source

def doBackgroundTask(inp):
    print("Doing background task")
    print(inp.msg)
    print("Done")
