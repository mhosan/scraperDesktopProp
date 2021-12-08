from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def buscar(url, driver, paginaPrincipal):
    
    productoTestigo = '//ul[@class="card__photos"]//img[@class="show"]'
    listadoDeProductos = '//div[@class="main__content"]//div[@class="listing-container"]//div[@class="listing__items"]//div[contains(@class, "listing__item")]'
    descripcionProducto = './/p[@class="card__title--primary"]'
    descripcionProducto2 = './/p[@class="card__title"]'
    superficieItem = './/ul[@class="card__main-features"]//span' 
    linkDetalle = './/a[contains(@id, "id-card")]'

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
            #listadoLinks = []
            for producto in listaDeProductos:
                try:
                    descripcion = producto.find_element_by_xpath(descripcionProducto).text
                    descripcion2 = producto.find_element_by_xpath(descripcionProducto2).text
                    #precio = producto.find_element_by_xpath(precioProducto).text
                    superficie = producto.find_element_by_xpath(superficieItem).text
                    id = producto.find_element_by_tag_name('a').get_attribute('data-item-card')
                    #link= producto.find_element_by_partial_link_text('Ver').get_attribute('href')
                    linkDetallado = producto.find_element_by_xpath(linkDetalle).get_attribute('href')
                    #listadoLinks.append(linkDetallado)
                    #detalles(driver, linkDetallado)
                    #driver.back()
                except:
                    descripcion = "No encontrado"
                    superficie = "0"
                if superficie != "0":
                    print(F'{descripcion2}, Superficie: {superficie}, Id: {id}, link: , linkDetallado: {linkDetallado} ')
                    print('-' * 120)
                    #data = {'Pagina ': paginaPrincipal, 'fecha': fechaISO, 'descrip': descripcion, 'precio': precio}
                    #persisteDatos.guardaDatos(data, paginaPrincipal)
            print('*' * 70)
            
            """
            for link in listadoLinks :
                detalle ='//div[@class="property-description"]//div[@class="property-features-title"]'
                driver.get(link)
                listaDeDetalles = driver.find_elements_by_xpath(detalle)
                print('\n')
                print('=' * 70)
                print(f'La cantidad de items con detalles es: {len(listaDeDetalles)}')
                print('=' * 70)
            """        
            return
    except TimeoutException: 
        print(f'Tiempo de espera agotado cargando la página "{url}" ')
        #driver.delete_all_cookies()
        #driver.quit()

def detalles(driver, link):
    detalle ='//div[@class="property-description"]//div[@class="property-features-title"]'
    driver.get(link)
    listaDeDetalles = driver.find_elements_by_xpath(detalle)
    print('\n')
    print('=' * 70)
    print(f'La cantidad de items con detalles es: {len(listaDeDetalles)}')
    print('=' * 70)
    


