vida_monstruo=500
print("te perdiste en el bosque, sientes que una vil presencia te esta asechando desde hace un largo rato, vas a revisar el origen del ruido que te lleva acosando. Cuando decides acercarte la bestia se avalanza sobre ti, con un habilidoso movimiento logras esquivarla, ahora solo queda luchar")
while vida_monstruo > 0:
    print(f"vida del jefe {vida_monstruo}")
    print("===Combate===")
    print("1-Atacar con la espada")
    print("2-Usar magia de fuego")
    print("3-Usar magia de hielo")
    print("4-Usar magia de electricidad")
    print("5-Usar magia de tierra")
    print("6-Usar magia de viento")
    print("7-Huir")
    opcion =int(input("Elije: "))    
    if opcion == 1:
        print("Atacas al monstruo con un tajo directo al pecho")
        vida_monstruo = vida_monstruo - 25
    if opcion == 2:
        print("Acatas a la bestia con una bola de fuego en la boca")
        vida_monstruo = vida_monstruo - 50
    if opcion == 3:
        print("lanzasas agua a presion a la bestia en el pecho")
        vida_monstruo = vida_monstruo - 40
    if opcion ==4:
        print("te fuerzas a lanzar punzantes lanzas de hielo al pecho de la bestia")
        vida_monstruo = vida_monstruo - 75
    if opcion == 5:
        print("haces temblar el piso para desestabilizar al monstruo")
        vida_monstruo = vida_monstruo -25
    if opcion == 6:
        print("lanzas una fuerte rafaga de aire afilado a la bestia")
        vida_monstruo= vida_monstruo-15
    if opcion == 7:
        print("No pudiste escapar la bestia te ha devorado")
        break
    if vida_monstruo <= 0:
        print("la vida del monstruo a caido a 0")
        print("lograste vencer a la bestia que buscaba darte caza.")
print("===FIN DEL JUEGO===")