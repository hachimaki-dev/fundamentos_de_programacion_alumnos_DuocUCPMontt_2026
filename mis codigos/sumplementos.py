cantidad = int(input("Ingrese la cantidad de suplementos: "))
precio = int(input("Ingrese el precio unitario: "))
while True:
    if precio == 0:
        print("El precio no puede ser cero, por favor ingrese un valor válido.")
        break
    elif cantidad >=3:
        print("Tiene un descuento del 10%")
        descuento = 0.1
        print("Total a pagar: ", (cantidad * precio) - (cantidad * precio * descuento))
        break
    else:        
        print("No tiene descuento")
        print("Total a pagar: ", cantidad * precio)