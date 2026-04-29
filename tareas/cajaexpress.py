opcion = 0
while opcion != 2:
    print("1 . Atender a un cliente")
    print("2 .Cerrar caja")
    opcion = int(input("Ingrese opcion : "))
    if opcion == 1:
        total_cliente = 0
        cantidad_productos = int(input("Cuantos productos desea llevar?"))
        for i in range(cantidad_productos):
            print(f"producto {i + 1}")
            precio_producto = int(input("Cuanto cuesta el producto?"))
            total_cliente = precio_producto + total_cliente
        print(f"el total de productos son {cantidad_productos} y el total a pagar es : {total_cliente}")
    if opcion == 2:
        print("Cerrando caja..")
        print(f"Total del dia {total_cliente}")
    else :
        print("Ingrese opcion valida!")