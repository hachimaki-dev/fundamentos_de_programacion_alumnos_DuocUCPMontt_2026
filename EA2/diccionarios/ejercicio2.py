'''Crea una lista llamada productos que contenga al menos 3 diccionarios. Cada diccionario debe tener:

    nombre
    precio
    stock

Luego:

    Recorre la lista con for.
    Muestra el nombre y precio de cada producto.
    Usa if para indicar cuáles productos tienen stock mayor que 0.
    Al final, imprime cuántos productos están disponibles.'''


productos = [
    {"nombre": "Memoria RAM 16Gb", "precio": 97990, "stock": 3},
    {"nombre": "Disco Duro 1Tb", "precio": 54990, "stock": 0},
    {"nombre": "RTX 3060", "precio": 399990, "stock": 7}
]

productos_disponibles = 0
for producto in productos:
    print(f"Producto: {producto['nombre']}, Precio: {producto['precio']}")
    
for producto in productos:
    if producto["stock"] > 0:
        productos_disponibles += 1

print(f"Productos disponibles: {productos_disponibles}")

for item in productos:
    if item["stock"] > 0:
        print(f"    -{item['nombre']}: {item['stock']} unidades en stock")