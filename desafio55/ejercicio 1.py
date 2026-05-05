sueldo_base = 500000
colacion = 50000
movilizacion = 30000

descuento_de_salud = sueldo_base * 0.07

descuento_afp = sueldo_base * 0.10


sueldo_liquido = (sueldo_base + colacion + movilizacion) - (descuento_de_salud + descuento_afp)

print(f"El sueldo a recibir es de: {sueldo_liquido}" )