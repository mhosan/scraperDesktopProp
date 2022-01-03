from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from persisteDatos import guardaDatos

def buscar(url, driver, fuente):
    
    productoTestigo = '//ul[@class="card__photos"]//img[@class="show"]'
    listadoDeProductos = '//div[@class="main__content"]//div[@class="listing-container"]//div[@class="listing__items"]//div[contains(@class, "listing__item")]'
    descripcionProducto = './/p[@class="card__title--primary"]'
    descripcionProducto2 = './/p[@class="card__title"]'
    superficieItem = './/ul[@class="card__main-features"]//span' 
    linkDetalle = './/a[contains(@id, "id-card")]'
    detallePropiedad = '//div[@class="property-description"]//section/ul[@class="property-features collapse"]/li'

    #driver.minimize_window()
    #driver.set_page_load_timeout(30)
    try:
        driver.get(url)
        #with open(f'paginaVeaLeche.txt', 'w', encoding='utf-8') as f:
        #        f.write(driver.page_source)
        #        f.close()
        #driver.implicitly_wait(30)

        #para ver si la página carga correctamente, dando un tiempo de espera de 30 segundos o un producto testigo
        #para buscar, lo que ocurra primero. Si la página no carga sale por el except del try.
        testearPageLoad = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, productoTestigo)))
        print(f'La página terminó de cargar ok. Driver title: {driver.title}')
        localidad = driver.title[driver.title.rfind(" en")+4:len(driver.title)-12]
        listaDeProductos = driver.find_elements_by_xpath(listadoDeProductos)
        print('=' * 70)
        print(f'Cantidad de propiedades en esta página: {len(listaDeProductos)}')
        print('=' * 70)
        
        if len(listaDeProductos) > 0:
            fecha = datetime.now()
            fechaISO = fecha.isoformat()
            #print('\n')
            #print('*' * 70)
            listaLinks = [] # Lista con las propiedades de la primer página
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
                    #print(F'{descripcion2}, Superficie: {superficie}, Id: {id}, linkDetallado: {linkDetallado} ')
                    #print('-' * 120)
                    data = {'Id ': id, 'fecha': fechaISO, 'descrip': descripcion2, 'superficie': superficie, 'link': linkDetallado}
                    listaLinks.append(data)
                    #persisteDatos.guardaDatos(data, paginaPrincipal)
            for link in listaLinks:
                for key, value in link.items():
                    if key == 'link':
                        print('\n\n')
                        print(f'{key}: {value}')
                        linkCortado = value.split('--')
                        idPropiedad = int(linkCortado[1].strip())
                        driver.get(value)
                        driver.implicitly_wait(30)
                        #driver.back() #para volver a la pagina principal
                        detalle ='//div[@class="property-description"]//div[@class="property-features-title"]'
                        #driver.get(link)
                        listaDeDetalles = driver.find_elements_by_xpath(detalle)
                        #print(f'La cantidad de items con detalles es: {len(listaDeDetalles)}')
                        print('=' * 150)
                        data = {'IdPropiedad ': idPropiedad, 'fuente' : fuente, 'localidad': localidad, 'fecha': fechaISO}
                        for detalle in listaDeDetalles:
                            descripcion = detalle.find_elements_by_xpath(detallePropiedad)
                            for item in descripcion:
                                textoContenido = item.get_attribute('textContent')
                                textoContenido = textoContenido.strip()
                                textoContenido = textoContenido.replace('\n','')
                                if ":" in textoContenido: #existe clave - valor
                                    listaDetalle = textoContenido.split(':')
                                    listaDetalle[0] = listaDetalle[0].strip()
                                    listaDetalle[1] = listaDetalle[1].strip()
                                else : #no existe clave - valor, hay un solo valor.
                                    listaDetalle[0] = textoContenido
                                    listaDetalle[1] = 'Si'    
                                print(f'---> {listaDetalle[0]} : {listaDetalle[1]}')
                                data[listaDetalle[0]] = listaDetalle[1]
                            break
                        print(f'data : {data}')
                        #guardaDatos(data)    
            return
    
    except TimeoutException: 
        print(f'Tiempo de espera agotado cargando la página "{url}" ')
        #driver.delete_all_cookies()
        #driver.quit()



