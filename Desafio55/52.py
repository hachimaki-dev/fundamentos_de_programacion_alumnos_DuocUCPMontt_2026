sueldo_base = 800000
bonos = {'colacion': 50000, 'movilizacion': 30000}
descuentos = {'AFP': 0.10, 'Salud': 0.07}
sueldo_total = sueldo_base

for bono in bonos.values():
    sueldo_total += bono

for desc in descuentos.values():
    sueldo_base = 800000
    sueldo_base = sueldo_base * desc
    sueldo_total -= sueldo_base

print(sueldo_total)