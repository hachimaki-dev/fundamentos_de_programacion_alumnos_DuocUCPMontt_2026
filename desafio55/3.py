personas_totales = 5
pichanga = 2
schops = 5
costo_pichanga = pichanga * 15000
costo_schops = schops * 3500
consumo = costo_pichanga + costo_schops
print(consumo)
propina = consumo * 0.1
print(propina)
monto_final = (consumo + propina) // personas_totales
print(monto_final)
