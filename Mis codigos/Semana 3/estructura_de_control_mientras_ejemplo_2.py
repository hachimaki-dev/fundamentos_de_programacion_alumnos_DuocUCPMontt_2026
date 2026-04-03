condicion = True

while condicion == True :
    print("Bienvenido, elija una opción")
    print("1. Contar chiste")
    print("2. Contar adiviniza")
    print("3. Salir")

    opcion_elegida = int(input("Elige una opción: "))

    if opcion_elegida == 1 :
        print("Contamos los chistes guapo")
    if opcion_elegida == 2 :
        print("Contamos las adivinanzas")
    if opcion_elegida == 3 :
        condicion = False

print (f"la condicion a cambiado a {condicion}")
