# Ejercicio 46: Suma de Ventas (Cornershop)

print("============================")
print("Calculando el total de venta")
print("============================")

ventas = {'LocalA': 150, 'LocalB': 300, 'LocalC': 100}

total = 0

for dinero in ventas.values():
    total = total + dinero

print(total)