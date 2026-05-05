sueldo_base = 500000
bono_colacion = 50000
bono_movilizacion = 30000
fonasa = 50000
afp = 35000

sueldo_liquido = sueldo_base - (fonasa + afp) + (bono_colacion + bono_movilizacion)
print(sueldo_liquido)
