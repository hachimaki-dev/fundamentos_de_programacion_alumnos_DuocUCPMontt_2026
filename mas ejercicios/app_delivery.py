#1. Pregunta al usuario cuántos platos desea pedir (cantidad).
#2. Usa un ciclo while y un contador para pedir el precio de CADA plato.
#3. Usa un ACUMULADOR para ir sumando todos los precios en un "subtotal".
#4. Una vez terminado el ciclo, evalúa el subtotal con un if:
#- Si el subtotal es mayor a $15.000, aplica un 10% de descuento y muestra el
 #detalle: "Subtotal: $X, Descuento: $Y, Total pagar: $Z".

#- Si no supera los $15.000, cobra un costo de envío fijo de $2.000 y muestra:
# "Subtotal: $X, Envío: $2000, Total a pagar: $Z".

comida = int(input("cuantos platos desea pedir ? :")) 
contador = 0
subtotal = 0
precio_total = 0 
descuento = 0
while contador != comida:
    precio = int(input(f"cual es el valor del plato n {contador + 1}: "))
    contador +=1
    subtotal += precio
    contador > comida

if subtotal > 15000:
    descuento = subtotal * 0.10 
    print(f"subtotal : {subtotal} , descuento: {descuento} , total pagar: {subtotal - descuento}")

elif subtotal < 15000:
    envio = 2000
    print(F"envio : {envio}, subtotal: {subtotal}, total pagar: {subtotal + envio}")    
