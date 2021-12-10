import buscar
import driver
import time

driver = driver.seteoDriver()

urlsOri = ['https://www.argenprop.com/departamento-venta-localidad-moron-mor',
        'https://www.argenprop.com/departamento-venta-localidad-la-plata-lp',
        'https://www.argenprop.com/departamento-venta-localidad-trenque-lauquen-tl',]

urls = ['https://www.argenprop.com/departamento-venta-localidad-moron-mor',
        'https://www.argenprop.com/departamento-venta-localidad-la-plata-lp',
        'https://www.argenprop.com/departamento-venta-localidad-trenque-lauquen-tl',]


for url in urls:
    buscar.buscar(url, driver, "Argenprop")
    time.sleep(5)
# driver.quit()


