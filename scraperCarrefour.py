import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


url = 'https://www.carrefour.com.ar/Lacteos-y-productos-frescos/Leches'

s = Service('./chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_argument('--incognito')
#options.add_argument('--headless')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(service=s, options=options)

#driver.minimize_window()
driver.set_page_load_timeout(50)
xpathBuscar ='//div[@class="lyracons-search-result-1-x-gallery flex flex-row flex-wrap items-stretch bn ph1 na4 pl9-l"]//div[@style="flex-basis: 33.3333%; max-width: 33.3333%;"]//span[@class="vtex-product-summary-2-x-productBrand vtex-product-summary-2-x-brandName t-body"]'
try:
    driver.get(url)
    #driver.implicitly_wait(30)
    #time.sleep(10)  #<-- esto es una demora estatica, siempre se ejecuta.
    unProducto = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpathBuscar)))
    print(f'La página terminó de cargar ok. Driver title: {driver.title}')
except TimeoutException: 
    print(f'Tiempo de espera agotado cargando la página "{url}" ')
    driver.delete_all_cookies()
    driver.quit()

#Carrefour:
listaDeProductos = driver.find_elements_by_xpath('//div[@class="lyracons-search-result-1-x-gallery flex flex-row flex-wrap items-stretch bn ph1 na4 pl9-l"]//div[@style="flex-basis: 33.3333%; max-width: 33.3333%;"]/section[@style="max-width: 300px;"]')
print('\n')
print('=' * 70)
print(f'La cantidad de productos leidos es: {len(listaDeProductos)}')
print('=' * 70)

print('\n')
print('*' * 70)
for producto in listaDeProductos:
    descripcion = producto.find_element_by_xpath('.//span[@class="vtex-product-summary-2-x-productBrand vtex-product-summary-2-x-brandName t-body"]').text
    #precio = producto.find_element_by_xpath('.//div[@class="contenedor-precio"]/span').text
    precio ="nada"
    print(F'Descripcion: {descripcion}, {precio}')
    print('-' * 70)
print('*' * 70)

driver.delete_all_cookies()
driver.quit()

