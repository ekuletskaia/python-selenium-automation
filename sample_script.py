from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


from time import sleep

# get the path to the ChromeDriver executable
driver_path = './chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.maximize_window()
driver.implicitly_wait(5) #up to 5 sec

# open the url
driver.get('https://www.google.com/')

# populate search field
search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('Tea')

# wait for 4 sec
# sleep(4)

# click search button
driver.find_element(By.NAME, 'btnK').click()

# verify search results
assert 'tea' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')

driver.quit()
