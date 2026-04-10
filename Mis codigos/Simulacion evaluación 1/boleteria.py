total_dia = 0
subtotal = 0
cantidad_pasajes = 0
destino1 = "Puerto Varas 🌹"
destino2 = "Osorno 🐮"
destino3 = "Frutillar 🍓"
destino_elegido = ""
tipo_viaje = 0 # No tiene validacion de dato ingresado
valor_destino1 = 3000
valor_destino2 = 7000
valor_destino3 = 5000
continuar_vendiendo = False

print("--- 🚌Bienvenido a la Boletería🚌 ---")

while True:

    if continuar_vendiendo:
        print("¿Desea continuar atendiendo?")
        desea_continuar = int(input("1. Continuar | 2. Salir: "))
        if desea_continuar == 1:
            continuar_vendiendo = True
        else:
            break
    continuar_vendiendo = True # Entra en la segunda iteracion

    descuento = False
    destino_elegido = int(input(f"\nDestinos: \n1. {destino1} (${valor_destino1})\n2. {destino2} (${valor_destino2})\n3. {destino3} (${valor_destino3})\n¿Hacia donde se dirige? "))
    
    if destino_elegido == 1:
        destino_elegido = destino1
        cantidad_pasajes = int(input("¿Cuantos pasajes necesita? "))
        tipo_viaje = int(input("1. Solo Ida | 2. Ida y Vuelta: "))
        subtotal = valor_destino1 * tipo_viaje * cantidad_pasajes
    elif destino_elegido == 2:
        destino_elegido = destino2
        cantidad_pasajes = int(input("¿Cuantos pasajes necesita? "))
        tipo_viaje = int(input("1. Solo Ida | 2. Ida y Vuelta: "))
        subtotal = valor_destino2 * tipo_viaje * cantidad_pasajes
    elif destino_elegido == 3:
        destino_elegido = destino3
        cantidad_pasajes = int(input("¿Cuantos pasajes necesita? "))
        tipo_viaje = int(input("1. Solo Ida | 2. Ida y Vuelta: "))
        subtotal = valor_destino3 * tipo_viaje * cantidad_pasajes
    else:
        print("\nOpcion Invalida")
        continue

    if tipo_viaje == 1:
        tipo_viaje = "Solo Ida"
    elif tipo_viaje == 2:
        tipo_viaje = "Ida y Vuelta"

    if subtotal > 10000:
        subtotal = subtotal * 0.9
        descuento = True

    total_dia = total_dia + subtotal

    print("\n--------------------------")
    print(f"Detalle:\n-Destino: {destino_elegido}\n-Tipo de viaje: {tipo_viaje}\n-Cantidad de pasajes: {cantidad_pasajes}\n-Subtotal: {subtotal}")
    if descuento:
        print("-Descuento del 10% aplicado")
    else:
        print("-Sin descuento aplicado")
    
    print("--------------------------")

    print("\n------ Imprimiendo boletos -----")
    for i in range(cantidad_pasajes):
        print(f"🎫 Imprimiendo boleto {i+1} de {cantidad_pasajes}...")
    print("------ Boletos entregados ------\n")

print("\n------ CAJA CERRADA ------")
print(f"Total recaudado: ${total_dia}")
print("--------------------------")