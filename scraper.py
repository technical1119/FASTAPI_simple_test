from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller

def getGoogleHomepage():
    # Automatically install the correct version of ChromeDriver for the installed Chromium
    chromedriver_autoinstaller.install()

    # Set Chrome options for headless mode
    options = Options()
    options.add_argument("--headless")  # Run in headless mode (no UI)
    options.add_argument("--no-sandbox")  # Necessary for Docker
    options.add_argument("--disable-dev-shm-usage")  # Fixes issue in Docker

    # Set up ChromeDriver with the options
    driver = webdriver.Chrome(options=options)

    # Open Google homepage
    driver.get("https://www.google.com")

    # Print the title of the page
    print(driver.title)

    driver.quit()



if __name__ == "__main__":
    getGoogleHomepage()
