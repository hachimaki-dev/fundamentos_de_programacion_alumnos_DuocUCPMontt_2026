contador = 0
while True:
    nombre_de_usuario = input("escrine tu nombre de ususario: ")
    contador += 1
    for x in nombre_de_usuario:
        if x == " ":
            print("no se permiten espacios")
            break
    
    if contador < 6:
        print("el numero de carecter minimo es de 6")
    
    print(f"usuario creado {nombre_de_usuario} ")

        







