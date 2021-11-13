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
listadoDeProductos = '//div[@class="search results"]//div[@id="catalog-listing"]//ul/li//div[@class="product details product-item-details box-info"]'
stockDisponible = './/div[@class="name-rating"]//div[@class="stock available"]/span'
#descripcionProducto = ".//a[@class='product-item-link']"
precioProducto = ".//div[@class='price-box price-final_price']//span[@data-label='Incl. impuestos']/span[@class='price']"

url = 'https://maxiconsumo.com/sucursal_capital/catalogsearch/result/?q=leche'

try:
    driver.get(url)
    # with open(f'paginaVeaLeche.txt', 'w', encoding='utf-8') as f:
    #        f.write(driver.page_source)
    #        f.close()
    productoVerificar = WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.XPATH, productoTestigo)))
except TimeoutException:
    print(f'Tiempo de espera agotado cargando la página "{url}" ')
    # driver.delete_all_cookies()
    # driver.quit()
else:
    print('\n', '=' * 70)
    print(f'La página terminó de cargar ok. Driver title: {driver.title}')
    print('=' * 70, '\n')
    listaDeProductos = driver.find_elements_by_xpath(listadoDeProductos)
    listadoDisponibles = driver.find_elements_by_xpath(stockDisponible)
    print('\n', '=' * 70)
    print(f'La cantidad de productos leidos es: {len(listaDeProductos)}')
    print('=' * 70, '\n')
    if len(listaDeProductos) > 0:
        fecha = datetime.now()
        fechaISO = fecha.isoformat()
        print('\n')
        print('*' * 70)
        for i in range(len(listaDeProductos)):
            producto = listaDeProductos[i]
            print(f'{i + 1}.- Producto: {listaDeProductos[i].text}')
            print(f'{i + 1}.- Stock disponible: {listadoDisponibles[i].text}')
            descripcion = listaDeProductos[i].text
            disponibilidad = listadoDisponibles[i].text
            disponibilidad = disponibilidad.strip()
            if disponibilidad == 'Disponible':
                precio = producto.find_element_by_xpath(".//div[@class='price-box price-final_price']//span[@data-label='Incl. impuestos']/span[@class='price']").text
                print(f'Precio: {precio}')

