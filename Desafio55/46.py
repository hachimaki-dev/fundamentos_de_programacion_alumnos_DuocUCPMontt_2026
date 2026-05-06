ventas = {'LocalA': 150, 'LocalB': 300, 'LocalC': 100}

total = 0

for value in ventas:
    total += ventas.get(value)

print(total)