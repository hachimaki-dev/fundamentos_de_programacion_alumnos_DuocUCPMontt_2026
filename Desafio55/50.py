cuenta = {'Papas': 5000, 'Pizza': 10000}
total = 0

for nombre, precio in cuenta.items():
    total += precio

total += total*0.1

print(f"Total final: {total}")