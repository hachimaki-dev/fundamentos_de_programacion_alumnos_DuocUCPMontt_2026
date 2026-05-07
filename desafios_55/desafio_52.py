sueldo_base = 800000
bonos = {'colacion': 50000, 'movilizacion': 30000}
descuentos = {'AFP': 0.10, 'Salud': 0.07}

total_bonos = 0

for bono in bonos.values():
    total_bonos += bono

sueldo_bruto = sueldo_base + total_bonos

total_descuentos = 0

for porcentaje in descuentos.values():
    total_descuentos += (sueldo_base * porcentaje)

sueldo_liquido = sueldo_bruto - total_descuentos

print(sueldo_liquido)