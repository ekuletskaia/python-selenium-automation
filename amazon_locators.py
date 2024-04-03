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
driver.get('https://www.amazon.com/ap/register?showRememberMe=true&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&prevRID=CB8TZDYYCF5T6HJK3YPD&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=usflex&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')

# locators
driver.find_element(By.CSS_SELECTOR, '[aria-label="Amazon"]')
driver.find_element(By.CSS_SELECTOR, '.a-spacing-small')
driver.find_element(By.ID, 'ap_customer_name')
driver.find_element(By.ID, 'ap_email')
driver.find_element(By.ID, 'ap_password')
driver.find_element(By.CSS_SELECTOR, '.a-alert-content')
driver.find_element(By.ID, 'ap_password_check')
driver.find_element(By.ID, 'continue')
driver.find_element(By.XPATH, '//a[text()="Conditions of Use"]')
driver.find_element(By.XPATH, '//a[text()="Privacy Notice"]')
driver.find_element(By.ID, 'ab-enhanced-registration-link')

print("Test case passed")
driver.quit()
