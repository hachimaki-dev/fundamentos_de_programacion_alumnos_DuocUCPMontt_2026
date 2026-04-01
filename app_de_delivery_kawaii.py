# Calcular el total a pagar de un pedido de comida, con descuentos.
import os

compra_en_progreso = True
monto_total = 0
carrito = []

os.system('clear')
print("Bienvenido a Delivery Kawaii! ( ˶ˆᗜˆ˵ ) \n")

while compra_en_progreso == True:
    print(f"Su total de compra es: [{monto_total}]")
    print("Ingrese un articulo para progresar! (1-6)")
    print("1. Udon de Kitsune $2500")
    print("2. Sopa de Miso $2000")
    print("3. Karaage $3000")
    print("4. Gyozas de Cerdo $3000")
    print("5. Sashimi de Salmon $4000")
    print("- - - - - - - - - - - - - - -")
    print("6. Continuar a pago")
    seleccion = int(input("[]: "))
    try:
        if seleccion == 1:
            carrito.append("Udon de Kitsune")
            monto_total += 2500
            os.system('clear')
        if seleccion == 2:
            carrito.append("Sopa de Miso")
            monto_total += 2000
            os.system('clear')
        if seleccion == 3:
            carrito.append("Karaage")
            monto_total += 3000
            os.system('clear')
        if seleccion == 4:
            carrito.append("Gyozas de Cerdo")
            monto_total += 3000
            os.system('clear')
        if seleccion == 5:
            carrito.append("Sashimi de Salmon")
            monto_total += 4000
            os.system('clear')
        if seleccion == 6:
            compra_en_progreso = False
    except:
        print("Valor invalido!")

os.system('clear')
print(f"Articulos totales: {len(carrito)}")
if monto_total >= 15000:
    print("Descuento aplicado! No se cobrara Envio")
    print(f"Costo de envio: {monto_total}")
    print("Gracias por su compra!")
else:
    print(f"Coste de Envio: {monto_total + 2000} (Envio incluido: $2000)")
    print("Gracias por su compra!")
