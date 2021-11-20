import buscar
import driver
import time

driver = driver.seteoDriver()

urls = ['https://maxiconsumo.com/sucursal_capital/catalogsearch/result/?q=leche',
           'https://maxiconsumo.com/sucursal_capital/catalogsearch/result/?q=yerba',
           'https://maxiconsumo.com/sucursal_capital/catalogsearch/result/?q=azucar',
           'https://maxiconsumo.com/sucursal_capital/catalogsearch/result/?q=galletitas',
           'https://maxiconsumo.com/sucursal_capital/catalogsearch/result/?q=arroz',
           'https://maxiconsumo.com/sucursal_capital/catalogsearch/result/?q=shampoo',
           'https://maxiconsumo.com/sucursal_capital/catalogsearch/result/?q=pollo'
           ]
urlsTest = ['https://maxiconsumo.com/sucursal_capital/catalogsearch/result/?q=azucar'
        ]

for url in urls:
    buscar.buscar(url, driver, "Maxiconsumo")
    time.sleep(5)
# driver.quit()
