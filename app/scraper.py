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



def pull_comments(driver):
    try:
        wait = WebDriverWait(driver, 10)
        comment_div = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "ssul_comments"))
        )
    
    
    except Exception as e: 
        print(f"Error: {str(e)}")

def pull_header(driver):
    try:
        wait = WebDriverWait(driver, 10)
        header = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "ssul_header"))
        )
        return header.text
    
    except Exception as e: 
        print(f"Error: {str(e)}")

def pull_article(driver):
    try:
        wait = WebDriverWait(driver, 10)

        article = wait.until(
            EC.presence_of_element_located((By.ID, "realArtcContents"))
        )
        paragraphs = article.text.split('\n')

        article_content = []
        for p in paragraphs:
            if p.strip() == '':
                continue

            article_content.append({
                "type": "text",
                "info": p
            })

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
        url = "https://news.nate.com/view/20250127n06427?mid=n1008"
        driver.get(url)

        pull_article(driver)

        print("scraping complete")

        
    except Exception as e:
        print(f"Error: {str(e)}")
    
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    main()