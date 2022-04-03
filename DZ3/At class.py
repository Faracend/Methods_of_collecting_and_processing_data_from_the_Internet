try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import Select
except:
    from os import system as cmd
    cmd('pip install selenium')

driver = webdriver.Chrome(executable_path="./chromedriver")
driver.get('https://gb.ru/login')

elem = driver.find_element(By.ID, 'user_email')
elem.send_keys('vladislavargun2007@gmail.com')

elem = driver.find_element(By.ID, 'user_password')
elem.send_keys('Vladislaver200710')

elem.send_keys(Keys.ENTER)

elem = driver.find_element(By.XPATH, "//a[contains(@href, '/users/')]")
href = elem.get_attribute('href')
driver.get(href)

elem = driver.find_element(By.XPATH, "//a[contains(@href, '/users/')]")
href = elem.get_attribute('href')
driver.get(href)

elem = driver.find_element(By.CLASS_NAME, 'text-sm')
href = elem.get_attribute('href')
driver.get(href)

hours = driver.find_element(By.NAME, 'user[time_zone]')
select = Select(hours)
select.select_by_value("Moscow")

hours.submit()