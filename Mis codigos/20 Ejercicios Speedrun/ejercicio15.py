# Ejercicio 15: Boss Final 🐉
# Tienes un diccionario llamado tienda.
# Cada clave representa un producto, y su valor es otro diccionario con:
#     'precio'
#     'stock'
# Tu tarea es calcular el valor total de todo el inventario.
# Eso significa multiplicar precio * stock de cada producto y sumar todos esos resultados.
# Guarda el total en la variable capital_total.
# Ejemplo:
# Si
#     tienda = {'pocion': {'precio': 50, 'stock': 3}, 'espada': {'precio': 200, 'stock': 1}}
# entonces
#     capital_total = 350

tienda = {'pocion': {'precio': 50, 'stock': 3}, 'espada': {'precio': 200, 'stock': 1}}
capital_total = 0

# for clave, valor in tienda.items():
#     capital_total += valor["precio"] * valor["stock"]

for valor in tienda.values():
    capital_total += valor["precio"] * valor["stock"]

print(capital_total)  # 350