productos=[
    {"nombre":"Trufa","precio":1000,"stock":20},
    {"nombre":"Roll de canela","precio":1500,"stock":20},
    {"nombre":"pie de limon","precio":2000,"stock":0}
]
productos_disponible = 0

for producto in productos:
    print(f"Producto: {producto["nombre"]}")
    print(f"Precio ${producto["precio"]}")
    print(f"Stock: {producto["stock"]}")
    
    if producto["stock"] > 0:
        print("Disponible")
        productos_disponible += 1
    else:
        print("no disponible")

print(f"Total de productos disponibles: {productos_disponible}")




