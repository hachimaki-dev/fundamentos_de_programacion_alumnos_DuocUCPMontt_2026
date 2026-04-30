catalogo = {'Armas': ['Espada', 'Arco'],
            'Items': ['Pocion', 'Luz']}

todo_stock = []

for key, objetos in catalogo.items() :
    for objeto in objetos :
        if len(objeto) > 5 :
            todo_stock.append(objeto)

print(todo_stock)