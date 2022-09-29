#FRESH THYME MARKET
# Dynamic page scrap that use react or google (non json files)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from webdriver_manager.chrome import ChromeDriverManager


## FRESH THYME MARKET
# This installs the Chrome driver for Selenium (browser automation API)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# navigates to a webpage
# driver.get('https://discover.freshthyme.com/shop/flyer')
driver.get('https://www.freshthyme.com/weekly-ads/')

# requested browser information (in this case the title)
title = driver.title

# wait until all iframes are loaded
WebDriverWait(driver, timeout=10).until(expected_conditions.frame_to_be_available_and_switch_to_it(By.CLASS_NAME)
# Navigate to iframe
# driver.find_element(by=By.ID, value="flipp-container")

#lFrame = driver.find_element(By.TAG_NAME, 'iframe')

#for i in lFrame:
# print(lFrame)

# driver.find_element(by=By.CLASS_NAME, value="flippiframe.mainframe")
# iframe = driver.find_element(by=By.ID, value="05a0da25-87a8-4eeb-95f1-867065e53b6a")
# either price box is needed to pull items
# price_box = driver.find_elements(by=By.CLASS_NAME, value="productprices")
# driver.find_element(by=By.NAME, value="cityZipInput").send_keys("15205")
# driver.implicitly_wait(10)
# driver.find_element(by=By.ID, value="shopping-selector-update-home-store-148-instore").click()




# item_box = driver.find_elements(by=By.CLASS_NAME, value="cell-title-text")
# price_box = driver.find_elements(by=By.CLASS_NAME, value="css-1ssd8ij")

# print(lButton.text)
# for x in item_box:
#    print(x.text)
# for p in price_box:
#    print(p.text)



driver.quit()