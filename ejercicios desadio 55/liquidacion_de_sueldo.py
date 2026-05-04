sueldo_base = 500000
bono_colacion = 50000
bono_movilizacion = 30000
descuento_salud = sueldo_base*0.07
descuento_AFP = sueldo_base*0.1
descuento_final = descuento_AFP + descuento_salud
sueldo_base = sueldo_base + bono_colacion + bono_movilizacion
sueldo_liquido = sueldo_base - descuento_final
print(sueldo_liquido)