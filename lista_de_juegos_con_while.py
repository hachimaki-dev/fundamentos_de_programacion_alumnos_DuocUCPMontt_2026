# Never do this btw

juego1 = "CS 1.6"
juego2 = "Team Fortress 2"
juego3 = "Portal"
juego4 = "Portal 2"
juego5 = "Left 4 Dead 2"
juego6 = "Factorio"
juego7 = "Kerbal Space Program"
juego8 = "Terraria"

libreria_de_juegos = ["CS 1.6", "Team Fortress 2", "Portal", "Portal 2", "Left 4 Dead 2", "Factorio", "Kerbal Space Program", "Terraria"]

contador = 0
juego = ""

while contador < len(libreria_de_juegos):
    juego_n = "juego" + str(contador + 1)
    if juego_n == "juego1":
        print(juego1)
        contador +=1
    if juego_n == "juego2":
        print(juego2)
        contador +=1
    if juego_n == "juego3":
        print(juego3)
        contador +=1
    if juego_n == "juego4":
        print(juego4)
        contador +=1
    if juego_n == "juego5":
        print(juego5)
        contador +=1
    if juego_n == "juego6":
        print(juego6)
        contador +=1
    if juego_n == "juego7":
        print(juego7)
        contador +=1
    if juego_n == "juego8":
        print(juego8)
        contador +=1

print("\n V V V Ahora utilizando una lista V V V \n")

contador = 0
while contador < len(libreria_de_juegos):
    print(libreria_de_juegos[contador])
    contador +=1