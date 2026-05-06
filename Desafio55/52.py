sueldo_base = 800000
sueldo_liquido = sueldo_base
bonos = {'colacion': 50000, 'movilizacion': 30000}
descuentos = {'AFP': 0.10, 'Salud': 0.07}

for descuento in descuentos.values():
    sueldo_liquido -= sueldo_base * descuento

for bono in bonos.values():
    sueldo_liquido += bono

print(sueldo_liquido)