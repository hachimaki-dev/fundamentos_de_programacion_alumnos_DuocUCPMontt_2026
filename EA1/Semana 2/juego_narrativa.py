#crear un juego de narrativa (de dialogo)
# hola bienvenido cual es tu nombre?

nombre = input("¿Cuál es tu nombre?: ")

print(
    f"===Bienvenidos :D===\n"
    f"Te contaré una historia divertida sisisi\n"
    f"Era una vez un caballero llamado {nombre} que dejó el reino para ir en busqueda de la princesa secuestrada\n"
    f"Después de recorrer largos caminos y cruzar tierras desconocidas, llegó a un misterioso bosque.\n"
    f"El aire era fresco, pero una sensación extraña llenaba el ambiente. Algo no estaba bien...\n"
    f"Había un problema...\n"
    f"🔥 Un dragón gigante 🔥 se cruzó en tu camino\n"
    f"Rápidamente piensas qué hacer:\n"
    f"Esconderme\n"
    f"Enfrentarlo\n"
    f"Moverme con sigilo"
)

movimiento1 = input ("Elige: ")

if movimiento1 == "Esconderme" or movimiento1 == "esconderme" or movimiento1 == "Esconder" or movimiento1 == "esconder":
        print(f"El caballero {nombre} se esconde rápidamente en los arbustos, intentando no ser visto por la criatura.\n"
          f"El dragón pasó cerca de donde te encuentras, y por un momento pensaste que te había visto, pero continuó su camino.\n"
          f"A medida que avanzabas, sentías la presencia del dragón más cerca. Sus pasos resonaban en el suelo, pero nunca llegaba a verte.\n"
          f"Finalmente despues de un tiempo llegaste al castillo, donde encontraste a la princesa...\n"
          f"Te miró con una sonrisa, pero algo en sus ojos te hizo dudar... \n"
          f"Tu misión había terminado... ¿Realmente es una princesa? Fin.")
else: 
    print(f"El caballero {nombre} se fue hacia atrás de la espalda del dragón con un sigilo bastante bueno,\n"
          f"pero no fue suficiente. El dragón se dio cuenta y te atacó antes de que reaccionaras con su cola.\n"
          f"Sales disparado contra una roca, ensangrentado\n
          f"Todo parece... aún más extraño.\n"
          f"Un destello, un cambio rápido, y la visión de la princesa te recibe ante ti. Pero, ¿por qué sientes que ya la habías visto antes?"\n"
          f"Un susurro te pasa por la mente, pero es demasiado tarde para entenderlo. Fin.")
