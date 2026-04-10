#1. Utiliza un ciclo (while) para preguntar repetidamente al usuario el precio de un suplemento a agregar al carrito.
    #Si ingresa "0" u otro número de salida que definas, el ciclo debe terminar.
#2. Lleva la cuenta del total a pagar y de la cantidad de productos ingresados.
#3. Si el usuario compró 3 o más productos en total, aplícale un descuento del 10% al total al finalizar.
#4. Imprime el total final a pagar y la cantidad de productos comprados.

precio_ingresado = 0
agregar_producto = True
respuesta_usuario = input("desea agregar otro producto?  y/n ")
total = 0
numero_productos = 0
descuento = 0

if respuesta_usuario == "y":
        agregar_producto = True
elif respuesta_usuario == "n":
    print("ono")
while agregar_producto == True:
    print("ingrese -1 si quiere salir")
    precio_ingresado = int(input("Ingrese el precio de su suplemento "))
    if precio_ingresado == -1:
        break
    total = total + precio_ingresado
    numero_productos += 1
if numero_productos >= 3:
    descuento = total * 0.10
    total = total - descuento

print(f"su descuento es de {descuento}")
print(f"su total a pagar es de: {total}")
print(f"su numero de productos es de: {numero_productos}")