from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from time import sleep

chromedriver_path = './chromedriver'
service = Service(executable_path=chromedriver_path)

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1366,768") 
driver = webdriver.Chrome(service=service, options=options)
url = 'http://ecodata.kz:3838/app_dg_map_ru/'

driver.get(url)

word = input() 

if word == 'close':
    driver.quit()