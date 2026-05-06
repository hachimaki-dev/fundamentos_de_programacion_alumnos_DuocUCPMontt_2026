pichanga = 15000
schops = 3500
sustotal = 0
sustotal = sustotal + pichanga * 2
sustotal = sustotal + schops * 5
propina = sustotal * 0.10
monto_final = sustotal + propina
monto_idividual = monto_final // 5
print(sustotal)
print(f"total a pagar {monto_final}, cada persona deve pagar por separado {monto_idividual}")