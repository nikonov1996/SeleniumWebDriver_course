import pytest
from requests import request
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver(request):
    chromeoptions = Options()
   
    chromeoptions.add_argument("headless")
    chromedriver = Service('./chromedriver_linux64/chromedriver')
    chromedriver = webdriver.Chrome(service=chromedriver,options=chromeoptions)
    
    request.addfinalizer(chromedriver.quit)
    
    return chromedriver


def testChrome(driver):
    driver.get('http://www.google.com')
    