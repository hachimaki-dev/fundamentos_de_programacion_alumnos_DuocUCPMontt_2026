""" Una tienda vende potes de proteína.
 El usuario puede agregar potes hasta que decida finalizar.

Requerimientos:
1. Utiliza un ciclo (while) para preguntar repetidamente al usuario 
el precio de un suplemento a agregar al carrito. Si ingresa "0" 
u otro número de salida que definas, el ciclo debe terminar.

2. Lleva la cuenta del total a pagar y de la cantidad de productos ingresados.

3. Si el usuario compró 3 o más productos en total, 
aplícale un descuento del 10% al total al finalizar.
4. Imprime el total final a pagar y la cantidad de productos comprados."""

articulo = 0    
total_precio = 0
while True:
    
    precio = int(input("cual es el precio del suplemento a agregar al carrito?"))
    print("press 0 para finalizar")
    articulo +