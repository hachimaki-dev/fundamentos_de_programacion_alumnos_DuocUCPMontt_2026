ventas = {"pocion_curación": 100, "espada": 500, "armadura_de_hierro": 1000}

total_ventas = 0

for monto in ventas.values():
    total_ventas += monto

print(f"El total de ventas es de: ${total_ventas}")
