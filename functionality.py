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
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--remote-debugging-port=9222')
    
    service = Service(executable_path='/usr/local/bin/chromedriver')
    
    driver = webdriver.Chrome(
        service=service,
        options=chrome_options
    )
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
