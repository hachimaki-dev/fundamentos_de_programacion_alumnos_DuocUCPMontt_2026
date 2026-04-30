catalogo = {
        "Armas": ["Espada", "Arco", "Hacha"],
        "Pociones": ["Luz", "Maná", "Vida"]
}

todo_stock = []

for categoria in catalogo:

    for i in catalogo[categoria]:
        if len(i) > 4:
            todo_stock.append(i)
        else:
            continue

print(todo_stock)
