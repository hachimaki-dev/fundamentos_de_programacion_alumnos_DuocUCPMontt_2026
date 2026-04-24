producto = {
    "nombre": "Notebook",
    "precio": 599990,
    "stock": 10}

for clave in producto:
    print(clave)



for clave, valor in producto.items():
    print(clave, valor)


for valor in producto.values():
    print(valor)