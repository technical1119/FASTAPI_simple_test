from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Replace with your Railway URL
REMOTE_URL = "https://standalone-chrome-production-c37d.up.railway.app"

def getGoogleHomepage():
    # Set up Chrome options
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # Connect to remote WebDriver
    driver = webdriver.Remote(
        command_executor=REMOTE_URL,
        options=options
    )

    # Open Google homepage
    driver.get("https://www.google.com")
    
    # Print the title of the page
    print("Title of the page:", driver.title)
    
    # Get page content
    content = driver.page_source
    print(content)

    # Quit the driver
    driver.quit()



if __name__ == "__main__":
    getGoogleHomepage()
