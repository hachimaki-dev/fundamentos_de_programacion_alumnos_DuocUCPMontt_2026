total_precio = 0
cantidad_productos = 0

print("******TIENDA DE SUMPLEMENTOS******")
while True:
    # solicitar datos al usuario
    precio_unitario = int(input("¿cual es el precio unitario del suplemento? "))

    if precio_unitario < 0:
        break
    
    total_precio = total_precio + precio_unitario
    cantidad_productos = cantidad_productos + 1