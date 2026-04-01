print("------------------------------------------")
print("🌸 ¡BIENVENIDOS AL RESTAURANTE KATSUDON! 🌸")
print("------------------------------------------")
print("MENÚ: Katsudon, Ramen, Sushi, Bolillos, ")
print("Dorayakis, Onigiri, Té Matcha, Ramune, ")
print("Llavero Anime, Figura Sorpresa")
print("------------------------------------------")

cuantos = input("¿Cuántos artículos desea pedir?: ")
cuantos = int(cuantos)

contador = 0
subtotal = 0 

while contador < cuantos:
    pedido = input("¿Qué desea ordenar?: ")
    pedido = pedido.lower() 
    
    if "katsudon" in pedido:
        precio = 8500
    elif "ramen" in pedido:
        precio = 7000
    elif "sushi" in pedido:
        precio = 6000
    elif "bolillo" in pedido:
        precio = 1000
    elif "dorayaki" in pedido:
        precio = 2500
    elif "onigiri" in pedido:
        precio = 3000
    elif "matcha" in pedido:
        precio = 2000
    elif "ramune" in pedido:
        precio = 3500
    elif "llavero" in pedido:
        precio = 4000
    elif "figura" in pedido:
        precio = 12000
    else:
        print("No encontré ese artículo, le pondremos un precio base de $2000")
        precio = 2000

    subtotal = subtotal + precio
    
    contador = contador + 1
    print("¡Agregado! Subtotal actual: $" + str(subtotal))

print("\n--- TICKET DE VENTA KATSUDON ---")

if subtotal > 15000:
    descuento = subtotal * 0.10
    total = subtotal - descuento
    print("Subtotal: $" + str(subtotal) + ", Descuento: $" + str(descuento) + ", Total pagar: $" + str(total))
else:
    envio = 2000
    total = subtotal + envio
    print("Subtotal: $" + str(subtotal) + ", Envío: $2000, Total a pagar: $" + str(total))

print("------------------------------------------")
print("¡Gracias por su visita! ¡Arigato! 🌸")