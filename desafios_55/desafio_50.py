cuenta = {'Papas': 5000, 'Pizza': 10000}
subtotal = 0

for plato, precio in cuenta.items():
    print(f"{plato}: ${precio}")
    subtotal += precio

propina = subtotal * 0.10

total_con_propina = subtotal + propina

print("--------------------")
print("Total final:", total_con_propina)