vida_boss = 1000 
vida_playerBenja = 500 

while vida_boss > 0 and vida_playerBenja > 0: 
    print("Vida del Boss:", vida_boss) 
    print("Vida de Benja:", vida_playerBenja) 
    print("1. Atacar con espada") 
    print("2. Atacar con magia") 
    print("3. Defenderse") 
    opcion = input("Elige tu acción: ")
    print ("Fin DEL JUEGO!!!")
    print ("YOU WIN!!!")
  

    if opcion == "1": 
        daño = 50 
        vida_boss -= daño 
        print("Has atacado con espada y causado", daño, "de daño al Boss.") 
    elif opcion == "2": 
        daño = 80 
        vida_boss -= daño 
        print("Has atacado con magia y causado", daño, "de daño al Boss.") 
    elif opcion == "3": 
        print("Te has defendido, reduciendo el daño del próximo ataque del Boss.") 
    else: 
        print("ataque fallido.") 

    # Simulación del ataque del Boss
    daño_boss = 30 
    if opcion == "3": 
        daño_boss //= 2  # Reducir el daño si el jugador se defendió
    vida_playerBenja -= daño_boss 
    print("El Boss ha atacado y causado", daño_boss, "de daño a Benja.")      