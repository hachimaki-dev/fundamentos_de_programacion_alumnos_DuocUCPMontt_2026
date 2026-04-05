print("bienvenido")
print("que desea ordenar (escribe igual)")
print("menu:")
print("hamburguesa -> 7,000clp")
print("completo -> 5,000clp")
print("papas -> 4,000clp")
platos = int(input("cuantos platos desea pedir"))
plato = 0
subtotal = 0 
hamburguesa = 7000 
completo = 5000
papas = 4000
envio = 2000
descuento = 10
while platos != plato :
    
    orden = input("que va a ordenar")
    if orden == "hamburguesa" :
        print("ordenaste la hamburguesa de 7,000clp")
        subtotal = subtotal + hamburguesa
        plato = plato + 1
    elif orden == "completo" :
        print("ordenaste el completo de 5,000clp")
        subtotal = subtotal + completo
        plato = plato + 1
    elif orden == "papas" :
        print("ordenaste las papas de 4,000clp")
        subtotal = subtotal + papas
        plato = plato + 1 
    else:
        print("seleccione una opcion valida")
print(f"el total de la orden es {subtotal}")

if subtotal > 15000 :
    print("debido a que el subtotal de la orden supera los 15,000clp se aplica un 10 porciento de descuento")
    total = subtotal/100*descuento
    subtotal = subtotal - total
    print(f"luego de descuentos el valor final es {subtotal}")




elif subtotal < 15000 :
    print(f"el subtotal de su orden es {subtotal} mas el costo de envio de 2,000clp")
    subtotal = subtotal + envio
    print(f"el precio final es {subtotal}")
