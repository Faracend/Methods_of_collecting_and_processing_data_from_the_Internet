from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

s = Service('./chromedriver')
chrome_options = Options()
chrome_options.add_argument("start-maximized")

driver = webdriver.Chrome(service=s, options=chrome_options)

driver.get('https://5ka.ru/special_offers')

button = driver.find_element(By.CLASS_NAME, 'add-more-btn')
button.click()

while True:

    wait = WebDriverWait(driver, 10)
    button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'add-more-btn')))

    # button = driver.find_element(By.CLASS_NAME, 'add-more-btn')
    button.click()