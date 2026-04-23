# Crea una lista llamada productos que contenga al menos 3 diccionarios. 
# Cada diccionario debe tener:

# nombre
# precio
# stock
# Luego:

# 1. Recorre la lista con for.
# 2. Muestra el nombre y precio de cada producto.
# 3. Usa if para indicar cuáles productos tienen stock mayor que 0.
# 4. Al final, imprime cuántos productos están disponibles.

stock_total = 0
productos_disponibles = 0
numero_producto = 1

productos = [
    {"nombre": "arroz", "precio": 1000, "stock": 50},
    {"nombre": "fideos", "precio": 700, "stock": 60},
    {"nombre": "lentejas", "precio": 1200, "stock": 0}
]

for producto in productos:
    print(f"Producto {numero_producto}: Nombre: {producto["nombre"]} | Precio: {producto["precio"]}")
    numero_producto += 1

for stock in productos:
    if stock["stock"] > 0:
        stock_total += stock["stock"]
        productos_disponibles += 1

print(f"Stock total: {stock_total}\nProductos disponibles: {productos_disponibles}")




