sueldo_base = 500000
colacion = 50000
movilizacion = 30000

porcentaje_descuento_afp = 10
porcentaje_salud = 7

descuento_afp = (sueldo_base * porcentaje_descuento_afp) / 100
descuento_salud = (sueldo_base * porcentaje_salud) / 100

sueldo_liquido = sueldo_base - descuento_afp - descuento_salud + colacion + movilizacion 

print(f"el sueldo liquido a percibir es: {sueldo_liquido}")

