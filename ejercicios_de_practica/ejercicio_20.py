catalogo = {"armas": ["espada", "arco", "bolas de fuego"], "pociones": ["mana", "veneno", "vida"]}

todo_stock = []

for lista_productos in catalogo.values():
    for producto in lista_productos:
        if len(producto) > 4:
            todo_stock.append(producto)

print(f"Productos del catalogo con mas de 4 letras son los siguientes: {todo_stock}")