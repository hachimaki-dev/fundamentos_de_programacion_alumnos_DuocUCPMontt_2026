hierbas = 0
frasco = 0
oro = 500
pocion = 0

while True:
    print("BIENVENIDO AL TALLER DE ALQUIMIA")
    print(f"Posees: {oro} de ORO, {hierbas} de HIERBAS, {frasco} Frascos y {pocion} POCIONES DE FUEGO creadas.")
    print("LISTA DE PRECIOS \n1) Hierba = $50\n2) Frascos = $100 \n3) Poción de fuego = 2 Hierbas y 1 Frasco")
    
    eleccion_jugador = int(input("Eliga una opción: "))
    
    if eleccion_jugador == 1:
        if oro >= 50:
            oro -= 50
            hierbas += 1
            print("Compraste una hierba")
            
    
        else:
            print("No tienes suficiente oro.")
        
    elif eleccion_jugador == 2:
        if oro >= 100:
            oro -= 100
            frasco += 1
            print("Compraste 1 frasco")
            
        else:
            print("No tienes suficiente oro.")
            
    elif eleccion_jugador == 3:
        if hierbas >= 2 and frasco >= 1:
            hierbas -= 2
            frasco -= 1
            pocion += 1
            print("HAZ CREADO LA MAGNFICA POCION DE FUEGO, FELICIDADES!!!!")
            
            break
            
    else:
        print("Te faltan materiales.")

