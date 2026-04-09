PRECIO_PUERTO_VARAS = 3000
PRECIO_OSORNO = 7000
PRECIO_FRUTLLAR = 5000

MONTO_PARA_DESCUENTO = 10000


monto_a_pagar_total = 0

precio_destino = 0


print("--- Bienvenido a la Boletería ---")
print("--- Por una compra mayor a $10.000, tendrá un descuento de 10%. ---")

while True :
    monto_a_pagar_cliente = 0
    
    while True :
        print("Aquí tiene sus destinos:")
        print(f"1) Puerto Varas - ${PRECIO_PUERTO_VARAS}")
        print(f"2) Osorno       - ${PRECIO_OSORNO}")
        print(f"3) Frutillar    - ${PRECIO_FRUTLLAR}")

        opcion = int (input(""))
        
        nombre_destino = ""

        match opcion :
            case 1 :
                precio_destino = 3000
                nombre_destino = "Puerto Varas"
                break
            case 2 : 
                precio_destino = 7000
                nombre_destino = "Osorno"
                break
            case 3 :
                precio_destino = 5000
                nombre_destino = "Frutillar"
                break
            case _ :
                print("Opción inválida.")

    cantidad_pasajes = int (input(f"¿Cuántos pasajes quiere comprar hacia {nombre_destino}? "))

    while True :
        cantidad_pasajes_ida_y_vuelta = int (input(f"De los {cantidad_pasajes} pasajes, ¿cuántos quiere que de ida y vuelta? (Un pasaje de ida y vuelta sale el doble). "))

        if cantidad_pasajes_ida_y_vuelta > cantidad_pasajes or cantidad_pasajes_ida_y_vuelta < 0:
            print(f"Error. Por favor, ingrese un valor entre 0 y {cantidad_pasajes}.")
        else :
            break

    cantidad_pasajes_solo_de_ida = cantidad_pasajes - cantidad_pasajes_ida_y_vuelta

    monto_pasajes_solo_de_ida = precio_destino * cantidad_pasajes_solo_de_ida
    monto_pasajes_ida_y_vuelta = precio_destino * cantidad_pasajes_ida_y_vuelta * 2
    monto_pasajes_total = monto_pasajes_solo_de_ida + monto_pasajes_ida_y_vuelta 

    if monto_pasajes_total > MONTO_PARA_DESCUENTO :
        print("¡¡¡ DESCUENTO DEL 10% APLICADO !!!")
        monto_pasajes_total = int (monto_pasajes_total * 0.9)
    else :
        print("Sin descuento aplicado.")

    monto_a_pagar_cliente += monto_pasajes_total
    monto_a_pagar_total += monto_a_pagar_cliente

    for i in range(cantidad_pasajes_solo_de_ida):
        print(f"🎫 Imprimiendo boleto sólo de ida: {i+1} de {cantidad_pasajes_solo_de_ida}... ${precio_destino}")

    for i in range(cantidad_pasajes_ida_y_vuelta):
        print(f"🎫 Imprimiendo boleto de ida y vuelta: {i+1} de {cantidad_pasajes_ida_y_vuelta}... ${precio_destino * 2}")



    print(f"El precio total a pagar es ${monto_a_pagar_cliente}.")
    nueva_compra = int (input("¿Quiere hacer otra compra? "))

    print("1) Sí.")
    print("2) No.")

    if nueva_compra == 2 :
        break

print(f"Monto total del día: ${monto_a_pagar_total}.")





    
