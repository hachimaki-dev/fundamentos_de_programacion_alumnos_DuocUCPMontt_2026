# Tienes un diccionario llamado catalogo.

# Cada clave es una categoría y su valor es una lista de productos.

# Debes recorrer todas las categorías y guardar en la lista todo_stock únicamente los productos que tengan más de 4 letras.

catalogo = {
    "comida": [
        "porotos",
        "nuez",
        "pan",
        "garbanzo",
        "pizza"
    ],
    "bebida": [
        "coca-cola",
        "agua",
        "sprite"
    ],
    "condimento": [
        "oregano",
        "sal",
        "azucar"
    ]
}

todo_stock = []

for valor in catalogo.values():
    for i in range(len(valor)):
        if len(valor[i]) > 4:
            todo_stock.append(valor[i])

print(todo_stock)