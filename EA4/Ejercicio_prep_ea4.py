lista_bichos = []
def mayorQueCero(pregunta):
    while True:        
        try:
            numero = int(input(pregunta))
            if numero > 0:
                return numero
            else:
                print("el numero debe de ser mayor que cero")
        except ValueError:
            print("el valor debe de ser un numero")
def printearMenu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar bicho \n2. Buscar bicho\n3. Eliminar bicho\n4. Actualizar estados\n5. Mostrar bichos\n6. Salir")
    print("=====================================")
def preguntaUsuario():
    eleccionescorrectas = ["1","2","3","4","5","6"]
    while True:
        pregunta = input("escoja una opcion: ")
        if pregunta not in eleccionescorrectas:
            print("escoja una opcion valida")
        else:
            return pregunta
def validacionEspecie():
    while True:
        texto2 = input("defina la especie:\n")
        if texto2.isspace() or texto2 == "":
            print("el texto no debe de contener espacios o ser solo espacios")
        else:
            return texto2
def validacionPeligrosidad(pregunta):
    while True:   
        try:
            numero = float(input(pregunta))
            if 1.0 <= numero and numero <= 10.0:
                return numero
            else:
                print("tiene que ser un numero mayor qUe 1.0 y menoR que 10.0")
        except ValueError:
            print("tiene que ser un numero")
def agregarBicho(lista):
    #especie = str
    #tamaño = int
    #peligrosidad = float
    #peligroso = bool
    especie = validacionEspecie()
    tamaño = mayorQueCero("defina el tamaño:\n")
    peligrosidad = validacionPeligrosidad("defina la peligrosidad:\n")
    peligroso = False
    lista.append({"especie":especie, "tamaño":tamaño, "peligrosidad":peligrosidad, "peligroso":peligroso})
def buscarBicho(lista,bicho):
    bichoencontrado = False
    for i in lista:
        if bicho in i["especie"]:
            bichoencontrado = True
            break
    if bichoencontrado == True:
        return lista.index(i)
    else:
        return -1
def actualizarEstados(lista):
    for i in lista:
        if i.get("peligrosidad") >= 7.0:
            i.update({"peligroso": True})
        else:
            pass
def imprimirBicho(lista,index):
    print(f"Especie: {lista[index].get("especie")}\nTamaño: {lista[index].get("tamaño")}\nPeligrosidad: {lista[index].get("peligrosidad")}\nEs Peligroso?: {lista[index].get("peligroso")} \nSu posicion en la lista de bichos es: {index}")
def mostrarBichos(lista):
    print("=== LISTA DE BICHOS ===")
    for i in range(len(lista)):
        imprimirBicho(lista,i)
        print("********************************************")
def main():
    while True:
        printearMenu()
        respuesta = preguntaUsuario()
        if respuesta == "1":
            agregarBicho(lista_bichos)
        elif respuesta == "2":
            especie = input("ingrese la especie del bicho: ")
            bicho_esta = buscarBicho(lista_bichos,especie)
            if bicho_esta == -1:
                print(f"el bicho {especie} no existe")
            else:
                imprimirBicho(lista_bichos,bicho_esta)
                #buscar bicho
        elif respuesta == "3":
            especie = input("ingrese el bicho a eliminar: ")
            bicho_a_eliminar = buscarBicho(lista_bichos,especie)
            if bicho_a_eliminar == -1:
                print(f"el bicho {especie} no existe")
            else:
                lista_bichos.pop(bicho_a_eliminar)
                print("Bicho eliminado >:3")       
            #eliminar bicho
        elif respuesta == "4":
            actualizarEstados(lista_bichos)
            print("Lista de bichos actualizada utilize la opcion 5 para revisar los datos de peligrosidad actualizados")
            #actualizar estados
        elif respuesta == "5":
            mostrarBichos(lista_bichos)
            #mostrar bichos
        elif respuesta == "6":
            print("Gracias por usar el Cazabichos. ¡Hasta la próxima expedición!")
            break
main()