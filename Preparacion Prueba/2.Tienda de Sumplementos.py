contadorproductos = 0
valortotal = 0

while True:
    productoagregado = int(input("Ingrese Valor del producto a agregar:  (Ingrese 0 si no quiere llevar nada mas)"))
    valortotal = valortotal + productoagregado
    if productoagregado == 0:
        break
    contadorproductos += 1
    print (f"\nUsted lleva{productoagregado} productos")


if contadorproductos >= 3:
    valortotal = valortotal - valortotal*0.1

print (f"Usted compro {contadorproductos} productos, por lo que tiene que pagar ${int(valortotal)}")