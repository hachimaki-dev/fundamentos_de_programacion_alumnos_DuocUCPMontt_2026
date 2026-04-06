vida_personaje = 300
vida_monstruo = 1000
print("te perdiste en el bosque, sientes que una vil presencia te esta asechando desde hace un largo rato, vas a revisar el origen del ruido que te lleva acosando. Cuando decides acercarte la bestia se avalanza sobre ti, con un habilidoso movimiento logras esquivarla, ahora solo queda luchar")
while vida_monstruo > 0 and vida_personaje > 0:
    print(f"==tu vida {vida_personaje}==")
    print(f"==vida del jefe {vida_monstruo}==")
    print("===Combate===")
    print("1-Atacar con la espada")
    print("2-Usar magia de fuego")
    print("3-Usar magia de hielo")
    print("4-Usar magia de electricidad")
    print("5-Usar magia de tierra")
    print("6-Usar magia de viento")
    print("7-Curarte")
    print("8-Huir")
    opcion = int(input("Elije: "))    
    if opcion == 1:
        print("Atacas al monstruo con un tajo directo al pecho, pero la bestia te ataca con sus feroces garras")
        vida_monstruo = vida_monstruo - 25
        vida_personaje = vida_personaje - 50
    elif opcion == 2:
        print("Acatas a la bestia con una bola de fuego en la boca, el monstruo te ataca con la cola")
        vida_monstruo = vida_monstruo - 50
        vida_personaje = vida_personaje - 25
    elif opcion == 3:
        print("lanzas agua a presion a la bestia en el pecho, pero tu enemigo te lanza una piedra impactandote levemente")
        vida_monstruo = vida_monstruo - 40
        vida_personaje -= 20
    elif opcion ==4:
        print("te fuerzas a lanzar punzantes lanzas de hielo al pecho de la bestia, el monstruo aturdido lanza un golpe flojo a ti")
        vida_monstruo = vida_monstruo - 75
        vida_personaje -= 10
    elif opcion == 5:
        print("haces temblar el piso para desestabilizar al monstruo, la bestia enojada te aplasta con sus patas")
        vida_monstruo = vida_monstruo -25
        vida_personaje -= 100
    elif opcion == 6:
        print("lanzas una fuerte rafaga de aire afilado a la bestia, el monstruo te ataca con una leve zarpada")
        vida_monstruo= vida_monstruo-15
        vida_personaje -= 15
    elif opcion == 7:
        if vida_personaje < 300:
            print("te proteges por un momento escondientote de la bestia, aprovechas ese momento para curarte")
            vida_personaje += 100
        else:
            print("Tu vida esta al maximo")
    elif opcion == 8:
        print("No pudiste escapar, la bestia te ha devorado")
        break
    elif opcion > 8:
        print("Comando no valido")
    elif opcion < 1:
        print("Comando no valido")
    elif vida_personaje <= 0:
        print("Has dado todo en batalla pero el monstruo se mostro victorioso ante ti...")
        break
    elif vida_monstruo <= 0:
        print("la vida del monstruo a caido a 0")
        print("lograste vencer a la bestia que buscaba darte caza.")
print("===FIN DEL JUEGO===")