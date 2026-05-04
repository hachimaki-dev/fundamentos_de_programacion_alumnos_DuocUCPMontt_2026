sueldo_base = 500000
bono_colacion = 50000
bono_movilizacion = 30000
descuento_afp = 0.1
descuento_salud = 0.07
sueldo_liquido = sueldo_base + bono_colacion + bono_movilizacion - (sueldo_base * descuento_afp) - (sueldo_base * descuento_salud)
print(sueldo_liquido)