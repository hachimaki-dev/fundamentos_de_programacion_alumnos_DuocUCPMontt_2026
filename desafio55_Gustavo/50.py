cuenta={
    "Papas":5000,
    "Pizza":10000
}

total = 0

for plato,precio in cuenta.items():
    total += precio

total_con_propina = total * 1.1
print(f"Total final {total_con_propina}")