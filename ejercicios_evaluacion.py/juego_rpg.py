vida_jugador = 100
mana_jugador = 20 
vida_jefe_final = 150 
print("bienvenido jugador!! has llegado hasta el final de tu recorrido\ny ya es hora de que te enfrestes al jefe final")
nombre_jugador = input("cual es tu nombre queridisimo jugador?")
print(f"bien {nombre_jugador} ahora te enfrentaras con el terrorifico jefe de las profundidades del abismo")
print(f"dispones de 20 de mana y 100 de vida, aprovechalos bien y mucha suerte {nombre_jugador} !!")
opcion_de_ataque = 0
print("***batalla final!!***")
print(f"la vida del jefe es de {vida_jefe_final}")
while vida_jefe_final and vida_jugador > 0:
    print("1. Atacar: esta accion le quita 20 de vida al jefe")
    print("2. Usar magia: esta accion quita 50 de vida al jefe y gasta 5 de mana")
    print("3. Pocion de curacion: te cura 30 de vida GASTA TODO TU MANA RESTANTE!!")
    opcion_de_ataque = int(input("elige una de las opciones de ataque(1, 2, 3):"))
    if opcion_de_ataque == 1 and vida_jefe_final != 0:
        vida_jefe_final = vida_jefe_final - 20
        print(f"Le has quitado 20 de vida al jefe!! ahora esta en {vida_jefe_final}")
        if vida_jefe_final != 0:
            vida_jugador = vida_jugador - 15
            print(f"ahora el jefe te ataca y tu vida es de {vida_jugador} ")
    if opcion_de_ataque == 2 and mana_jugador > 5 and vida_jefe_final != 0:
        vida_jefe_final = vida_jefe_final - 50
        print(f"le diste!! ahora la vida del jefe es de {vida_jefe_final} ")
        mana_jugador = mana_jugador - 5
        print(f"ahora tu mana es de {mana_jugador} ")
        if vida_jefe_final != 0:
            vida_jugador = vida_jugador - 15
            print(f"el jefe te ataco y ahora tu vida es: {vida_jugador} ")
    if opcion_de_ataque == 3 and mana_jugador != 0 and vida_jefe_final != 0:
        vida_jugador = vida_jugador + 30
        print(f"felicidades!! ahora tu vida es de {vida_jugador} ")
        mana_jugador = mana_jugador - mana_jugador
        print(f"pero ahora tu mana es de {mana_jugador}")
        if vida_jefe_final != 0:
            vida_jugador = vida_jugador - 15
            print(f"el jefe te golpeo!! ahora tu vida es de {vida_jugador}")
        else:
            print(f"no tienes mana suficiente, tu mana esta en {mana_jugador}")
            print("elige una de las opciones validas")            
    if vida_jefe_final == 0:
        print(f"Felicidadeees!!! has derrotado al jefe!!! gracias {nombre_jugador}")
        break 
    if vida_jugador == 0:
        print(f"lo lamentamos {nombre_jugador} estas muerto...")
        break