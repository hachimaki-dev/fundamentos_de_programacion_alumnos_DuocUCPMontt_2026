sueldo_base = 500000
bono_colacion = 50000
bono_movilizacion = 30000

porcentaje_salud = 7
porcentaje_AFP = 10

descuento_salud = (sueldo_base * porcentaje_salud) / 100
descuento_AFP = (sueldo_base * porcentaje_AFP) / 100

sueldo_liquido = sueldo_base - descuento_salud - descuento_AFP + bono_colacion + bono_movilizacion

print(f"El sueldo líquido a pagar es: {sueldo_liquido}")