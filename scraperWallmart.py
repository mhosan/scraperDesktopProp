import buscar
import driver

driver = driver.seteoDriver()

urls = ['https://www.walmart.com.ar/buscar?text=yerba',
    'https://www.walmart.com.ar/buscar?text=azucar',
    'https://www.walmart.com.ar/buscar?text=galletitas',
    'https://www.walmart.com.ar/buscar?text=gaseosas',
    'https://www.walmart.com.ar/buscar?text=shampoo',
    'https://www.walmart.com.ar/buscar?text=arroz',
    'https://www.walmart.com.ar/buscar?text=pollo',
]

for url in urls:
    buscar.buscar(url, driver, "Wallmart")

driver.quit()