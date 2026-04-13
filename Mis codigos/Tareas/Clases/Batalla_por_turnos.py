
vida_j1 = 1000
vida_j2 = 1000

nombre_j1 = input("Ingrese nombre jugador 1")
nombre_j2 = input("Ingrese nombre jugador 2")

bomba = 100
granada = 300
c4 = 500

rondas = 0

ataque = input(f"{nombre_j1} comienza la partida")
if ataque == "1":
    vida_j2 = vida_j2 - bomba
    rondas += 1
    print(f"A {nombre_j2} le quedan {vida_j2}")
elif ataque == "2":
    vida_j2 = vida_j2 - granada
    rondas += 1
    print(f"A {nombre_j2} le quedan {vida_j2}")
elif ataque == "3":
    vida_j2 = vida_j2 - c4
    rondas += 1
    print(f"A {nombre_j2} le quedan {vida_j2}")

while True:

    
    if rondas == 0:
        ataque = input(f"Es el turno de {nombre_j1} ")
        if ataque == "1":
            vida_j2 = vida_j2 - bomba
            rondas += 1
            print(f"A {nombre_j2} le quedan {vida_j2}")
        elif ataque == "2":
            vida_j2 = vida_j2 - granada
            rondas += 1
            print(f"A {nombre_j2} le quedan {vida_j2}")
        elif ataque == "3":
            vida_j2 = vida_j2 - c4
            rondas += 1
            print(f"A {nombre_j2} le quedan {vida_j2}")
    
    if rondas == 1:
        ataque = input(f"Es el turno de {nombre_j2} ")
        if ataque == "1":
            vida_j1 = vida_j1 - bomba
            rondas -= 1
            print(f"A {nombre_j1} le quedan {vida_j1}")
        elif ataque == "2":
            vida_j1 = vida_j1 - granada
            rondas -= 1
            print(f"A {nombre_j1} le quedan {vida_j1}")
        elif ataque == "3":
            vida_j1 = vida_j1 - c4
            rondas -= 1
            print(f"A {nombre_j1} le quedan {vida_j1}")
    
    if vida_j1 <= 0 or vida_j2 <= 0:
        if vida_j1 > vida_j2:
            print(f"Ganador: {nombre_j1}")
            break
        elif vida_j2 > vida_j1:
            print(f"Ganador: {nombre_j2}")
            break

    





