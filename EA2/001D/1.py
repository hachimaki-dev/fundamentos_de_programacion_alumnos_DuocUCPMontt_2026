sueldo = 500000
bono_colacion = 50000
movilizacion = 30000

por_desc_salud_afp = sueldo * 0.17
liq= sueldo + bono_colacion + movilizacion - (por_desc_salud_afp)

print(int(liq))