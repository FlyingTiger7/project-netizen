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

        content_divs = driver.find_element(By.ID, "main").text
        paragraphs = content_divs.split('\n')

        article_content = []
        for p in paragraphs:
            if p.strip() == '':
                continue

            article_content.append({
                "type": "text",
                "info": p
            })
        
        article = driver.find_element(By.ID, "main")
        # Get all child elements
        content_elements= article.find_elements(By.TAG_NAME, "*")

        div_position_counter = 0
        br_flag = False
        for content in content_elements:
            if content.tag_name == 'br':
                if br_flag == True:
                    div_position_counter += 1
                br_flag = not (br_flag)

            if content.tag_name == 'img':
                image_info = {
                    "type": "image",
                    "info": content.get_attribute('src')
                }
                article_content.insert(div_position_counter,image_info)
                div_position_counter += 1

        return article_content
            
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