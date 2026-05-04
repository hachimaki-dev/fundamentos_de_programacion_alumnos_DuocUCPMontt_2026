# Ejercicio 20: Filtrar productos por longitud
# Define el diccionario catalogo = {'armas': ['espada', 'arco'], 'items': ['pocion', 'luz']}. 
# Crea una lista vacía llamada todo_stock. 
# Recorre todas las categorías y agrega a esa lista solo los productos que tengan más de 5 letras. 
# Luego, imprime todo_stock.

catalogo = {'armas': ['espada', 'arco'], 'items': ['pocion', 'luz']}
todo_stock = []

# for clave, valor in catalogo.items():
#     for palabra in valor:
#         if len(palabra) > 5:
#             todo_stock.append(palabra)

for valor in catalogo.values():
    for palabra in valor:
        if len(palabra) > 5:
            todo_stock.append(palabra)

print(todo_stock)