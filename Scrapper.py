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
driver.get('https://www.ajio.com/men-backpacks/c/830201001')


# Navigate to ajio
time.sleep(2)

#find the height of the current page
height = driver.execute_script('return document.body.scrollHeight')
print(height)

#scroll to last
old_height = driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')

#loop till the last row of items
while True:
    driver.execute_script('return document.body.scrollHeight')
    time.sleep(2)

    new_height = driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')

    if new_height == old_height:
        break

    old_height=new_height

html = driver.page_source

with open('ajio.html','w',encoding='utf-8') as f:
    f.write(html)

    