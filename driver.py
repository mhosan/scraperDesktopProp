from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def seteoDriver():
    
    PROXY = "78.138.99.76:1080"

    s = Service('./chromedriver.exe')
    options = webdriver.ChromeOptions()
    options.add_argument('--incognito')
    #options.add_argument('--headless')
    options.add_argument('--ignore-certificate-errors')
    #options.add_argument('--proxy-server=%s' % PROXY)
    driver = webdriver.Chrome(service=s, options=options)
    return driver

