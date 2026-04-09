total_pagar= 0
carrito= 0
maximo_productos= 10
print("BIENVENIDO")
while True:
    carrito= float(input("Cuantos productos desea llevar: "))
    precio_producto= float(input("Ingrese precio del producto: "))
    total_pagar= total_pagar + precio_producto
    if carrito > 3:
        print("TIENES UN 10% DE DESCUENTO!")
        total_con_descuento= total_pagar - (total_pagar * 0.10)
        total= total_con_descuento * carrito
        print(f"TU TOTAL ES DE {total} POR {carrito} PRODUCTOS")
    else:
        total_pagar= total_pagar * carrito
        print(f"TU TOTAL ES DE {total_pagar} POR {carrito} PRODUCTOS")
    break

print("GRACIAS POR COMPRAR CON NOSOTROS")