print("---Bienvenido al juego de Atack on Titan---")
print("Crees poder salvar a la humanidad?....")
Titanes = ["Titan Acorazado", "Titan Colosal", "Titan Bestia"]
Legion = ["levi", "eren", "mikasa"]
Vida = 100
ganaste = True
print("Podras luchar contra los siguientes titanes: ")
for t in Titanes:
    print("El " + t)
print("Estos son los personajes que podras ocupar: ")
for p in Legion:
    print("-" + p)
jugador = input("Escoge un personaje: ").lower()
if jugador in Legion:
    print(jugador + " entra en BATALLA!!")
    print("Entras con 100HP!!!")
else:
    print("Personaje invalido")
    print("Entraras como soldado")
    jugador = "soldado"
while len(Titanes) > 0:
    titan = Titanes.pop(0)
    print("Te enfrentas al " + titan)
    accion = input("¿Prefieres atacar, huir o curar?: ").lower()
    if accion == "atacar":
            print(f"Estas con {jugador}, puedes atacar (nuca / tobillos / ojos): ")
            ataques = input("Ingresa hacia donde quieres atacar: ").lower()
            if ataques == "nuca":
                print("Atacaras con Misil o Cuchillas: ")
                equipo = input("Elige el equipo de maniobra que utilizaras: ").lower()
                if equipo == "misil":
                    print(f"Le disparaste misiles a la nuca al {titan} por lo cual...")
                    print("!GANASTE!")
                    print("Apesar de haber atacado " + ataques + " y usar " + equipo + f" el {titan} te quito 30 de vida!!")
                    Vida = Vida - 30
                    print("Derrotaste al: " + titan, "Tu vida es de " + str(Vida))
                elif equipo == "cuchillas":
                    print("Le cortaste la nuca a puras cuchillas...por lo cual...")
                    print("!GANASTE! pero tardaste mas tiempo")
                    print("Apesar de haber atacado " + ataques + " y usar " + equipo + f" el {titan} te quito 30 de vida!!")
                    Vida = Vida - 30
                    print("Derrotaste al: " + titan, "Tu vida es de " + str(Vida))      
            elif ataques == "tobillos":
                print("Atacaras con Misil o Cuchillas: ")
                equipo = input("Elige el equipo de maniobra que utilizaras: ").lower()
                if equipo == "misil":
                    print(f"Le disparaste misiles a los Tobillos al {titan} por lo cual...")
                    print("!GANASTE!")
                    print("Apesar de haber atacado " + ataques + " y usar " + equipo + f" el {titan} te quito 30 de vida!!")
                    Vida = Vida - 30
                    print("Derrotaste al: " + titan, "Tu vida es de " + str(Vida))
                elif equipo == "cuchillas":
                    print("Le cortaste los Tobillos a puras cuchillas por lo cual...")
                    print("!GANASTE! Se cayo y dejo la Nuca descubierta")
                    print("Apesar de haber atacado " + ataques + " y usar " + equipo + f" el {titan} te quito 30 de vida!!")
                    Vida = Vida - 30
                    print("Derrotaste al: " + titan, "Tu vida es de " + str(Vida))
            elif ataques == "ojos":
                print("Atacaras con Misil o Cuchillas: ")
                equipo = input("Elige el equipo de maniobra que utilizaras: ").lower()
                if equipo == "misil":
                    print(f"Le disparaste misiles a los Ojos al {titan} por lo cual lo dejaste ciego....")
                    print("!GANASTE! No pudo ver que fuiste hacia su Nuca y lo mataste")
                    print("Apesar de haber atacado " + ataques + " y usar " + equipo + f" el {titan} te quito 30 de vida!!")
                    Vida = Vida - 30
                    print("Derrotaste al: " + titan, "Tu vida es de " + str(Vida))
                elif equipo == "cuchillas":
                    print("Le cortaste los Ojos a puras cuchillas...por lo cual quedo ciego....")
                    print("!GANASTE! No pudo ver que fuiste hacia su Nuca y lo mataste ")
                    print("Apesar de haber atacado " + ataques + " y usar " + equipo + f" el {titan} te quito 30 de vida!!")
                    Vida = Vida - 30
                    print("Derrotaste al: " + titan, "Tu vida es de " + str(Vida))
            else:
                print("Ataque invalido, el titan te golpea! Haciendote 30 de daño")
                Vida -= 30
                print(f"Tu vida es de" + Vida)
    elif accion == "huir":
        if titan == "Titan Acorazado":
            print("Escapaste del " + titan)
            print("Pero no creas que todo termina aqui...Te sigue...Te alcanza...")
            print("!MUERES! Te agarro y despedazo comiendote de un bocado")
            ganaste = False
            break
        elif titan == "Titan Colosal":
            print("Escapaste del " + titan)
            print("Pudiste escapar!! Ya que el Titan Colosal es muy lento...felicidades...por ahora")
            continue
        elif titan == "Titan Bestia":
            print("Escapaste del " + titan)
            print("Pero no creas que todo termina aqui...Te sigue...Te lanza piedras, caes y pierdes tu equipo de maniobras")
            print("Te dice que solo un tonto pierde el equipo de maniobras y te come pedazo x pedazo riendose....")
            ganaste = False
            break        
    elif accion == "curar":
        Vida = Vida + 20
        print("Te curaste! Ahora tienes " + str(Vida) + " de HP.")
        Titanes.insert(0, titan)
    else:
        print("No hiciste nada, miedoso...")
        print("el Titan sigue vivo")
        Titanes.insert(0, titan)
    if Vida <= 0:
        print("Moriste....FIN DEL JUEGO!!")
        ganaste = False
        break
if ganaste == True:
    print("Felicidades derrotaste a todos los titanes que fuerteee")
else:
    print("Perdiste la batalla.......")