cuentas = {'Papas': 5000, 'pizza': 10000}
total = 0 
for plato, precio in cuentas.items():
    total = total + precio
total_propina = total + total * 0.10
print("total final: ",  total_propina)