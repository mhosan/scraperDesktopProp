import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

url = 'https://www.carrefour.com.ar/Lacteos-y-productos-frescos/Leches'

s = Service('./chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_argument('--incognito')
#options.add_argument('--headless')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(service=s, options=options)
#driver.minimize_window()

driver.get(url)
driver.implicitly_wait(30)
print(f'Driver title: {driver.title}')

#Carrefour:

listaDeProductos = driver.find_elements_by_xpath('//div[@class="lyracons-search-result-1-x-gallery flex flex-row flex-wrap items-stretch bn ph1 na4 pl9-l"]//div[@style="flex-basis: 25%; max-width: 25%;"]')
print('\n')
print('=' * 70)
print(f'La cantidad de productos leidos es: {len(listaDeProductos)}')
print('=' * 70)
"""
print('\n')
print('*' * 70)
for producto in listaDeProductos:
    descripcion = producto.find_element_by_xpath('.//div[contains(@class, "vtex-product-summary-2-x-nameContainer")]//span[contains(@class, "vtex-product-summary-2-x-productBrand")]').text
    precio = producto.find_element_by_xpath('.//div[@class="contenedor-precio"]/span').text
    print(F'Descripcion: {descripcion}, {precio}')
    print('-' * 70)
print('*' * 70)
"""

driver.quit()

