import time
from lib2to3.pgen2 import driver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

CHROME_DRIVER_PATH = '/Users/leewan/chromedriver'

PATH = 'https://app.ergodex.io/pool?active=positions-overview'

def main():
    webdriver_options = webdriver.ChromeOptions()
    webdriver_options.add_experimental_option('detach', True)

    s = Service(CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=s, options=webdriver_options)
    driver.get(PATH)

    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[13]/button')))
    button1 = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div[13]/button')
    button1.click()

    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CLASS_NAME, 'ant-list-items')))
    dashboard = driver.find_element(By.CLASS_NAME, 'ant-list-items')
    items = dashboard.find_elements(By.TAG_NAME, 'span')
    while(1):
        for item in items:
            if 'ERG / NETA' in item.text:
                print(item.text)
                break
        time.sleep(10)
    
if __name__=='__main__':
    main()