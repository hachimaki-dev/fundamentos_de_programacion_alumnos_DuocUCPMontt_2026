# Mauricio Carcamo, Gustavo Araneda, Romina Cossio
import random
# numero = random.randint(0, 1)
jugador_vida = 100
pistola_daño = 50
hacha_daño = 35
botiquin_vida = 50
zombies_vidas = 250
zombies_daño = 20
botiquines_user = 0
print("Estas en un mundo infectado de zombies,\ntienes que hacer todo lo posible para sobrevivir,\ntu vida esta en tus manos,\ncada accion tomada tiene su consecuencia. Empiezas dentro de tu casa")
print("-" * 50)
print("       Inicia el juego \n       Escoge tu camino \n")
opcion = input("1.Eleccion de pistola(Empiezas sin balas) \n2.Eleccion de la hacha(El sigilo será tu aliado) \n3.Eleccion llaves de un coche(Debes encontrar el coche) \nEligue: ")

#  RUTA PISTOLA 
if opcion == "1":
    print("\nEstas en tu casa")
    print("\nOBJETIVO:")
    print("1. Buscar balas en la alcoba")
    ruta_pistola = input("Eligue: ")
    if ruta_pistola == "1":
        print("Balas encontradas \n")
        print("Escuchas pasos en el segundo piso")
        print("Abres la puerta y se aparece un zombie")
        print("-------------Inicio del combate------------- \n")
        print(f"Vida del zombie: {zombies_vidas}")
        while jugador_vida > 0 and zombies_vidas > 0:
            print("1. Atacar")
            print("2. Huir")
            opcion1 = input("Eligue: ")
            if opcion1 == "1":
                critico = random.randint(0, 1)
                if critico == 0:
                    zombies_vidas = zombies_vidas - pistola_daño
                    if zombies_vidas < 0:
                        zombies_vidas = 0
                    print(f"Has hecho daño normal: {pistola_daño} \nLa vida actual del zombie es de: {zombies_vidas}")
                elif critico == 1:
                    zombies_vidas = zombies_vidas - pistola_daño * 2
                    if zombies_vidas < 0:
                        zombies_vidas = 0
                    print(f"Has hecho daño letal: {pistola_daño * 2} \nLa vida actual del zombie es de: {zombies_vidas}")
            elif opcion1 == "2":
                huida_perfecta = random.randint(0, 3)
                if huida_perfecta == 0 or huida_perfecta == 1 or huida_perfecta == 3:
                    jugador_vida = jugador_vida - zombies_daño
                    print(f"La huida no fue exitosa, has perdido vida. \nVida actual: {jugador_vida}")
                elif huida_perfecta == 2:
                    print("Has huido a la perfección")
                    break
    print("********Fin del combate********")
    if jugador_vida <= 0:
        print("Te han derrotado, has sido zombificado")
    elif jugador_vida > 0:
        print("Has sobrevivido un día más en el apocalipsis")

#  RUTA HACHA
elif opcion == "2":
    print("\nEstas en la bodega de tu casa, tomas el hacha y un botiquin cercano")
    botiquines_user = 1
    print("Escuchas un ruido cerca de la bodega en la que estas")
    print("Te acercas a la ventana y ves a un zombie intentando ingresar")
    print("-------------Inicio del combate------------- \n")
    print(f"Vida del zombie: {zombies_vidas}")
    while jugador_vida > 0 and zombies_vidas > 0:
        print("1. Atacar al zombie")
        print("2. Botiquin")
        opcion1 = input("Eligue: ")
        if opcion1 == "1":
                critico = random.randint(0, 1)
                if critico == 0:
                    zombies_vidas = zombies_vidas - hacha_daño
                    if zombies_vidas < 0:
                        zombies_vidas = 0
                    print(f"Has hecho daño normal: {hacha_daño} \nLa vida actual del zombie es de: {zombies_vidas}")
                elif critico == 1:
                    zombies_vidas = zombies_vidas - hacha_daño * 2
                    if zombies_vidas < 0:
                        zombies_vidas = 0
                    print(f"Has hecho daño letal: {hacha_daño * 2} \nLa vida actual del zombie es de: {zombies_vidas}")
                jugador_vida = jugador_vida - zombies_daño
                print(f"El zombie te ataco, hizo un daño de: {zombies_daño}\n Tu vida actual es de: {jugador_vida}")
        elif opcion1 == "2":
            if botiquines_user == 1:
                jugador_vida = jugador_vida + botiquin_vida
                if jugador_vida > 100:
                    jugador_vida = 100
                print(f"Has usado el botiquin y te has curado los puntos de salud faltantes, tu vida actual es: {jugador_vida}")
                botiquines_user = 0
            elif botiquines_user == 0:
                print("No te puedes curar porque no tienes botiquines")
    print("********Fin del combate********")
    if jugador_vida <= 0:
        print("Te han derrotado, has sido zombificado")
    elif jugador_vida > 0:
        print("Has sobrevivido un día más en el apocalipsis")            

#  RUTA AUTO
elif opcion == "3":
    print("Tomas las llaves y usas el botón en llavero para que el auto suene")
    print("Escuchas el auto sonar, lo que tambien atrae a muchos zombies, por lo que corres y entras al auto")    
    print(" Manejas hasta e supermercado")
    print("Durante el camino chocas a 3 zombies")
    print("Triple kill")
    print("Llegas hasta el supermercado, tienes muchas provisiones, por lo que puedes aguantar mucho tiempo \n")
    print("Escogiste la ruta fácil, felicidades, no has tenido que luchar \n")
    print("********FIN del juego********")
    print(""-" * 50")