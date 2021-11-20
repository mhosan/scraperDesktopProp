from datetime import datetime
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import persisteDatos 

def buscar(url, driver, supermercado):
    if supermercado == "Wallmart":
        productoTestigo = '//ul//li/div[@class="prateleira__item price-checked"]//div[@class="prateleira__content"]//a[@class="prateleira__name"]' 
        listadoDeProductos = '//ul//li/div[@class="prateleira__item price-checked"]'
        descripcionProducto = './/div[@class="prateleira__content"]//a[@class="prateleira__name"]'
        precioProducto = './/div[@class="prateleira__content"]//a[@class="prateleira__price"]/span[@class="prateleira__best-price originalBestPrice"]'
    if supermercado == "Disco" or supermercado == "Vea":
        productoTestigo ='//div[@id="gallery-layout-container"]//div[contains(@class, "vtex-product-summary-2-x-nameContainer")]//span[contains(@class, "vtex-product-summary-2-x-productBrand")]'
        listadoDeProductos = '//div[contains(@class,"pr0")]//div[contains(@class,"vtex-flex-layout-0-x-flexColChild")]//div[@class="vtex-flex-layout-0-x-flexRow"]//div[@id="gallery-layout-container"]//div[contains(@class,"vtex-search-result-3-x-galleryItem")]'
        descripcionProducto = './/div[contains(@class, "vtex-product-summary-2-x-nameContainer")]//span[contains(@class, "vtex-product-summary-2-x-productBrand")]'
        precioProducto = './/div[@class="vtex-flex-layout-0-x-flexRow vtex-flex-layout-0-x-flexRow--mainRow-price-box"]//div[@class="contenedor-precio"]//span'
    if supermercado == "Maxiconsumo":
        productoTestigo ="//div[@class='search results']//div[@id='catalog-listing']//ul/li//a[@class='product-item-link']"
        listadoDeProductos = '//div[@class="search results"]//div[@id="catalog-listing"]//ul/li//div[@class="product details product-item-details box-info"]'
        stockDisponible = './/div[@class="name-rating"]//div[@class="stock available"]/span'
        precioProducto = ".//div[@class='price-box price-final_price']//span[@data-label='Incl. impuestos']/span[@class='price']"

    #driver.minimize_window()
    xpathBuscar = productoTestigo
    #driver.set_page_load_timeout(30)
    try:
        driver.get(url)
        #with open(f'paginaVeaLeche.txt', 'w', encoding='utf-8') as f:
        #        f.write(driver.page_source)
        #        f.close()
        
        #driver.implicitly_wait(30)
        productoTestigo = WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.XPATH, xpathBuscar)))
        print(f'La página terminó de cargar ok. Driver title: {driver.title}')
        listaDeProductos = driver.find_elements_by_xpath(listadoDeProductos)
        print('\n')
        print('=' * 70)
        print(f'La cantidad de productos leidos es: {len(listaDeProductos)}')
        print('=' * 70)

        if len(listaDeProductos) > 0:
            fecha = datetime.now()
            fechaISO = fecha.isoformat()
            print('\n')
            print('*' * 70)
            for producto in listaDeProductos:
                
                if supermercado == "Maxiconsumo":
                    descripcion = producto.find_element_by_xpath(".//a[@class='product-item-link']").text
                    disponibilidad = producto.find_element_by_xpath(stockDisponible).text
                    disponibilidad = disponibilidad.strip()
                    if disponibilidad == "Disponible":
                        precio = producto.find_element_by_xpath(".//div[@class='price-box price-final_price']//span[@data-label='Incl. impuestos']/span[@class='price']").text    
                        precio = precio.strip()
                    else:
                        precio = "0"
                else:
                    try:
                        descripcion = producto.find_element_by_xpath(descripcionProducto).text
                        precio = producto.find_element_by_xpath(precioProducto).text
                    except:
                        descripcion = "No encontrado"
                        precio = "0"
                
                if precio != "0":
                    print(F'Descripcion: {descripcion}, {precio}')
                    print('-' * 70)
                    data = {'supermercado': supermercado, 'fecha': fechaISO, 'descrip': descripcion, 'precio': precio}
                    persisteDatos.guardaDatos(data, supermercado)
            print('*' * 70)
        return
    except TimeoutException: 
        print(f'Tiempo de espera agotado cargando la página "{url}" ')
        #driver.delete_all_cookies()
        #driver.quit()

 