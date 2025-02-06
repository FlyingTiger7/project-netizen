from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import json
import sys

def setup_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument('--disable-notifications')
    
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    return driver

def main():
    try:
        driver = setup_driver()
        # Let's use a simple news site as an example
        driver.get("https://news.nate.com/view/20250127n06427?mid=n1008")
        
        # Get the page title
        title = driver.title
        wait = WebDriverWait(driver, 10)
        korean_title = driver.find_element(By.CLASS_NAME, "articleSubecjt").text
        
        message = {
            "korean_title": korean_title,
            "status": "success"
        }
        
        sys.stdout.write(json.dumps(message))
        sys.stdout.flush()
        
    except Exception as e:
        error_msg = {
            "text": f"Error: {str(e)}",
            "status": "error"
        }
        sys.stdout.write(json.dumps(error_msg))
        sys.stdout.flush()
    
    finally:
        driver.quit()

if __name__ == "__main__":
    main()