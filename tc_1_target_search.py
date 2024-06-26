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
driver.find_element(By.XPATH, '//span[text()="Sign in"]').click()
sleep(1)
driver.find_element(By.XPATH, '//a[@data-test="accountNav-signIn"]').click()

# verification
sleep(2)
actual_text = driver.find_element(By.XPATH, '//span[text()="Sign into your Target account"]').text
driver.find_element(By.ID, "login")
#driver.find_element(By.ID, "login")
assert "Sign into your Target account" in actual_text, f"Error! -Sign into your Target account- not in {actual_text}"
print("Test case passed.")
driver.quit()
