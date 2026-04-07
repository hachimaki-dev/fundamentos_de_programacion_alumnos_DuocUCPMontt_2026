print("¡Bienvenido al calabozo de las 3 puertas")
clase = input("Elige tu clase: 1) Ladron 2) Guerrero ")
intentos = 0
while intentos < 3:
    opción = input("Elige tu opción: 1) Buscar llave 2) Ganzúa 3) Forzar: ")
    if opción == "1":
        numero = input("Ingresa un número: ")
        if int(numero) % 2 == 0:
            print("Puerta abierta")
            break
        else:            
            print("No encontraste la llave")
            intentos += 1
    if opción == "2":
        if clase == "1":
            print("Puerta abierta")
            break
        else:  
            print("No puedes")
            intentos += 1
    if opción == "3":
        if clase == "2":
            print("Puerta abierta")
        else:
            print("No puedes")
            intentos += 1
else:
    print("Perdiste el juego")
