sueldo_base = 800000
bonos = {'colacion': 50000, 'movilizacion': 30000}
descuentos = {'AFP': 0.10, 'Salud': 0.07}
for i in bonos.values():    
    sueldo_bono = sueldo_base + i
for i in descuentos.values():
    sueldo_descuentos = sueldo_base * i
sueldo_total = sueldo_bono - sueldo_descuentos
print(sueldo_total)