from selenium.webdriver.common.by import By
import mailsender
from product import Product
import driver_manager

BASE_URL = 'https://www.trendyol.com/'
PRODUCT = 'apple/z0yj000y0-macbook-air-13-i3-1-1ghz-16gb-256gb-space-gray-ozel-konfig-p' \
          '-81411508?boutiqueId=583864&merchantId=141868'  # sys.argv[1]
PRODUCT_URL = BASE_URL + PRODUCT
product = Product(PRODUCT_URL)

driver = driver_manager.init_driver()
driver.get(product.url)

PRICE = driver.find_element(By.CSS_SELECTOR, product.price_locator) \
    .text.replace(' TL', '') \
    .replace('.', '')
size = len(PRICE)

product.price = PRICE[:size - 3]
product.name = driver.find_element(By.CSS_SELECTOR, product.name_locator).text

message = '''\
Subject: Trendyol Product Price Info

Price of the product : {} TL

Name of the product : "FIX non ascii characters" 

Click here : {}

'''.format(product.price, product.url)

password = input('Enter the password: ')
mailsender.send('testautomationwithmaksu@gmail.com', password, message)
print('Messge sent : {}'.format(message))

driver.quit()
