print("EL AHORCADO *v*")



frutas = ["manzana", "pera", "sandia", "platano","frutilla", "arandano", "mango", "melon"]
animales = ["perro", "gato", "conejo", "serpiente", "raton", "pollitos", "camello", "caballo"]
  
while True:
    eleccion_de_usuario = input("¿eliga una opcion?: frutas o animales ")
    posicion_palabra_secreta = int(input("eliga un numero del 0 al 7"))
    if eleccion_de_usuario == "frutas":
        palabra_secreta = frutas[posicion_palabra_secreta]
        respuesta_usuario_frutas = input("ADIVINE LA FRUTA SECRETA")
        while True:
            if respuesta_usuario_frutas == palabra_secreta:
                print("EXCELENTE RESPUESTA CORRECTA")
                break

            elif respuesta_usuario_frutas != palabra_secreta:
                print("RESPUESTA INCORRECTA")
                
    elif eleccion_de_usuario == "animales":
        print("ADIVINE EL ANIMAL")
        palabra_secreta = animales[posicion_palabra_secreta]



