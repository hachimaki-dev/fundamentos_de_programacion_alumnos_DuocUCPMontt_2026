print("############ BIENBEVIDOS AL JUEGO DE VENCER AL JEFE FINAL #############")
print("El jefe final tiene 1000 puntos de vida iniciales , Mucha suerte en derrotar el jefe jugador")

vida_del_jefe = 1000

while vida_del_jefe > 0 :
    daño_al_jefe = int(input("Ingrese cuanto daño hace su ataque"))

    if daño_al_jefe < 0 :
        print("El ataque falló")
    elif daño_al_jefe >= 0 :
        vida_del_jefe = vida_del_jefe - daño_al_jefe
        print(f"la vida restante del jefe es {vida_del_jefe} ")
    elif vida_del_jefe <= 0 :
        break
    

print("Felicitaciones Derrotaste al Jefe Final")