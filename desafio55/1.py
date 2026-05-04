sueldo_base = 500000
bono_colacion = 50000
bono_movilizacion = 30000

porcentaje_descuento_salud = 0.07
porcentaje_descuento_afp = 0.1 

descuento_salud = sueldo_base  * porcentaje_descuento_salud
descuento_afp = sueldo_base  * porcentaje_descuento_afp

sueldo_liquido = sueldo_base + bono_colacion + bono_movilizacion - descuento_salud - descuento_afp 

print(f"El sueldo a pagar es {sueldo_liquido}")
