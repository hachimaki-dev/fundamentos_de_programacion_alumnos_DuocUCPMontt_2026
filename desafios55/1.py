sueldo_base = 500000
bono_colacion = 50000
bono_movilizacion = 30000
descuento_salud = sueldo_base * 0.07
descuento_afp = sueldo_base * 0.10
sueldo_liquido = sueldo_base + bono_colacion + bono_movilizacion - descuento_salud - descuento_afp
print(sueldo_liquido)
