print("Simulador de daño RPG!!!")
print("INTENTA MATAR AL JEFE FINAL...")
print("MUZAN KIBUTSUJI")
Jefe_final_puntos_de_vida = 1000
Ataque_al_jefe = 0
while Jefe_final_puntos_de_vida > 0 :
    Ataque_al_jefe = int(input("Ingresa el daño del ataque en numero entero: "))
    if Ataque_al_jefe < 0 :
        print("UPS!! El ataque ha fallado")
    elif Ataque_al_jefe >= 0 :
        Jefe_final_puntos_de_vida = Jefe_final_puntos_de_vida - Ataque_al_jefe
        print(f"La vidal del jefe es: {Jefe_final_puntos_de_vida}")
if Jefe_final_puntos_de_vida <=0 :
    print("DERROTASTE A MUZAN KIBUTSUJI!!!!FELICIDADESSSSS")





#1. El jefe final tiene 1000 puntos de vida iniciales.
#2. Usa un ciclo while que se repita mientras la vida del jefe sea mayor que 0.
#3. Dentro del ciclo, pide al usuario ingresar el daño del ataque (entero).
#4. Si el daño es menor a 0, muestra un mensaje "El ataque falló" y no restes vida.
#5. Si el daño es mayor o igual a 0, réstalo de la vida del jefe y muestra la vida restante.
#6. Si la vida es 0 o menos, rompe el ciclo o deja que termine naturalmente, y muestra "¡Jefe derrotado!".