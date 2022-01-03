import buscar
import driver
import time

driver = driver.seteoDriver()

urlsOri = ['https://www.argenprop.com/departamento-venta-localidad-moron-mor',
        'https://www.argenprop.com/departamento-venta-localidad-la-plata-lp',
        'https://www.argenprop.com/departamento-venta-localidad-trenque-lauquen-tl',]

urls = ['https://www.argenprop.com/departamento-venta-localidad-moron-mor',
        'https://www.argenprop.com/departamento-venta-localidad-la-plata-lp',
        'https://www.argenprop.com/departamento-venta-localidad-trenque-lauquen-tl',
        'https://www.argenprop.com/departamento-venta-localidad-pilar-pil',
        'https://www.argenprop.com/departamento-venta-localidad-san-justo-lm',
        'https://www.argenprop.com/departamento-venta-localidad-martinez']


for url in urls:
    buscar.buscar(url, driver, "Argenprop")
    time.sleep(5)
# driver.quit()


