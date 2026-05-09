sueldo_base = 800000
bonos = {'colacion': 50000, 'movilizacion': 30000}
descuentos = {'AFP': 0.10, 'Salud': 0.07}

sueldo_final = sueldo_base

for monto_bono in bonos.values():
    sueldo_final += monto_bono

for porcentaje in descuentos.values():
    monto_descuento = sueldo_base * porcentaje
    sueldo_final-= monto_descuento


print(sueldo_final)