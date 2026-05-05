sueldo_base = 500000
bono_colacion = 50000
movilizacion = 30000
salud = 7
afp = 10

descuentos_afp = (sueldo_base * afp ) / 100
descuentos_salud = (sueldo_base * salud) / 100

sueldo_liquido = (sueldo_base - descuentos_afp - descuentos_salud + bono_colacion + movilizacion)

print(sueldo_liquido)