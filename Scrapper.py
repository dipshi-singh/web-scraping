from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert


import time

#open browser
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

prefs = {"profile.default_content_setting_values.geolocation": 2}
chrome_options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.smartprix.com/mobiles')


# Navigate to ajio
time.sleep(2)

driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[1]/input').click()
time.sleep(1)
driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[2]/input').click()


time.sleep(2)

#find the height of the current page
old_height = driver.execute_script('return document.body.scrollHeight')

while True:
    driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/div[1]/div[2]/div[3]').click()
    time.sleep(1)

    new_height=driver.execute_script('return document.body.scrollHeight')

    if new_height == old_height:
        break

    old_height=new_height

html = driver.page_source

with open('smartprix.html','w',encoding='utf-8') as f:
    f.write(html)

