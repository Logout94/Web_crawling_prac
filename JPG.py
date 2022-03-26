import time
from lib2to3.pgen2 import driver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

CHROME_DRIVER_PATH = '/Users/leewan/chromedriver'

PATH = 'https://www.jpg.store/'

def find_floor(driver, nft):
    el = driver.find_element(By.CLASS_NAME, 'nav-search-bar_navbarSearchContainer__2kA_M').find_element(By.TAG_NAME, 'input')
    el.send_keys(nft)
    el.send_keys(Keys.ENTER)

    col = driver.find_element(By.XPATH, '//*[@id="filter-bar"]/div/div[1]')
    col.click()
    #lst = driver.find_element(By.CSS_SELECTOR, '#filter-bar > div > div:nth-child(1) > div.properties-modal.border.border-radius-4 > div > div')
    item_list = col.find_element(By.CLASS_NAME, 'properties-modal-scroll').find_elements(By.CLASS_NAME, 'align-items-center')
    for item in item_list:
        tmp = item.find_element(By.TAG_NAME, 'div')
        if nft.lower() == tmp.get_attribute('textContent').lower():
            #action.move_to_element(item)
            item.click()
    pri = driver.find_element(By.XPATH, '//*[@id="filter-bar"]/div/div[3]')
    pri.click()
    prop_list = pri.find_elements(By.TAG_NAME, 'span')
    for prop in prop_list:
        if 'Low to High' in prop.get_attribute('textContent'):
            prop.click()
    driver.refresh()
    time.sleep(1)
    low_price = driver.find_element(By.ID, 'asset-price')

    return low_price.text

def main():
    webdriver_options = webdriver.ChromeOptions()
    webdriver_options.add_experimental_option('detach', True)

    s = Service(CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=s, options=webdriver_options)
    driver.get(PATH)

    floor_price = find_floor(driver, 'pavia') 
    print(floor_price)

if __name__=='__main__':
    main()