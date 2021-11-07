from selenium import webdriver
from selenium.webdriver.chrome.service import Service

url = 'https://www.latamairlines.com/ar/es/ofertas-vuelos?dataFlight=%7B%22tripTypeSelected%22%3A%7B%22label%22%3A%22Solo+ida%22%2C%22value%22%3A%22OW%22%7D%2C%22cabinSelected%22%3A%7B%22label%22%3A%22Economy%22%2C%22value%22%3A%22Economy%22%7D%2C%22passengerSelected%22%3A%7B%22adultQuantity%22%3A1%2C%22childrenQuantity%22%3A0%2C%22infantQuantity%22%3A0%7D%2C%22originSelected%22%3A%7B%22id%22%3A%22BUE_AR_CITY%22%2C%22name%22%3A%22null%22%2C%22city%22%3A%22Buenos+Aires%22%2C%22cityIsoCode%22%3A%22BUE%22%2C%22country%22%3A%22Argentina%22%2C%22iata%22%3A%22BUE%22%2C%22latitude%22%3A-34.603684%2C%22longitude%22%3A-58.381559%2C%22timezone%22%3A-3%2C%22tz%22%3A%22America%2FMendoza%22%2C%22type%22%3A%22CITY%22%2C%22countryAlpha2%22%3A%22AR%22%2C%22allAirportsText%22%3A%22xp_sales_web_searchbox_od_allAirports%22%2C%22airportIataCode%22%3A%22BUE%22%7D%2C%22destinationSelected%22%3A%7B%22id%22%3A%22MAD_ES_AIRPORT%22%2C%22name%22%3A%22Barajas+Intl.%22%2C%22city%22%3A%22Madrid%22%2C%22cityIsoCode%22%3A%22MAD%22%2C%22country%22%3A%22Espa%C3%B1a%22%2C%22iata%22%3A%22MAD%22%2C%22latitude%22%3A40.471926%2C%22longitude%22%3A-3.56264%2C%22timezone%22%3A1%2C%22tz%22%3A%22Europe%2FMadrid%22%2C%22type%22%3A%22AIRPORT%22%2C%22countryAlpha2%22%3A%22ES%22%2C%22allAirportsText%22%3Anull%2C%22airportIataCode%22%3A%22MAD%22%7D%2C%22dateGoSelected%22%3A%222021-12-18T15%3A00%3A00.000Z%22%2C%22dateReturnSelected%22%3Anull%2C%22redemption%22%3Afalse%7D'
url2 = 'https://www.vea.com.ar/leche?map=ft'

s = Service('./chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_argument('--incognito')

driver = webdriver.Chrome(service=s, options=options)
#driver.maximize_window()
driver.get(url2)
print(f'Driver title: {driver.title}')
listaProductos = driver.find_elements_by_id('gallery-layout-container')
producto = listaProductos[0]
precio = producto.find_element_by_class_name('contenedor-precio').get_attribute('innerHTML')
print(f'precio: {precio}')

#vuelos = driver.find_elements_by_xpath('//li[@class="sc-hZeNU czUTzo"]')
#vuelo = vuelos[0]
#hora = vuelo.find_element_by_xpath('.//span[@class="sc-kkwfeq hZlYEC"]').text
#print(f'Hora: {hora}')


driver.quit()

