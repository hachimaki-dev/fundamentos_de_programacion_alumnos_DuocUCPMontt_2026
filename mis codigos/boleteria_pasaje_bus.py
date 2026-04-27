total_dia = 0
precio_destino_1 = 3000
precio_destino_2 = 5000
precio_destino_3 = 7000

print("---- BIENVENIDO A LA BOLETERIA ----")

#FLAGS POR ESTUDIAR

continuar_vendiendo = False


while True:

    if continuar_vendiendo:
        desea_continuar = int((input("1. continuar 2. finalizar:")))
        if continuar_vendiendo == 1:
            continuar_vendiendo = True
            

    print("--- INGRESE SU DESTINO ---")
    print(f"1. Puerto Varas - ${precio_destino_1}")
    print(f"2. Frutillar - ${precio_destino_2}")
    print(f"3. Osorno - ${precio_destino_3}")

    destino = input("ingrese el numero del destino elegido (1/2/3):")

    if destino == "1":

        print("pasaje a puerto varas registrado")
        print("1. ida")
        print("2. ida y vuelta")

        tipo_viaje = int(input("ingrese su tipo de viaje (1/2):"))

        if tipo_viaje == 1:
            total_dia += precio_destino_1
        elif tipo_viaje == 2:
            total_dia += precio_destino_1 * 2
        break

    elif destino == "2":

        
        print("pasaje a frutillar registrado")
        print("1. ida")
        print("2. ida y vuelta")

        tipo_viaje = int(input("ingrese su tipo de viaje (1/2):"))

        if tipo_viaje == 1:
            total_dia += precio_destino_2
        elif tipo_viaje == 2:
            total_dia += precio_destino_2 * 2

    elif destino == "3":    
        
        print("pasaje a osorno registrado")
        print("1. ida")
        print("2. ida y vuelta")

        tipo_viaje = int(input("ingrese su tipo de viaje (1/2):"))

        if tipo_viaje == 1:
            total_dia += precio_destino_3
        elif tipo_viaje == 2:
            total_dia += precio_destino_3 * 2
        break

    else:
        print("opcion invalida, intente de nuevo")
        continue

