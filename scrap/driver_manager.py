from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def init_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    return webdriver.Chrome(ChromeDriverManager().install(), options=options)


