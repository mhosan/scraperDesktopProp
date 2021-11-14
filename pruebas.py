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

#Disco
url = 'https://www.disco.com.ar/leche?_q=leche&map=ft'

productoTestigo = '//div[contains(@class,"vtex-flex-layout-0-x-flexColChild")]//div[@id="gallery-layout-container"]//div[contains(@class,"vtex-search-result-3-x-galleryItem")]//div[contains(@class,"vtex-product-summary-2-x-nameContainer")]//span'

listadoDeProductos = '//div[contains(@class,"vtex-flex-layout-0-x-flexCol")]//div[contains(@class,"vtex-flex-layout-0-x-flexColChild")]//div[@id="gallery-layout-container"]//div[contains(@class,"vtex-search-result-3-x-galleryItem")]'

#descripcionProducto = './/div[contains(@class, "vtex-product-summary-2-x-nameContainer")]//span[contains(@class, "vtex-product-summary-2-x-productBrand")]'
descripcionProducto = '//div[contains(@class,"vtex-flex-layout-0-x-flexColChild")]//div[@id="gallery-layout-container"]//div[contains(@class,"vtex-search-result-3-x-galleryItem")]//div[contains(@class,"vtex-product-summary-2-x-nameContainer")]//span'

precioProducto = './/div[@class="contenedor-precio"]/span'

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
    print('\n', '=' * 70)
    print(f'La cantidad de productos leidos es: {len(listaDeProductos)}')
    print('=' * 70, '\n')
    if len(listaDeProductos) > 0:
        fecha = datetime.now()
        fechaISO = fecha.isoformat()
        print('\n')
        print('*' * 70)
        for producto in listaDeProductos:
            descripcion = producto.find_element_by_xpath(descripcionProducto).text
            print(f'Producto descripcion: {descripcion}')
