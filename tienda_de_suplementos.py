'''
1. Utiliza un ciclo (while) para preguntar repetidamente al usuario el precio de un suplemento a agregar al carrito. Si ingresa "0" u otro número de salida que definas, el ciclo debe terminar.
2. Lleva la cuenta del total a pagar y de la cantidad de productos ingresados.
3. Si el usuario compró 3 o más productos en total, aplícale un descuento del 10% al total al finalizar.
4. Imprime el total final a pagar y la cantidad de productos comprados.
'''

contador_productos = 0
total_a_pagar = 0

while True :
    precio_suplemento = int (input("Ingrese el precio del producto: "))

    if precio_suplemento == 0 :
        break

    contador_productos += 1

    total_a_pagar += precio_suplemento

if contador_productos >= 3 :
    print(f"¡Tiene un descuento del 10%!")
    total_a_pagar = int (total_a_pagar * 0.9)
    
print(f"El precio total es {total_a_pagar}.")
print(f"Compró un total de {contador_productos} productos.")