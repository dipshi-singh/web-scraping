from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


import time

#open browser
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# Navigate to google
driver.get('https://www.google.com')
time.sleep(2)

#search on google
input = driver.find_element(by=By.XPATH, value='//*[@id="APjFqb"]')
input.send_keys('selenium')
time.sleep(1)
input.send_keys(Keys.ENTER)