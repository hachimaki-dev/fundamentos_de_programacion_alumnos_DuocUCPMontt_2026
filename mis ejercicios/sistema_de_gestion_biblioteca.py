lista_de_los_libros_agregado = []
def menu_a_mostrar():
    print("========== MENÚ PRINCIPAL ==========")
    print("1.Agregar libro")
    print("2.Buscar libro")
    print("3.eliminar libro")
    print("4.Actualizar disponibilidad")
    print("5.Mostrar libros")
    print("6.salir")
def seleccionando_opcion():
    while True:
        opcion_escogida = input("selecione una opcion del 1 al 6: \n")
        if opcion_escogida in ["1","2","3","4","5","6"]:
            return opcion_escogida
        else:
            print("error: opcion invalida")
def iniciando_programa():
    while True:
        menu_a_mostrar()
        opcion_escogida =seleccionando_opcion()
        if opcion_escogida =="1":
            print("1")
        elif opcion_escogida =="2":
            print("2")
        elif opcion_escogida =="3":
            print("3")
        elif opcion_escogida =="4":
            print("4")
        elif opcion_escogida =="5":
            print("5")
        elif opcion_escogida =="6":
            print("salir")
            break
        else:
            print("opcion invalida")
def validando_titulo_del_libro():
    while True:
        titulo_del_libro = input("ingrese el titulo del libro \n")
        if " " in titulo_del_libro or len(titulo_del_libro) <= 0:
            print("error: titulo no debe estar vacio ni solo espacios en blanco")
        else:
            return titulo_del_libro
def validando_autor():
        while True:
            nombre_del_autor = input("ingrese el titulo del libro \n")
            if " " in nombre_del_autor or len(nombre_del_autor) <= 0:
                print("error: titulo no debe estar vacio ni solo espacios en blanco")
            else:
                return nombre_del_autor
def validando_ejemplares():
    while True:
        try:
            cantidad_de_copias_disponibles = int(input("ingrese la cantidad de copias del libro\n"))
            if cantidad_de_copias_disponibles >= 0:
                return cantidad_de_copias_disponibles
            else:
                print("dato invalido ingrese numeros enteros mayor o igual a cero")
        except ValueError:
            print("error: ingrese solo numeros porfa")
def agregando_libro():
    titulo_agregado = validando_titulo_del_libro()
    autor_agregado = validando_autor()
    ejemplares_agregados = validando_ejemplares()
    print(f"se agrego el titulo{titulo_agregado}")
    print(f"el autor es = {autor_agregado}")
    print(f"cantidad de copias {ejemplares_agregados}")
    agregando_a_la_lista = {
        "titulo": {titulo_agregado},
        "autor":{autor_agregado},}



iniciando_programa()
