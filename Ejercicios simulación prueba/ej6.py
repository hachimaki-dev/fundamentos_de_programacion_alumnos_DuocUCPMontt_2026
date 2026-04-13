#inicio
ganar = True
#BIENVENIDA
print("Bienvenido aventurero al Calabozo de las 3 puertas")

#ESCOGE TU CLASE
print("Aventurero escoge tu clase: ")
print("\n1) Ladrón\nObtienes la habilidad < Ganzúa >")
print("\n2) Guerrero\nObtienes la habilidad < Forzar >")

while True:
    clase = input("\nIngresa tu clase (selecciona 1 ó 2): ")
    
    if clase == "1":
        print(f"\nEscogiste: {clase}")
        print("Habilidad Ganzúa aprendida")
        break
    elif clase == "2":
        print(f"\nEscogiste: {clase}")
        print("Habilidad Forzar aprendida")
        break
    else:
        print("ingresa una clase válida")

#INICIA LA AVENTURA
print("\nEmpieza tu aventura por el calabozo")

#NUMEROS DE HABITACIÓN
for i in range (1, 4):
    print(f"\n---Te encuentras en la habitación {i}---")
    abierto = False
    intentos = 0
    
    while intentos < 3 and not abierto:
        intentos += 1
        print(f"\nIntento {intentos}/3")
        accion = input("\n¿Qué acción deseas realizar?\n- Buscar llave\n- Ganzúa\n- Forzar\nEscribe tu acción: ").strip().lower()
        
        if accion == "buscar llave":
            llave = int(input("\nIngresa un número para buscar la llave: "))
            if llave % 2 == 0:
                print(f"\nHas encontrado la llave\nPuerta de la habitación {i} abierta")
                abierto = True
            else:
                print("\nNo has obetnido suerte\nIntenta de nuevo o realiza otra acción")
            
        elif accion == "ganzúa" or accion == "ganzua":
            if clase == "1":
                print(f"\nHas abierto la puerta {i}\nTus habilidades de ladrón son impecables")
                abierto = True
            else:
                print("Hanilidad no aprendida\n intenta otra acción")
                
        elif accion == "forzar":
            if clase == "2":
                print(f"\nHas abierto la puerta {i}\n¡Qué guerrero tan fuerte!")
                abierto = True
            else:
                print("\nNo tienes la suficiente fuerza")
        
        else:
            print("\nAcción no valida\n Pierdes un intento")
    #PERDISTE
    if not abierto:
        print("---PERDISTE---\nEl amo del calabozo ha capturado tu alma")
        ganar = False
        break
#GANASTE
if ganar:
    print("\n==========================================")
    print("¡FELICIDADES! Has atravesado el calabozo.")
    print("==========================================")
