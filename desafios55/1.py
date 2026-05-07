sueldo_base = 500000
bono_colacion = 50000
bono_movilicacion = 30000

descuento_salud = sueldo_base/100*7

descuento_AFP = sueldo_base/10

sueldo_base = sueldo_base - descuento_salud
sueldo_base = sueldo_base - descuento_AFP

sueldo_liquido = sueldo_base + bono_colacion + bono_movilicacion

print(sueldo_liquido)