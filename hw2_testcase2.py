from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = './chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.maximize_window()

# open the url
driver.get('https://www.target.com/')

# steps
driver.find_element(By.ID, 'search').send_keys('kids clothing')
driver.find_element(By.XPATH, '//button[text()="search"]').click()
sleep(5)

# verification
actual_text = driver.find_element(By.XPATH, '//div[@data-test="resultsHeading"]').text

assert "kids clothing" in actual_text, f'Error! "kids clothing" is not in the page'
print('Test case passed.')

driver.quit()