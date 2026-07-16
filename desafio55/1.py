sueldo_base = 500000
bono_colacion = 50000
bono_transporte = 30000
sueldo_líquido = 0
desc7SALUD = 0.07
desc10AFP = 0.10
descuento_salud = sueldo_base * desc7SALUD
descuento_AFP = sueldo_base * desc10AFP
sueldo_líquido = sueldo_base - descuento_salud - descuento_AFP + bono_colacion + bono_transporte
print(sueldo_líquido)