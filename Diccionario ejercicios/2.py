"""
### Ejercicio 2: Nivel medio

Crea una lista llamada `productos` que contenga al menos 3 diccionarios. Cada diccionario debe tener:

* `nombre`
* `precio`
* `stock`

Luego:

1. Recorre la lista con `for`.
2. Muestra el nombre y precio de cada producto.
3. Usa `if` para indicar cuáles productos tienen stock mayor que 0.
4. Al final, imprime cuántos productos están disponibles.
"""

productos = [
    {
        "Nombre": "Galletas Wafers Cuisina & Co Avellana 150 g", "Precio": 1590, "Stock": 33,
    },
    {
        "Nombre": "Cocadas Poppies 190 g", "Precio": 2990, "Stock": 0,
    },
    {
        "Nombre": "Galletas Gustino Choco Rollls con Chocolate Amargo 125 g", "Precio": 3190, "Stock": 19,
    }
]

contador = 0

disponibles = []

for producto in productos:
    print(f"Los productos son los siguientes: {producto['Nombre']}\nPrecio: {producto['Precio']}")
    if producto["Stock"] > 0:
        contador += 1
        disponibles.append(producto['Nombre'])

lista_final = ", ".join(disponibles)

print(f"\nTotal disponibles: {contador}")
print(f"Que serian: {lista_final}")