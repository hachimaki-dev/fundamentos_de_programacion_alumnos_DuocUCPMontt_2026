sueldo_base = 800000
total_bonos = 0
bonos = {"colacion": 50000, "movilizacion": 30000}
descuentos = {"AFP": 0.10, "Salud": 0.07}

for bono in bonos.values():
    total_bonos += bono

monto_total_descuentos = 0
for descuento in descuentos.values():
    monto_total_descuentos += (sueldo_base * descuento)

sueldo_liquido = sueldo_base + total_bonos - monto_total_descuentos


print(sueldo_liquido)

    
    


