
ventas = {'taza': 500, 'plato': 1200, 'vaso': 300}
total_ventas = 0

for precio in ventas.values():
    total_ventas += precio

print(f"El total de las ventas es: {total_ventas}")

