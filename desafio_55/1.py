# liquidacion de sueldo base

sueldo_base = 500000
bono_colacion = 50000
movilizacion = 30000

descuento_afp = 10
descuento_salud = 7

descuento_afp = (sueldo_base * descuento_afp) / 100

descuento_salud = (sueldo_base * descuento_salud) / 100

sueldo_liquido = sueldo_base - descuento_afp - descuento_salud + bono_colacion + movilizacion

print(f"El sueldo liquido a recibir es de {sueldo_liquido}")


