ventas = {'LocalA': 150, 'LocalB': 300, 'LocalC': 100}


total_ganancias = 0


for monto in ventas.values():
    total_ganancias += monto

print(total_ganancias)