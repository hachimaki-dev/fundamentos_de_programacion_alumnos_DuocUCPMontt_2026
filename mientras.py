#Asignamos las variables del codigo

estoy_haciendo_un_pedido = True
escogiendo_ingredientes = False

#Ponemos un while para que se cree un bucle y le agregamos una interfaz

while estoy_haciendo_un_pedido :
    print("Que desea pedir")

    print(".1 Pizza ")
    print(".2 Hamburguesas ")
    print(".3 Papitas")
    print(".0 Terminar el pedido")

#Agregamos una nueva variable para guardar la eleccion como número entero

    opcion_comida = int(input(""))
    
#Mostramos diferentes opciones dependiendo de la eleccion
    if opcion_comida == 1 :
        print("Escoja los ingredientes")
        escogiendo_ingredientes = True

        while escogiendo_ingredientes :
            print(".1 Extra queso")
            print(".2 Peperoni")
            print(".3 picante")
            print(".0 Terminar de escojer ingredientes")

            opcion_ingredientes = int(input(""))

            if opcion_ingredientes == 0 :
                print("")
                escogiendo_ingredientes = False
    if opcion_comida == 2 :
        print("Escoja los ingredientes")
        escogiendo_ingredientes = True

        while escogiendo_ingredientes :
            print(".1 italiana")
            print(".2 Con queso")
            print(".3 Vegana")
            print(".0 Terminar de escojer ingredientes")

            opcion_ingredientes = int(input(""))

            if opcion_ingredientes == 0 :
                print("")
                escogiendo_ingredientes = False
    
    if opcion_comida == 3 :
        print("Escoja los ingredientes")
        escogiendo_ingredientes = True

        while escogiendo_ingredientes :
            print(".1 Con salchcicha")
            print(".2 Con queso")
            print(".3 Con palta")
            print(".0 Terminar de escojer ingredientes")

            opcion_ingredientes = int(input(""))

            if opcion_ingredientes == 0 :
                print("")
                escogiendo_ingredientes = False
        
    if opcion_comida == 0 :
        estoy_haciendo_un_pedido = False

print("************************")
print("*****Fin del pedido*****")
print("************************")