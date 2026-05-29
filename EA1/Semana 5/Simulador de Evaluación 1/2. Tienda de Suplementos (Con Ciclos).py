# 2. Tienda de Suplementos (Con Ciclos)
# Una tienda vende potes de proteína. El usuario puede agregar potes hasta que decida finalizar.

# Requerimientos:
# 1. Utiliza un ciclo (while) para preguntar repetidamente al usuario el precio de un suplemento a agregar al carrito. Si ingresa "0" u otro número de salida que definas, el ciclo debe terminar.
# 2. Lleva la cuenta del total a pagar y de la cantidad de productos ingresados.
# 3. Si el usuario compró 3 o más productos en total, aplícale un descuento del 10% al total al finalizar.
# 4. Imprime el total final a pagar y la cantidad de productos comprados.

contador = 0
suma_total = 0

print("****Tienda de Suplementos****")
while True:
    monto_carrito = int(input("¿Cual es el precio del del suplemnto a agreagar al carrito? 0. Salir: "))
    suma_total += monto_carrito
    contador += 1

    if monto_carrito == 0:
        break
if contador >= 3:
    descuento_10 = suma_total * 0.1
    suma_total = suma_total - descuento_10

contador -= 1

print(f"Total final a pagar es: ${suma_total} y la cantidad de productos comprados es {contador}")