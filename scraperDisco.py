import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException

url = 'https://www.latamairlines.com/ar/es/ofertas-vuelos?dataFlight=%7B%22tripTypeSelected%22%3A%7B%22label%22%3A%22Solo+ida%22%2C%22value%22%3A%22OW%22%7D%2C%22cabinSelected%22%3A%7B%22label%22%3A%22Economy%22%2C%22value%22%3A%22Economy%22%7D%2C%22passengerSelected%22%3A%7B%22adultQuantity%22%3A1%2C%22childrenQuantity%22%3A0%2C%22infantQuantity%22%3A0%7D%2C%22originSelected%22%3A%7B%22id%22%3A%22BUE_AR_CITY%22%2C%22name%22%3A%22null%22%2C%22city%22%3A%22Buenos+Aires%22%2C%22cityIsoCode%22%3A%22BUE%22%2C%22country%22%3A%22Argentina%22%2C%22iata%22%3A%22BUE%22%2C%22latitude%22%3A-34.603684%2C%22longitude%22%3A-58.381559%2C%22timezone%22%3A-3%2C%22tz%22%3A%22America%2FMendoza%22%2C%22type%22%3A%22CITY%22%2C%22countryAlpha2%22%3A%22AR%22%2C%22allAirportsText%22%3A%22xp_sales_web_searchbox_od_allAirports%22%2C%22airportIataCode%22%3A%22BUE%22%7D%2C%22destinationSelected%22%3A%7B%22id%22%3A%22MAD_ES_AIRPORT%22%2C%22name%22%3A%22Barajas+Intl.%22%2C%22city%22%3A%22Madrid%22%2C%22cityIsoCode%22%3A%22MAD%22%2C%22country%22%3A%22Espa%C3%B1a%22%2C%22iata%22%3A%22MAD%22%2C%22latitude%22%3A40.471926%2C%22longitude%22%3A-3.56264%2C%22timezone%22%3A1%2C%22tz%22%3A%22Europe%2FMadrid%22%2C%22type%22%3A%22AIRPORT%22%2C%22countryAlpha2%22%3A%22ES%22%2C%22allAirportsText%22%3Anull%2C%22airportIataCode%22%3A%22MAD%22%7D%2C%22dateGoSelected%22%3A%222021-12-18T15%3A00%3A00.000Z%22%2C%22dateReturnSelected%22%3Anull%2C%22redemption%22%3Afalse%7D'
url2 = 'https://www.disco.com.ar/leche?_q=leche&map=ft'

s = Service('./chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_argument('--incognito')
#options.add_argument('--headless')
options.add_argument('--ignore-certificate-errors')

driver = webdriver.Chrome(service=s, options=options)

#driver.minimize_window()
driver.set_page_load_timeout(30)
try:
    driver.get(url2)
    #driver.implicitly_wait(30)
    print(f'Driver title: {driver.title}')
except TimeoutException: 
    print(f'Tiempo de espera agotado cargando la página "{url2}" ')
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

"""
vuelos = driver.find_elements_by_xpath('//li[@class="sc-hZeNU czUTzo"]')
print('*' * 50)
vuelo = vuelos[0]
hora = vuelo.find_element_by_xpath('.//span[@class="sc-kkwfeq hZlYEC"]').text
print(f'Hora: {hora}')
print(f'el atributo es: {vuelo.text}')
print(f'el tipo de vuelo es: {type(vuelo)}')
"""

driver.delete_all_cookies()
driver.quit()

