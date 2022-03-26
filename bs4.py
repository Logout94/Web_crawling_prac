import sys
import os
import requests
import time
from bs4 import BeautifulSoup

url = 'http://luka7.net/'
def main():
    #while(1):
        rs = requests.get(url)
        
        if rs.status_code == 200:
            html = rs.content
            soup = BeautifulSoup(html, 'html.parser')
            ADA = soup.select_one('div#coinList > div')
            print(ADA)
            #print(soup)
            #print(soup.find('div'))
            #ul = soup.select_one('#rc-tabs-12-panel-positions-overview > div > div > div > div > div > ul > div:nth-child(1) > div > div.ergo-flex.ergo-flex-direction--row.ergo-flex-justify--space-between.ergo-flex-align-items--center > div:nth-child(1) > div > div:nth-child(2) > div > div:nth-child(2) > div > div > span')
            #print(ul)
        else:
            print(rs.status_code)
        time.sleep(0.5)
if __name__=='__main__':
    main()