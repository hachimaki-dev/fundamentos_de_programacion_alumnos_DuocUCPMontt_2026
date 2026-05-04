sueldo_base = 500000
bono_colacion = 50000
bono_movilizacion = 30000
sueldo_descontado = sueldo_base * 0.17
print(sueldo_descontado)
sueldo_liquido = sueldo_base + bono_colacion + bono_movilizacion - sueldo_descontado
print(sueldo_liquido)

