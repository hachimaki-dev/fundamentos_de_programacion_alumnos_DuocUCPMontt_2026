catalogo = {"armas": ["espada", "arco"], "items": ["pocion", "luz"]}
todo_stock = []
for producto in catalogo["armas"]:
    if producto in catalogo["armas"]:
        if len(producto) > 5:
            todo_stock.append(producto)
for producto in catalogo["items"]:
    if producto in catalogo["items"]:
        if len(producto) > 5:
            todo_stock.append(producto)
print(todo_stock)