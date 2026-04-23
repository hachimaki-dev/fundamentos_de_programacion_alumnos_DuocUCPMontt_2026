vengadores = []
nombre_avenger = str
opcion_de_destruccion = str
while True:
    print("1. Agregar Avenger")
    print("2. Mostrar Base")
    print("3. Salir")
    opcion_elegida = int(input("Elije una de las opciones (1, 2, 3)"))
    if opcion_elegida == 1:
        nombre_avenger = input("ingresa el nombre del avenger para ingresarlo: ")
        nombre_avenger = vengadores.append(nombre_avenger)
    if opcion_elegida == 2:
        for n in range(len(vengadores)):
            print(vengadores)
            mayus = 0
            mayus = int(input("Presione 1 para poner los nombres en mayuscula o 0 para salir: "))
            if mayus == 1:
                vengadores[n] = vengadores[n].upper()
                print(vengadores)
    if opcion_elegida == 3:
        print("has salido del programa")
        break
    if opcion_elegida == 00:
        print("has elegido la opcion secreta")
        opcion_de_destruccion = input("escriba aqui la palabra clave: ")
        if opcion_de_destruccion == "Sacrificar":
            vengadores.pop()
            print("operacion realizada con exito")
