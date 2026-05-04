sueldo_Base = 500000
colacion = 50000
movilizacion = 30000
descuento_afp = sueldo_Base/100*10
descuento_salud = sueldo_Base/100*7
sueldo_liquido = sueldo_Base - descuento_salud - descuento_afp + colacion + movilizacion
print(sueldo_liquido)