import time 
import sys 



sueldo_base = 500000
bono_de_colación = 50000
movilicación = 30000
descuento_1 = 7
descuento_2 = 10

descuento_1 = (sueldo_base * descuento_1) / 100
descuento_2 = (sueldo_base * descuento_2) / 100
sueldo_total = (sueldo_base + bono_de_colación + movilicación) - (descuento_1 + descuento_2)
print (f"El sueldo total a recibir es de ${sueldo_total}")

