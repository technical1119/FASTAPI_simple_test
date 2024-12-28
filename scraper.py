from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def getGoogleHomepage():
    options = Options()
    options.add_argument("--headless")  # Run in headless mode (no UI)
    options.add_argument("--no-sandbox")  # Necessary for Docker
    options.add_argument("--disable-dev-shm-usage")  # Fixes issue in Docker

    # Set up ChromeDriver with the options
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Open Google homepage
    driver.get("https://www.google.com")

    # Print the title of the page
    print(driver.title)

    driver.quit()

if __name__ == "__main__":
    getGoogleHomepage()
