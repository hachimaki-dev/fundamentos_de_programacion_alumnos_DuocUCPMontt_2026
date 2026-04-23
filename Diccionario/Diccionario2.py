productos = [
    {"nombre": "Fideos", "precio": 500, "stock": "10 Kilos"},
    {"nombre": "Arroz", "precio": 1000, "stock": "15 Kilos"},
    {"nombre": "Papas", "precio": 800, "stock": "28 Kilos" }
]
for producto in productos:
    print(producto["nombre"], producto["precio"], producto["stock"])