print ("EL AHORCADO *+*")

frutas = ["manzana", "pera", "sandia", "platano", "frutilla", "arandano", "mango", "melon"]
animales = ["perro", "gato", "conejo", "serpiente", "raton", "pollitos", "camello", "caballo"]

while True:
    eleccion_de_usuario = input("Elija una opcion: frutas o animales: ")
    posicion_palabra_secreta = int(input("Elija un numero del 0 al 7: "))

    if eleccion_de_usuario == "frutas":
        palabra_secreta = frutas[posicion_palabra_secreta]
        respuesta_usuario_frutas = input("ADIVINE LA FRUTA SECRETA: ")

        while True:
            if respuesta_usuario_frutas == palabra_secreta:
                print("EXCELENTE RESPUESTA CORRECTA")
                break
            else:
                print("RESPUESTA INCORRECTA")
                respuesta_usuario_frutas = input("Intente otra vez: ")

    elif eleccion_de_usuario == "animales":
        palabra_secreta = animales[posicion_palabra_secreta]
        respuesta_usuario_animales = input("ADIVINE EL ANIMAL: ")

        while True:
            if respuesta_usuario_animales == palabra_secreta:
                print("EXCELENTE RESPUESTA CORRECTA")
                break
            else:
                print("RESPUESTA INCORRECTA")
                respuesta_usuario_animales = input("Intente otra vez: ")

    salir = input("¿Desea seguir jugando? si / no: ")

    if salir == "no":
        print("Gracias por jugar")
        break 