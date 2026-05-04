sueldo_base = 500000
bono_colacion = 50000
bono_movilizacion = 30000

salud = sueldo_base*0.07
afp = sueldo_base*0.10

sueldo_liquido = sueldo_base - salud - afp + bono_colacion + bono_movilizacion
print(sueldo_liquido)