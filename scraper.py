from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def setup_driver():
    """Set up and return a Chrome WebDriver instance"""
    # Set up Chrome options
    chrome_options = webdriver.ChromeOptions()
    
    # Add some common options (you can modify these as needed)
    chrome_options.add_argument('--start-maximized')  # Start with maximized window
    chrome_options.add_argument('--disable-notifications')  # Disable notifications
    
    # Create and return the driver
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    return driver

def main():
    try:
        # Initialize the driver
        driver = setup_driver()
        
        # Example: Navigate to a website (replace with your target URL)
        driver.get("https://example.com")
        
        # Wait a moment to let the page load (you can adjust this)
        time.sleep(3)
        
        # Example of how to find an element (uncomment and modify as needed)
        # element = driver.find_element(By.CSS_SELECTOR, "your-css-selector")
        # print(element.text)
        
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Always make sure to close the driver
        driver.quit()
        print("Finished Scraping")

if __name__ == "__main__":
    main()
