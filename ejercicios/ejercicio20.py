catalogo = {'armas': ['espada', 'arco'], 'items': ['pocion', 'luz']}
todo_stock = []
for lista_productos in catalogo.values():
    for producto in lista_productos:
        if len(producto) > 5:
            todo_stock.append(producto)
print(todo_stock)