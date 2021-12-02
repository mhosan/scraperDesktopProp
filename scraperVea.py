import buscar
import driver
import time

driver = driver.seteoDriver()

urlsOri = ['https://www.vea.com.ar/leche?map=ft',
           'https://www.vea.com.ar/yerba?map=ft',
           'https://www.vea.com.ar/azucar?map=ft',
           'https://www.vea.com.ar/galletitas?map=ft',
           'https://www.vea.com.ar/gaseosas?map=ft',
           'https://www.vea.com.ar/arroz?map=ft',
           'https://www.vea.com.ar/shampoo?map=ft',
           'https://www.vea.com.ar/pollo?map=ft'
           ]
urls = [   'https://www.vea.com.ar/shampoo?map=ft',
        ]

for url in urls:
    buscar.buscar(url, driver, "Vea")
    time.sleep(5)
# driver.quit()
