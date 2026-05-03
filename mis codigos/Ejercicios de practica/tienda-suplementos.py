total_pagar = 0
cantidad_productos = 0
print("Cada producto cuesta $100. Si compras 3 o mas obtienes un descuento de 10%")
while True:
    respuesta_user = int(input("Desea agregar un producto al carrito? 1= si 0= terminar"))
    if respuesta_user == 1:
        cantidad_productos += 1
        total_pagar += 100
        print(f"llevas {cantidad_productos} productos.")
    elif respuesta_user == 0:
        break
    else: 
        print("Respuesta invalida. vuelva a intentarlo")

if cantidad_productos >=3:
    total_pagar = total_pagar * 0.90
    print("Tienes un descuento de 10%")
    print(f"El precio total de tu compra es de {total_pagar}")
else:
    print(f"El precio total de tu compra es de {total_pagar}")

    

