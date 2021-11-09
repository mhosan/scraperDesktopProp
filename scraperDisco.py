import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

url = 'https://www.disco.com.ar/leche?_q=leche&map=ft'

s = Service('./chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_argument('--incognito')
#options.add_argument('--headless')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(service=s, options=options)

#driver.minimize_window()
xpathBuscar ='//div[@id="gallery-layout-container"]//div[contains(@class, "vtex-product-summary-2-x-nameContainer")]//span[contains(@class, "vtex-product-summary-2-x-productBrand")]'
#driver.set_page_load_timeout(30)
try:
    driver.get(url)
    #driver.implicitly_wait(30)
    unProducto = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, xpathBuscar)))
    print(f'La página terminó de cargar ok. Driver title: {driver.title}')
except TimeoutException: 
    print(f'Tiempo de espera agotado cargando la página "{url}" ')
    driver.delete_all_cookies()
    driver.quit()

#Disco:
listaDeProductos = driver.find_elements_by_xpath('//div[@id="gallery-layout-container"]//div[@class="vtex-search-result-3-x-galleryItem vtex-search-result-3-x-galleryItem--normal vtex-search-result-3-x-galleryItem--grid pa4"]//a[@draggable="false"]')
print('\n')
print('=' * 70)
print(f'La cantidad de productos leidos es: {len(listaDeProductos)}')
print('=' * 70)
print('\n')
print('*' * 70)
for producto in listaDeProductos:
    descripcion = producto.find_element_by_xpath('.//div[contains(@class, "vtex-product-summary-2-x-nameContainer")]//span[contains(@class, "vtex-product-summary-2-x-productBrand")]').text
    precio = producto.find_element_by_xpath('.//div[@class="contenedor-precio"]/span').text
    print(F'Descripcion: {descripcion}, {precio}')
    print('-' * 70)
print('*' * 70)

driver.delete_all_cookies()
driver.quit()

