sueldo_base = 500000
bono_colacion = 50000
movilizacion = 30000
salud_d1 = sueldo_base/100*7
afp_d2 = sueldo_base/10

sueldo_base = sueldo_base - salud_d1
sueldo_base = sueldo_base - afp_d2
sueldo_final = sueldo_base + bono_colacion + movilizacion
print(sueldo_final)