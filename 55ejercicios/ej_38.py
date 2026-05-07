# Ejercicio 38: Top 3 Ventas (MercadoLibre)

print("==========================================")
print("Calculando Top 3 de productos más vendidos")
print("==========================================")

ventas = [500, 1000, 200, 800, 1500]

ventas.sort(reverse=True)

top3 = ventas[:3]

print(top3)