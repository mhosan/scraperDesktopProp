import buscar
import driver

driver = driver.seteoDriver()

urls = ['https://www.walmart.com.ar/buscar?text=yerba',
        'https://www.walmart.com.ar/buscar?text=leche'
]
for url in urls:
    buscar.buscar(url, driver)

driver.quit()