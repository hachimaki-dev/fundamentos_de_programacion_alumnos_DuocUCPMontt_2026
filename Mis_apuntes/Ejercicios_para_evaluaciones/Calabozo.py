ladron = 1
guerrero = 2
clase = int(input("Que clase vas a elegir? \n 1.Ladron \n 2.Guerrero. "))

for i in range (1,4):
    intentos = 0
    abierta = False
    while intentos < 3 and not abierta:
        accion = int(input("Para abrir la puerta que opcion eligiras? \n1.forzar\n2.ganzua\n3.Buscar llave. "))
        if accion == 1:
            if clase == ladron:
                print("No tienes la fuerza suficiente para abrirla.")
                intentos +=1
            elif clase == guerrero:
                print("Lograste abrir la puerta facilmente.")
                abierta = True
        elif accion ==2:
            if clase == ladron:
                print("Lograste abrir la cerradura facilmente.")
                abierta = True
            elif clase == guerrero:
                print("No sabes como usar la ganzúa, tal vez un ladrón pueda.")
                intentos +=1
        elif accion == 3:
            numero = int(input("Elige un numero : "))
            if numero % 2 == 0:
                print("Lograste encontrar la llave y abriste la puerta")
                abierta = True
            else:
                print("No pudiste encontrar la llave.")
                intentos +=1
    if not abierta:
        print("No lograste abrir la puerta, perdiste.")
        break
    
print("FIN DEL JUEGO.")