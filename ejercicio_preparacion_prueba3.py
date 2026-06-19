listaDeAnimales = []

def menuPrincipal():
    print("= = = = = = = = = = = = = MENU PRINCIPAL = = = = = = = = = = = = =")
    print("1. Registrar Animal \n2. Buscar Animal \n3. Eliminar Animal \n4. Actualizar Alertas \n5. Mostrar Animales \n6. Salir \n7. Debugging (SOLO DESARROLADOR)")
    print("= = = = = = = = = = = = = = = =  = = = = = = = = = = = = = = = = =")

def validarNombre():
    while True:
        nombreDelAnimal = input("Ingrese el nombre del animal a registrar \n[]: ")
        if len(nombreDelAnimal) <= 0 or nombreDelAnimal.isspace():
            print("El nombre no puede estar vacio!")
            continue
        else:
            return nombreDelAnimal
def validarEspecie():
    while True:
        especieDelAnimal = input("Ingrese la especie del animal \n[]: ")
        if len(especieDelAnimal) <= 0 or especieDelAnimal.isspace():
            print("La especie no puede estar vacia!")
        else:
            return especieDelAnimal
def validarPeso():
    while True:
        pesoDelAnimal = float(input("Ingrese el peso del animal que desea registrar (de 1-7!) \n[]: "))
        if pesoDelAnimal < 0:
            print("El peso no puede ser menor que 0!")
            continue
        else:
            return pesoDelAnimal

def debugging():
    nuevoAnimal = {
        "nombre" : "Mr Wellingbeard the Third of Yorkertown",
        "especie" : "Perro",
        "peso" : 3.2,
        "alerta" : False
    }
    listaDeAnimales.append(nuevoAnimal)
    nuevoAnimal = {
        "nombre" : "Galaghaz el Destructor",
        "especie" : "Gato",
        "peso" : 2.6,
        "alerta" : False
    }
    listaDeAnimales.append(nuevoAnimal)
    nuevoAnimal = {
        "nombre" : "George",
        "especie" : "Hamster",
        "peso" : 1.8,
        "alerta" : False
    }
    listaDeAnimales.append(nuevoAnimal)

def agregarRegistro():
    nombreValidado = validarNombre()
    especieValidada = validarEspecie()
    pesoValidado = validarPeso()


    print(f"Los datos del animal son, el nombre: {nombreValidado}, la especie: {especieValidada} y su peso: {pesoValidado}.")

    estudianteNuevo = {
        "nombre" : nombreValidado,
        "especie" : especieValidada,
        "peso" : pesoValidado,
        "alerta" : False
    }
    listaDeAnimales.append(estudianteNuevo)

def mostrarAnimales():
    print("=== LISTA DE REGISTROS === \n")
    for animal in listaDeAnimales:
        print(f"Nombre : {animal["nombre"]}")
        print(f"Especie : {animal["especie"]}")
        print(f"Peso : {animal["peso"]}")
        if animal["alerta"] == True:
            print(f"Estado : En Alerta!")
        else:
            print(f"Estado : Normal!")
        print("***************************************")


def BuscadorDeLista(nombreDelAnimal):
    for animal in listaDeAnimales:
        if animal["nombre"] == nombreDelAnimal:
            indiceDelAnimal = listaDeAnimales.index(animal)
            return indiceDelAnimal
        elif animal["nombre"] != nombreDelAnimal and listaDeAnimales.index(animal) > len(listaDeAnimales):
            continue
    return

def eliminarRegistro(nombreDelRegistroAEliminar):
    indiceDelAnimal = BuscadorDeLista(nombreDelRegistroAEliminar)
    if listaDeAnimales.pop(indiceDelAnimal):
        return True
    
def actualizarEstados():
    for animal in listaDeAnimales:
        if animal["peso"] > 3.0:
            animal["alerta"] = True


def IniciarPrograma():
    while True:
        menuPrincipal()
        try:
            selectorDeOpcion = int(input("\nIngrese el valor que desea \n[]: "))
            if selectorDeOpcion == 1:
                agregarRegistro()
            elif selectorDeOpcion == 2:
                    nombreDelAnimal = input("Ingrese el nombre del animal a buscar \n[]: ")
                    indiceEncontrado = BuscadorDeLista(nombreDelAnimal)
                    if indiceEncontrado is not None:
                        print(f"{nombreDelAnimal} existe!")
                        print(f"Animal : {listaDeAnimales[indiceEncontrado]["nombre"]}")
                        print(f"Especie : {listaDeAnimales[indiceEncontrado]["especie"]}")
                        print(f"Peso : {listaDeAnimales[indiceEncontrado]["peso"]}")
                        print(f"Estado : {listaDeAnimales[indiceEncontrado]["alerta"]}")
                    else:
                        print("No existen registros")
            elif selectorDeOpcion == 3:
                nombreDelRegistroAEliminar = input("Ingrese el nombre del animal a eliminar \n[]: ")
                se_elimino = eliminarRegistro(nombreDelRegistroAEliminar)
                if se_elimino is not None:
                    print(f"{nombreDelRegistroAEliminar} esta registrado!")
                    print("Se elimino con exito")
                else:
                    print("No se puede eliminar algo que no existe")
            elif selectorDeOpcion == 4:
                actualizarEstados()
            elif selectorDeOpcion == 5:
                mostrarAnimales()
            elif selectorDeOpcion == 6:
                print("Salimos!")
                break
            elif selectorDeOpcion == 7:
                debugging()
        except ValueError:
            print("Gracias por usar el sistema. Hasta pronto!")

IniciarPrograma()