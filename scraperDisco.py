import buscar
import driver

driver = driver.seteoDriver()

urls = ['https://www.disco.com.ar/leche?_q=leche&map=ft'
]

for url in urls:
    buscar.buscar(url, driver, "Wallmart")

driver.quit()

