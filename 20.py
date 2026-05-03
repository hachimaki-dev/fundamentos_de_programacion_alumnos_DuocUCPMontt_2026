catalogo = {'armas': ['espada', 'arco'], 'items': ['pocion', 'luz']}

todo_stock = []

for categoria in catalogo:
    for producto in catalogo[categoria]:
        if len(producto) > 5:
            todo_stock.append(producto)

print(todo_stock)