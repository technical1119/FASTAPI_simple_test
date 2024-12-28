from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def getGoogleHomepage():
    # Initialize WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run headless
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


    # Open Google
    driver.get("https://www.google.com")

    content = driver.page_source
    print(content)

    # Close the browser
    driver.quit()

if __name__ == "__main__":
    getGoogleHomepage()
