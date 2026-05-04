sueldo_base = 500000
bono_colacion = 50000  
movilizacion = 30000

porcentaje_descuento_afp = 10
porcentaje_descuento_salud = 7 

descuento_afp = (sueldo_base * porcentaje_descuento_afp) / 100 


descuento_salud = (sueldo_base * porcentaje_descuento_salud) / 100

sueldo_liquido = sueldo_base - descuento_afp - descuento_salud + bono_colacion + movilizacion

print (f"El sueldo liquido a recibir es {sueldo_liquido}")
