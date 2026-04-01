boss_life = 1000
while boss_life > 0: 
    damage = int(input("Ingrese el daño del ataque: "))
    if damage < 0:
        print("El ataque falló")
        continue
    elif damage >= 0:
        boss_life -= damage
        print(f"Vida restante del jefe: {boss_life}")
    elif boss_life <= 0:
        print("¡Jefe derrotado!")
    else:
        print("Algo inesperado ocurrió")
print("Fin de juego")