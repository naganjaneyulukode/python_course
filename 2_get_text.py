from selenium import webdriver
import time

# Open Chrome Browser
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.python.org")

## Get text based on xpath
text = driver.find_element_by_xpath('//*[@id="downloads"]/a').text

print('\n Text is :', text)
time.sleep(4)

# Verify text is expected or not 
assert text == 'Download',  'Text is not expected'

time.sleep(4)
driver.close()


