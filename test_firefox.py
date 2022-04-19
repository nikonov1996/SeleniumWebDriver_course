import pytest
import time
from requests import request
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver(request):
    ffoptions = Options()
    
    # ffoptions.add_argument('headless')
    ffoptions.headless = True 
    ffdriver = Service('./geckodriver-v0.31.0-linux64/geckodriver')
    ffdriver = webdriver.Firefox(service=ffdriver, options=ffoptions)

    #ffdriver.implicitly_wait(10)
    
    request.addfinalizer(ffdriver.quit)
    
    return ffdriver


def testChrome(driver):
    driver.get('https://selenium-python.readthedocs.io/index.html')
    #print(driver.get_cookies())
    
    search_input = driver.find_element(By.CSS_SELECTOR,'#searchbox input[type="text"]')
    #time.sleep(10)
    # search_input.send_keys("Testing value")
    # search_submit = driver.find_element(By.CSS_SELECTOR,'#searchbox input[type="submit"]')
    # search_submit.click()

    name = search_input.get_attribute("name")
    type = search_input.get_attribute("type")
    html = search_input.get_attribute('outerHTML')

    
    print(f'name = {name} / type = {type} / html = {html}' )
    # Result: name = q / type = text / html = <input type="text" name="q">
    # time.sleep(10)
    

    