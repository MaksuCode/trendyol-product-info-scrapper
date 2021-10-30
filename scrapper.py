from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import mailsender

BASE_URL = 'https://www.trendyol.com/'
PRODUCT = 'apple/z0yj000y0-macbook-air-13-i3-1-1ghz-16gb-256gb-space-gray-ozel-konfig-p-81411508?boutiqueId=583864' \
          '&merchantId=141868 '
PRODUCT_URL = BASE_URL + PRODUCT

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get(PRODUCT_URL)

PRICE = driver.find_element(By.CSS_SELECTOR, 'div.product-price-container span.prc-dsc').text.replace(' TL', '')\
    .replace('.', '')
size = len(PRICE)
PRICE = PRICE[:size-3]

message = '''\
Subject: Trendyol Product Price Info

Price of the product is {}

Click here : {}

'''.format(PRICE, PRODUCT_URL)

password = input('Enter the password: ')
mailsender.send('testautomationwithmaksu@gmail.com', password, message)

driver.quit()
