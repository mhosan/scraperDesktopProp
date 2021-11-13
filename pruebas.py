from datetime import datetime
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import driver

driver = driver.seteoDriver()

productoTestigo = "//div[@class='search results']//div[@id='catalog-listing']//ul/li//a[@class='product-item-link']"
listadoDeProductos = '//div[@class="search results"]//div[@id="catalog-listing"]//ul/li'

stockDisponible = "//div[@class='search results']//div[@id='catalog-listing']//ul/li//div[@class='stock available']/span"

descripcionProducto = "//div[@class='search results']//div[@id='catalog-listing']//ul/li//a[@class='product-item-link']"
precioProducto = "//div[@class='search results']//div[@id='catalog-listing']//ul/li//div[@class='price-box price-final_price']//span[@class='price']"

url = 'https://maxiconsumo.com/sucursal_capital/catalogsearch/result/?q=leche'

driver.get(url)
# with open(f'paginaVeaLeche.txt', 'w', encoding='utf-8') as f:
#        f.write(driver.page_source)
#        f.close()
listaDeProductos = driver.find_elements_by_xpath(listadoDeProductos)
print('\n')
print('=' * 70)
print(f'La cantidad de productos leidos es: {len(listaDeProductos)}')
print('=' * 70)
print('\n')
if len(listaDeProductos) > 0:
    fecha = datetime.now()
    fechaISO = fecha.isoformat()
    print('\n')
    print('*' * 70)
    for producto in listaDeProductos:
        descripcion = producto.find_element_by_xpath(descripcionProducto).text
        stock = producto.find_element_by_xpath(stockDisponible).text
        print(f'descripcion: {descripcion} - stock: {stock}')
        """ if stock.text == 'Disponible':
            print('Disponible')
            precio = producto.find_element_by_xpath(precioProducto).text
            print(F'Descripcion: {descripcion}, {precio}')
            print('-' * 70) 
        else:
            print(f'{descripcion}: No disponible')
        """
    print('*' * 70)
driver.quit()
