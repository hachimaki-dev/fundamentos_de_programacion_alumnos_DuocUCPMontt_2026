sueldo_base = 500000
bono_colacion = 50000
bono_movilizacion = 30000

sueldo_liquido = sueldo_base - (sueldo_base*0.07) - (sueldo_base*0.1) + bono_colacion + bono_movilizacion

print(sueldo_liquido)