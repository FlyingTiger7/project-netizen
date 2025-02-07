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





def get_image_url(driver):
    try:
        wait = WebDriverWait(driver, 10)
        image_element = wait.until(
            EC.presence_of_element_located((By.ID, "mainimg0"))
        )
        url = image_element.get_attribute("src")

        if url and '///' in url:
            url = url.split('///').pop()
        
        if not url.startswith('http'):
                url = 'https://' + url
        return url 




    except Exception as e:
        print(f"Error getting main_image: {str(e)}")
        return None


def get_maincontent(driver):
    try:
        wait = WebDriverWait(driver, 10)
        content_div = wait.until(
            EC.presence_of_element_located((By.ID, "realArtcContents"))
        )
        
        content = []
        
        for element in content_div.find_elements(By.TAG_NAME, "p"):
    
    
    
    
    
    
    
    
    except Exception as e:
        print(f"Error getting main content: {str(e)}")
        return None
        



def main():

    driver = None
    try:
        driver = setup_driver()
        driver.get("https://news.nate.com/view/20250127n06427?mid=n1008")

        time.sleep(1)
        
        data = {
            "korean_title": get_headline(driver),
            #"content": get_content(driver),
            #"comments": get_comments(driver)
        }
        
        sys.stdout.write(json.dumps(data))
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