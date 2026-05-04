Sueldo_base = 500000
bono_colacion = 50000
bono_movilización = 30000

porcentaje_descuento_afp = 10
porcentaje_descuento_salud = 7

descuento_afp = (Sueldo_base * porcentaje_descuento_afp) / 100

descuento_salud = (Sueldo_base * porcentaje_descuento_salud) / 100

sueldo_liquido = Sueldo_base - descuento_afp - descuento_salud + bono_colacion + bono_movilización

print(f"El sueldo liquido a recibir es {sueldo_liquido}")