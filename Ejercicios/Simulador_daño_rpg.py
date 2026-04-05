vida_jefe = 1000

print("--- ¡COMIENZA LA BATALLA! ---")
print(f"El jefe tiene {vida_jefe} HP.")

while vida_jefe > 0:
    
    try:
        daño = int(input("\nIngresa el daño de tu ataque: "))
        if daño < 0:
            print("El ataque falló. No restaste vida.")
        else:
            vida_jefe = vida_jefe - daño

        if vida_jefe < 0:
            vida_jefe = 0
        print(f"¡Golpe directo! Vida restante del jefe: {vida_jefe}")

    except ValueError:
        print("Por favor, ingresa un número entero válido.")
        print("\n¡Jefe derrotado! Has ganado la batalla.")

