sueldo_base = 500000
bono_colacion = 50000
bono_movilizacion = 30000
porcentaje_descuento_salud = 7
porcentaje_descuento_AFP = 10
Descuento_salud = (sueldo_base * porcentaje_descuento_salud)/100
Descuento_AFP = (sueldo_base * porcentaje_descuento_AFP)/100
sueldo_liquido = sueldo_base - Descuento_salud - Descuento_AFP+ bono_movilizacion + bono_colacion
print(f"El sueldo liquido a percibir es de {sueldo_liquido}")