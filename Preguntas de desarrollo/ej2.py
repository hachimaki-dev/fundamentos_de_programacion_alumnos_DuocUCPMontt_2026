bandera = True
producto = 0
productos_a_llevar = 0
total = 0
import sys

print("Bienvenido a la tienda de suplementos de Python, para su suerte si lleva 3 productos o más te llevaras un majestuoso 10% de descuento")

productos_a_llevar = int(input("¿Cuantos suplementos quiere llevar?"))

while bandera:
    producto = producto + 1
    valor = int(input(f"¿Cual sería el precio de su producto {producto}?"))
    if valor > 0:
        total = total + valor
    elif valor < 0:
        respuesta1 = input(f"¿Estas seguro de que {valor} es el precio (responder con SI o NO)?")
        if respuesta1 == "NO":
            print("Perfecto, entonces le vuelvo a preguntar")
            producto = producto - 1
        if respuesta1 == "SI":
            print("Hmmm, vale?")
    if productos_a_llevar == producto:
        break
if productos_a_llevar >= 3:
    print("Felicidades, haz obtenido un 10% de descuento")
    print(f"Su total sera de {total * 0.9}")
    print(f"Precio origina: {total}, descuento de {total * 0.1}")
    sys.exit ()
if productos_a_llevar < 3:
    print(f"Su total sería de {total}")
    print("Lastimosamnete no ha obtenido descuento")