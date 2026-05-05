sueldo_base = 500000
bono_colacion = 50000
movilizacion = 30000

porcentaje_salud = 0.07
porcentaje_afp = 0.10

total_sueldo = sueldo_base + bono_colacion + movilizacion

descuento_salud = sueldo_base * porcentaje_salud
descuento_afp = sueldo_base * porcentaje_afp
total_descuentos = descuento_salud + descuento_afp
sueldo_liquido = total_sueldo - total_descuentos

print(f"tu total de descuento es {sueldo_liquido}")
