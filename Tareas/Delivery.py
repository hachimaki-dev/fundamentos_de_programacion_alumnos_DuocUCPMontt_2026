bandera = True
subtotal = 0
descuento = 0
envio = 0
contador = 0
print("Bienvenido al Delivery de PYTHON")
print("Tenemos hamburguesas, pizza, sushi y completos.")
print("Por una compra superior a $14.999 obtendras un 10% de descuento ")

cantidad_a_comprar = int(input("¿Cuantos alimentos deseas comprar?"))

while bandera:
    contador = contador + 1
    print("1. Hamburguesa 2000 CLP")
    print("2. Pizza 4500 CLP")
    print("3. Sushi 5000 CLP")
    print("4. Completo 30000 CLP")
    articulo_a_comprar = int(input(f"¿Que quieres comprar? (articulo {contador}) (Selecciona con el numero a la izquierda del alimento)"))
    if articulo_a_comprar == 1:
        respuesta = input("¿Estas seguro de tu elección? RESPONDER CON 'SI' o 'NO'")
        if respuesta == "SI":
            subtotal = subtotal + 3000
            print(f"Perfecto, se le sumado $3000CLP a su cuenta, tiene un total de ${subtotal}CLP en el carrito")
        if respuesta == "NO":
            contador = contador - 1
            print("Perfecto, se ha eliminado su elecciòn")
    if articulo_a_comprar == 2:
        respuesta = input("¿Estas seguro de tu elección? RESPONDER CON 'SI' o 'NO'")
        if respuesta == "SI":
            subtotal = subtotal + 4500
            print(f"Perfecto, se le sumado $4500CLP a su cuenta, tiene un total de ${subtotal}CLP en el carrito")
        if respuesta == "NO":
            contador = contador - 1
            print("Perfecto, se ha eliminado su elecciòn")
    if articulo_a_comprar == 3:
        respuesta = input("¿Estas seguro de tu elección? RESPONDER CON 'SI' o 'NO'")
        if respuesta == "SI":
            subtotal = subtotal + 5000
            print(f"Perfecto, se le sumado $5000CLP a su cuenta, tiene un total de ${subtotal}CLP en el carrito")
        if respuesta == "NO":
            contador = contador - 1
            print("Perfecto, se ha eliminado su elecciòn")
    if articulo_a_comprar == 4:
        respuesta = input("¿Estas seguro de tu elección? RESPONDER CON 'SI' o 'NO'")
        if respuesta == "SI":
            subtotal = subtotal + 3000
            print(f"Perfecto, se le sumado $3000CLP a su cuenta, tiene un total de ${subtotal}CLP en el carrito")
        if respuesta == "NO":
            contador = contador - 1
            print("Perfecto, se ha eliminado su elecciòn")
    if cantidad_a_comprar == contador:
        bandera = False
if subtotal > 15000:
    print(f"Perfecto has obtenido un 10% de descuento, su total a pagar es de ${subtotal * 0.9}CLP ")
    print(f"El descuento aplicado es de {subtotal * 0.1}")
    print(f"El precio sin descuento es de {subtotal}")
    print("Espero que tenga una buena tarde")
if subtotal < 15000:
    print("Lastimosamente no has obtenido el descuento")
    print(f"El precio de los productos es de ${subtotal}CLP y se le aplicara una tarifa de $2000CLP de envio")
    print(f"El total a pagar es de ${subtotal + 2000}CLP. ")
    print("Espero que tenga una buena tarde")