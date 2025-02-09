from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os


def setup_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument('--disable-notifications')
    
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    return driver



    
def get_headline(driver):
    try:
        wait = WebDriverWait(driver, 10)
        headline_element = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "articleSubecjt"))
        )
        return headline_element.text.strip()
    
    except Exception as e:
        print(f"Error getting headline: {str(e)}")
        return None


def get_maincontent(driver):
    try:
        wait = WebDriverWait(driver, 10)
        # Check if the element exists first
        content_divs = driver.find_elements(By.ID, "realArtcContents")

        content_div = wait.until(
            EC.presence_of_element_located((By.ID, "realArtcContents"))
        )
        
        # Get the full innerHTML
        inner_html = content_div.get_attribute('innerHTML')
        print("\nContent div innerHTML:")
        print(inner_html[:500])  # First 500 chars
        
        # Also try getting text content for comparison
        text_content = content_div.text
        print("\nContent div text:")
        print(text_content[:1000])
        
        return None

    except Exception as e:
        print(f"Error getting main content: {str(e)}")
        print(f"Exception type: {type(e)}")
        print(f"Exception args: {e.args}")
        return None
    

def tester_function(driver):
    try:

        content_divs = driver.find_element(By.TAG_NAME, "br").text
        print(content_divs)
            
    except Exception as e: 
        print(f"Error: {str(e)}")



def main():
    driver = None
    try:
        driver = setup_driver()
        local_path = "file:///Users/griffith/project-netizen/app/test.html"
        driver.get(local_path)

        tester_function(driver)
        
    except Exception as e:
        print(f"Error: {str(e)}")
    
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    main()