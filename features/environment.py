from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


def browser_init(context):
    """
    :param context: Behave context
    """
    driver_path = './chromedriver.exe'
    context.driver = webdriver.Chrome(executable_path=driver_path)

    context.driver.maximize_window()
    context.driver.implicitly_wait(6)
    context.wait = WebDriverWait(context.driver, 10)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
