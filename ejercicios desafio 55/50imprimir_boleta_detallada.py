cuentas = {"papas" : 5000, "pizza" : 10000}
total = 0
total_comida = 0
for comida, precio in cuentas.items():
    total = total + precio
propina = total *0.1
total_final = propina + total
print(f"total final: {total_final}")