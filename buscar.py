from datetime import datetime
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from persisteDatos import guardarDatos 

def buscar(url, driver, supermercado):
    if supermercado == "Wallmart":
        productoTestigo = '//ul//li/div[@class="prateleira__item price-checked"]//div[@class="prateleira__content"]//a[@class="prateleira__name"]' 
        listadoDeProductos = '//ul//li/div[@class="prateleira__item price-checked"]'
        descripcionProducto = './/div[@class="prateleira__content"]//a[@class="prateleira__name"]'
        precioProducto = './/div[@class="prateleira__content"]//a[@class="prateleira__price"]/span[@class="prateleira__best-price originalBestPrice"]' 
    #driver.minimize_window()
    xpathBuscar = productoTestigo
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
            descripcion = producto.find_element_by_xpath(descripcionProducto).text
            precio = producto.find_element_by_xpath(precioProducto).text
            print(F'Descripcion: {descripcion}, {precio}')
            print('-' * 70)
            data = {'supermercado': supermercado, 'fecha': fechaISO, 'descripcion': descripcion, 'precio': precio}
            guardarDatos(data, supermercado)
        print('*' * 70)
