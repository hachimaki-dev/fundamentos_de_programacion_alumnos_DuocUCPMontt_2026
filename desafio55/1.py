sueldo_base = 500000
bono_colacion = 50000
bono_movilizacion = 30000

descuento_salud = 35000
descuento_afp = 50000

sueldo_liquido = sueldo_base - (descuento_afp + descuento_salud)

bonos = bono_colacion + bono_movilizacion
print(sueldo_liquido + bonos)