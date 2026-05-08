ventas = {'LocalA': 150, 'LocalB': 300, 'LocalC': 100}
total = 0
for valor in ventas.values():
    total = total + valor
print(total)