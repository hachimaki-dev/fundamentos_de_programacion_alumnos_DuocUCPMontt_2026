sueldo_base = 500000
bono_colacion = 50000
bono_movilizacion = 30000

sueldo_base_descontado = sueldo_base * 0.83

sueldo_liquido = sueldo_base_descontado + bono_colacion + bono_movilizacion

print(sueldo_liquido)