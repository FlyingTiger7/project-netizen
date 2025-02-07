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
        content_div = wait.until(
            EC.presence_of_element_located((By.ID, "realArtcContents"))
        )
        
        content = []
        
        # Get text content
        paragraphs = [
            para.strip() 
            for para in content_div.text.split('\n') 
            if para.strip() and not para.startswith('==')
        ]
        
        # Get images
        images = []
        image_divs = content_div.find_elements(By.CLASS_NAME, "articleMedia")
        for div in image_divs:
            img = div.find_element(By.TAG_NAME, "img")
            url = img.get_attribute("src")
            if url and '///' in url:
                url = url.split('///').pop()
            if not url.startswith('http'):
                url = 'https://' + url
            images.append({
                "type": "image",
                "url": url
            })

        # Combine text and images
        current_image = 0
        for para in paragraphs:
            content.append({
                "type": "text",
                "content": para
            })
            
            if current_image < len(images):
                content.append(images[current_image])
                current_image += 1
        
        return content

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
            "content": get_maincontent(driver),
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