catalogo = {'armas': ['espada', 'arco'], 'items': ['pocion', 'luz']}
todo_stock = []
for producto in catalogo.values():  #Recorre los valores del diccionario armas e items.
    for item in producto:           #Recorre cada item dentro de la lista.
        if len(item)>=5:
            todo_stock.append(item)

print(todo_stock)