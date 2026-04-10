productos = 0
total_pagar = 0

while True:
    productos_elegidos = int(input("agregue la cantidad de productos: "))
    if productos_elegidos == 0:
        print(f"llevas {productos} productos elegidos")
        print(f"Y el total a pagar es: {total_pagar}")
        break
    precio_elegido = int(input("agregue el precio de su producto: "))

    
    productos = productos + productos_elegidos
    total_pagar = total_pagar + precio_elegido
    