sueldo_base = 500000
bono_colacion = 50000
bono_movilizacion = 30000

porcentaje_descuento_salud = 7
porcentaje_descuento_afp = 10

sueldo_total = sueldo_base - (sueldo_base / 100 * (porcentaje_descuento_salud + porcentaje_descuento_afp)) + bono_colacion + bono_movilizacion

print(sueldo_total)
