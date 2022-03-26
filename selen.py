import time
from lib2to3.pgen2 import driver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

CHROME_DRIVER_PATH = '/Users/leewan/chromedriver'
#PATH = 'http://luka7.net/'
PATH = 'https://coinmarketcap.com/ko/'
coin_dict = {}

def serch_name(driver, coinName):
    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[1]/div[1]/div[1]/div/div[2]/div[3]/div/div[1]')))
    el = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[1]/div[1]/div/div[2]/div[3]/div/div[1]')
    el.click()
    #WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CLASS_NAME, 'bzyaeu-1.jytGVs')))
    driver.implicitly_wait(2)
    query = driver.find_element(By.CLASS_NAME, 'bzyaeu-1.jytGVs')
    query = query.find_element(By.TAG_NAME, 'input')
    query.send_keys(coinName)
    driver.implicitly_wait(2)
    query.send_keys(Keys.ENTER)
def main():
    coin_list = ['occ', 'ergo', 'ada', 'tether']
    webdriver_options = webdriver.ChromeOptions()
    webdriver_options.add_experimental_option('detach', True)

    s = Service(CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=s, options=webdriver_options)
    driver.get(PATH)

    while(1):
        #driver.implicitly_wait(10)
        for coin in coin_list:
            serch_name(driver, coin)
            price_val = driver.find_element(By.CLASS_NAME, 'priceValue').text
            coin_dict[coin] = price_val
        print(coin_dict)
        time.sleep(5)
    ''' 
    driver.implicitly_wait(2)
    #WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#coinList>div.BTC>div.minus")))
    el = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[1]/div[1]/div/div[2]/div[3]/div/div[1]')
    el.click()
    driver.implicitly_wait(1)
    #query = driver.find_element(By.CSS_SELECTOR, '#tippy-30 > div > div > div > div > div.bzyaeu-1.jytGVs > div.bzyaeu-2.gSgMWQ > input')
    query = driver.find_element(By.CLASS_NAME, 'bzyaeu-1.jytGVs')
    query = query.find_element(By.TAG_NAME, 'input')
    #tippy-25 > div > div > div > div > div.bzyaeu-1.jytGVs > div.bzyaeu-2.gSgMWQ > input
    query.send_keys('occ')
    driver.implicitly_wait(1)
    query.send_keys(Keys.ENTER)

    price_val = driver.find_element(By.CLASS_NAME, 'priceValue').text
    print(price_val)
    el = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[1]/div[1]/div/div[2]/div[3]/div/div[1]')
    el.click()
    driver.implicitly_wait(1)
    query = driver.find_element(By.CLASS_NAME, 'bzyaeu-1.jytGVs')
    query = query.find_element(By.TAG_NAME, 'input')
    #tippy-25 > div > div > div > div > div.bzyaeu-1.jytGVs > div.bzyaeu-2.gSgMWQ > input
    query.send_keys('ergo')
    query.send_keys(Keys.ENTER)
    #query = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/input')
    #query.send_keys('occ')
    #query.send_keys(Keys.ENTER)
    while(1):
        WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#coinList>div.BTC>div.minus")))
        coin_row = driver.find_element(By.CSS_SELECTOR, '.ADA')
        ADA_USDT_curr = coin_row.find_element(By.CSS_SELECTOR, '.usd').text
        if ADA_USDT_curr != ADA_USDT_pre:
            print(ADA_USDT_curr)
        ADA_USDT_pre = ADA_USDT_curr
    '''
if __name__=='__main__':
    main()