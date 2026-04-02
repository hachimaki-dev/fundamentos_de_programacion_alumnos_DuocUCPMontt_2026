print("Eres un aventurero criado en un pueblo.")
input()
print("Un día aparece el temido rey demonio y decides enfrentarte a el.")
print("Ten cuidado con el tiempo, de lo contrario destruira tu pueblo.")

vida_jefe = 1000
turnos = 0

while vida_jefe > 0:
    daño_ataque = int(input("Ingrese el daño del ataque: "))
    if daño_ataque <= 0:
        print("Has fallado, vuelve a intentar")
        turnos += 1
    elif daño_ataque >= 0:
        print(f"Le has quitado {daño_ataque} puntos de vida al jefe")
        vida_jefe = vida_jefe - daño_ataque
        turnos += 1
        print(f"Ahora le quedan {vida_jefe} puntos de vida")

print("Has derrotado al jefe, ¡Felicidades!")
print(f"Te has demorado {turnos} turnos en derrotarlo.")
if turnos <= 5:
    print("Lo has hecho genial.")
    print("Todos en tu pueblo sobrevivieron")
    print("Final Feliz")

elif turnos > 5:
    print("Lo has hecho, pero por tu tardanza todas las personas del pueblo\nfallecieron..")
    print("Final.")
    