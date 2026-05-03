# Tienes un diccionario llamado tienda.

# Cada clave representa un producto, y su valor es otro diccionario con:

#    'precio'
#    'stock'

# Tu tarea es calcular el valor total de todo el inventario.

# Eso significa multiplicar precio * stock de cada producto y sumar todos esos resultados.

# Guarda el total en la variable capital_total.

tienda = {
    "prod1": {
        "precio": 1500,
        "stock": 10
        },
    "prod2": {
        "precio": 1500,
        "stock": 10
        },
    "prod3": {
        "precio": 1500,
        "stock": 10
        },
    "prod4": {
        "precio": 1500,
        "stock": 10
        },
    "prod5": {
        "precio": 1500,
        "stock": 10
        }
}

capital_total = 0

for valor in tienda.values():
    capital_total += valor.get("precio") * valor.get("stock")

print(capital_total)