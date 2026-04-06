# Una tienda vende potes de proteína. El usuario puede agregar potes hasta que decida finalizar. 

"""
1. Utiliza un ciclo (while) para preguntar repetidamente al usuario el precio de un suplemento a agregar al carrito. Si ingresa "0" u otro número de salida que definas, el ciclo debe terminar.
2. Lleva la cuenta del total a pagar y de la cantidad de productos ingresados.
3. Si el usuario compró 3 o más productos en total, aplícale un descuento del 10% al total al finalizar.
4. Imprime el total final a pagar y la cantidad de productos comprados.
"""

ciclo_de_tienda = True
total_de_compra = 0
cantidad_de_compra = 0

print("Bienvenido a Protein Plus!")
while ciclo_de_tienda == True:
    print("Seleccione un producto para añadirlo al carro (1-3) y ingrese 4 para continuar con el pago")
    print("1. Protein Plus Classic $2000")
    print("2. Protein Max $3000")
    print("3. Protein Plus Ultra $2400")
    print("4. Continuar a pago")
    seleccion = int(input("[]: "))
    if seleccion == 1:
        total_de_compra += 2000
        cantidad_de_compra += 1
    if seleccion == 2:
        total_de_compra += 3000
        cantidad_de_compra += 1
    if seleccion == 3:
        total_de_compra += 2400
        cantidad_de_compra += 1
    if seleccion == 4:
        break

if cantidad_de_compra > 0:
    if cantidad_de_compra >= 3:
        print(f"Total de su compra: ${total_de_compra * 0.90} [DESCUENTO APLICADO!]")
        print("Gracias por su compra!")
    if cantidad_de_compra < 3:
        print(f"Total de su compra: ${total_de_compra}")
        print("Gracias por su compra!")
else:
    print("Ningun articulo seleccionado!")