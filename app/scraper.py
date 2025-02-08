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
        



def main():
    driver = None
    try:
        driver = setup_driver()
        driver.get("https://news.nate.com/view/20250127n06427?mid=n1008")
        time.sleep(1)
        
        # Get the data
        data = {
            "korean_title": get_headline(driver),
            "content": get_maincontent(driver)
        }
        
        # Print in a readable format
        print("\n=== Article Data ===")
        print(f"\nTitle: {data['korean_title']}")
        print("\nContent:")
        for i, item in enumerate(data['content'], 1):
            print(f"\n--- Item {i} ---")
            print(f"Type: {item['type']}")
            if item['type'] == 'image':
                print(f"Image URL: {item['info']}")
            else:   
                print(f"Text: {item['info']}\n")
        
    except Exception as e:
        print(f"\nError: {str(e)}")
    
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    main()