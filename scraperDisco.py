import buscar
import driver
import time

driver = driver.seteoDriver()

urls = ['https://www.disco.com.ar/leche?_q=leche&map=ft',
           'https://www.disco.com.ar/yerba?_q=yerba&map=ft',
           'https://www.disco.com.ar/azucar?_q=azucar&map=ft',
           'https://www.disco.com.ar/galletitas?_q=galletitas&map=ft',
           'https://www.disco.com.ar/gaseosas?_q=gaseosas&map=ft',
           'https://www.disco.com.ar/arroz?_q=arroz&map=ft',
           'https://www.disco.com.ar/shampoo?_q=shampoo&map=ft',
           'https://www.disco.com.ar/pollo?_q=pollo&map=ft'
           ]
urlsTest = ['https://www.disco.com.ar/pollo?_q=pollo&map=ft'

        ]

for url in urls:
    buscar.buscar(url, driver, "Disco")
    time.sleep(5)
# driver.quit()

