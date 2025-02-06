from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import json
import sys  # Add this import

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
  

        message = {"text": "Hello World from Python"}
        print(json.dumps(message))
        
if __name__ == "__main__":
    main()
