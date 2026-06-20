lista_de_todos_los_animales = []


def MostrarMenu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Registrar animal")
    print("2. Buscar animal")
    print("3. Eliminar animal")
    print("4. Actualizar alertas")
    print("5. Mostrar animales")
    print("6. Salir")
    print("=====================================")


def OpcionMenuElejida():
    opcion_elejida = input("que opcion quieres elegir: ")
    if opcion_elejida in ["1", "2", "3", "4", "5", "6"]:
        return opcion_elejida
    else:
        print("error eliga una de las 6 opciones")


def RegistrarNombreAnimal():
    while True:
        try:
            NombreAnimal = input("cual es el nombre de su animal: ")
            if len(NombreAnimal.strip()) <= 0:
                print("nombre invalido")
            else:
                return NombreAnimal
        except:
            print("intente de nuevo")


def RegistrarEspecieAnimal():
    while True:
        try:
            EspecieAnimal = input("cual es la especie del animal?: ")
            if len(EspecieAnimal.strip()) <= 0:
                print("especie invalida")
            else:
                return EspecieAnimal
        except:
            print("error")


def PesoAnimal():
    while True:
        try:
            ValorPeso = float(input("cuanto pesa el animal: "))
            if ValorPeso <= 0:
                print("tienes que ser un numero mayor a cero y positivo")
            else:
                return ValorPeso
        except:
            print("es solo numeros positivos y mayores a 0")


def AgregarAnimal():
    NombreValido = RegistrarNombreAnimal()
    EspecieValida = RegistrarEspecieAnimal()
    PesoValido = PesoAnimal()
    AnimalAgregado = {
        "nombre": NombreValido,
        "especie": EspecieValida,
        "peso": PesoValido,
        "alerta": False
    }
    lista_de_todos_los_animales.append(AnimalAgregado)
    print("animal registrado con exito")


def BuscarAnimal(AnimalABuscar):
    for indice, CadaAnimal in enumerate(lista_de_todos_los_animales):
        if CadaAnimal["nombre"] == AnimalABuscar:
            return indice
    return -1


def EliminarAnimal(AnimalABuscar):
    Indice_de_animal = BuscarAnimal(AnimalABuscar)
    if Indice_de_animal == -1:
        print(f"El animal '{AnimalABuscar}' no se encuentra registrado.")
        return False
    lista_de_todos_los_animales.pop(Indice_de_animal)
    return True


def ActualizarPesoDeAnimal():
    for CadaAnimal in lista_de_todos_los_animales:
        if CadaAnimal["peso"] < 3.0:
            CadaAnimal["alerta"] = True
        else:
            CadaAnimal["alerta"] = False


def MostrarTodosLosAnimales():
    print("=== LISTA DE ANIMALES ===")
    for CadaAnimal in lista_de_todos_los_animales:
        estado = "EN ALERTA" if CadaAnimal["alerta"] else "NORMAL"
        print(f"Nombre: {CadaAnimal['nombre']}")
        print(f"Especie: {CadaAnimal['especie']}")
        print(f"Peso: {CadaAnimal['peso']} kg")
        print(f"Estado: {estado}")
        print("*******************************************")


def IniciarPrograma():
    while True:
        MostrarMenu()
        OpcionMenuSeleccionada = OpcionMenuElejida()

        if OpcionMenuSeleccionada == "1":
            AgregarAnimal()

        elif OpcionMenuSeleccionada == "2":
            AnimalABuscar = input("que animal buscas?: ")
            Indice_de_animal = BuscarAnimal(AnimalABuscar)
            if Indice_de_animal != -1:
                print("animal encontrado")
                print(f"Nombre: {lista_de_todos_los_animales[Indice_de_animal]['nombre']}")
                print(f"Especie: {lista_de_todos_los_animales[Indice_de_animal]['especie']}")
                print(f"Peso: {lista_de_todos_los_animales[Indice_de_animal]['peso']}")
                print(f"Alerta: {lista_de_todos_los_animales[Indice_de_animal]['alerta']}")
            else:
                print(f"El animal '{AnimalABuscar}' no se encuentra registrado.")

        elif OpcionMenuSeleccionada == "3":
            AnimalPorEliminar = input("que animal deseas eliminar?: ")
            fue_eliminado = EliminarAnimal(AnimalPorEliminar)
            if fue_eliminado:
                print("animal borrado")

        elif OpcionMenuSeleccionada == "4":
            ActualizarPesoDeAnimal()
            print("alertas actualizadas")

        elif OpcionMenuSeleccionada == "5":
            ActualizarPesoDeAnimal()
            MostrarTodosLosAnimales()

        elif OpcionMenuSeleccionada == "6":
            print("Gracias por usar el sistema. ¡Hasta pronto!")
            break


IniciarPrograma()
