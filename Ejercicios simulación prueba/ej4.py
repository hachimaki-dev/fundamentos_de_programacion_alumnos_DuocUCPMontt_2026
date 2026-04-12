#Variables del simulador RPG
vida_jugador = 100
mana_jugador = 20
jefe_final = 150

#ataques del jugador jeje
ataque = 20
magia = 50
curacion = 30

#empieza la batalla
print("¡¡¡¡La Guerra por el Santogrial ha iniciado!!!!\n")
print(f"*** Tu vida es de: {vida_jugador} puntos ***")
print(f"*** Tu mana es de: {mana_jugador} puntos ***\n")

print(f"••• El jefe tiene {jefe_final} puntos de vida •••\n")

print("¿Qué acción deseas realizar?\n")
print("1) Ataque = 20 puntos")
print("2) Magia = 50 puntos")
print("3) Curación = 30 puntos\n")

#lets goooooooooo
while vida_jugador > 0 and jefe_final > 0:
    accion = int(input("Ingresa la acción a realizar: "))
    if accion == 1:
        jefe_final = jefe_final - ataque
        print(f"\n¡¡Realizaste un ataque!!\nLa vida actual del jefe es de: {jefe_final} puntos\nTu maná actual es de: {mana_jugador} puntos")
        
        if jefe_final > 0:
            vida_jugador = vida_jugador - 15
            print(f"\nEl jefe te ha atacado\nTienes actualmente {vida_jugador} puntos de vida")
        else:
            print("\n¡¡El jefe ha fallado su ataque!!")
            
    elif accion == 2:
        if mana_jugador >=5:
            jefe_final = jefe_final - magia
            mana_jugador -= 5
            print(f"\n¡¡Acabas de realizado magia!!!\nLa vida actual del jefe es de: {jefe_final} puntos\nTu maná actual es de: {mana_jugador} puntos")
        else:
            print(f"\nManá insuficiente\n¡¡Has fallado!!!")
            
            if jefe_final > 0:
                vida_jugador = vida_jugador - 15
                print(f"\nEl jefe te ha atacado\n Tienes {vida_jugador} puntos de vida")
            
            else:
                print("\n¡¡El jefe ha fallado su ataque!!")
                continue
                
    elif accion == 3:
        vida_jugador = (vida_jugador + curacion)
        mana_jugador = 0
        
        if jefe_final > 0:
            vida_jugador = vida_jugador - 15
            print(f"\nEl jefe te ha atacado\n Tienes {vida_jugador} puntos de vida")
            
        else:
            print("\nEl jefe ha fallado su ataque!!")
    else:
        print("\nAcción inválida\nIntenta de nuevo")

#Resultados
if jefe_final <= 0:
    print(f"\nEl jefe tiene {jefe_final} puntos de vida.\n¡¡Felicidades!! Has ganado la guerra por el Santogrial")
else:
    print(f"\n¡¡Has perdido!!\nTienes {vida_jugador} puntos de vida")
