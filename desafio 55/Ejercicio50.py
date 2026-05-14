cuenta = {'Papas': 5000, 'Pizza': 10000}

total = 0

for _, precio in cuenta.items():
    total += precio

print('Total final:', int(total * 1.10))