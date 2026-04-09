"""
2. Tienda de Suplementos (Con Ciclos)
Una tienda vende potes de proteína. El usuario puede agregar potes hasta que decida finalizar.

Requerimientos:
1. Utiliza un ciclo (while) para preguntar repetidamente al usuario el precio de un suplemento a agregar al carrito. Si ingresa "0" u otro número de salida que definas, el ciclo debe terminar.
2. Lleva la cuenta del total a pagar y de la cantidad de productos ingresados.
3. Si el usuario compró 3 o más productos en total, aplícale un descuento del 10% al total al finalizar.
4. Imprime el total final a pagar y la cantidad de productos comprados.
"""
Salida = ""
Cuenta = 0
Productos = 0
Precio = 0
while Salida != "Si":
    Productos = int(input("Cuantos suplementos vas a llevar? "))
    Precio = int(input("Cuanto vas a costar? "))
    Cuenta = Cuenta + Productos * Precio
    print(f"Esta saliendo en total ${Cuenta}")
    Salida = input("Quieres salir? ")
if Productos >= 3:
    Cuenta = Cuenta * 0.9
    print("Estas de suerte, hay una oferta")
    print(f"Te va a costar {Cuenta}")
else:
    print(f"Te va a costar {Cuenta}")