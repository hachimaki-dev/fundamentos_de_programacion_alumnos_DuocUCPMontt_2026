sueldo_base = 500000
bono_colacion = 50000
bono_movilizacion = 30000
#Descuento de 7% por salud y 10% por AFP al sueldo base
descuento_salud = sueldo_base * (7/100)
descuento_afp = sueldo_base * (10/100)
descuento_total = descuento_afp + descuento_salud
sueldo_base = sueldo_base - descuento_total
sueldo_liquido = sueldo_base + bono_colacion + bono_movilizacion
print("--Su sueldo base es---")
print(sueldo_base)
print("--Su sueldo liquido es--")
print(sueldo_liquido)


