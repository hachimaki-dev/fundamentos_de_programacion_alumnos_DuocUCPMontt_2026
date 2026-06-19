
listaDeLosLibros = []

def menuPrincipal():
    print("= = = = = = = = = = = = = MENU PRINCIPAL = = = = = = = = = = = = =")
    print("1. Agregar Libro \n2. Buscar Libro \n3. Eliminar Libro \n4. Actualizar Disponibilidad \n5. Mostrar Libros \n6. Salir \n7. Debugging (SOLO DESARROLADOR)")
    print("= = = = = = = = = = = = = = = =  = = = = = = = = = = = = = = = = =")

def validar_titulo():
    while True:
        tituloDelLibro = input("Ingrese el titulo del libro que desea agregar \n[]: ")
        if len(tituloDelLibro) <= 0 or tituloDelLibro.isspace():
            print("El titulo no puede estar vacio!")
            continue
        else:
            return tituloDelLibro
def validar_autor():
    while True:
        autorDelLibro = input("Ingrese el autor del libro que desea agregar \n[]: ")
        if len(autorDelLibro) <= 0 or autorDelLibro.isspace():
            print("El autor no puede estar vacio!")
        else:
            return autorDelLibro
def validar_ejemplares():
    while True:
        numeroDeEjemplares = int(input("Ingrese la cantidad de ejemplares que desea registrar \n[]: "))
        if numeroDeEjemplares < 0:
            print("La cantidad de ejemplares a registrar no puede ser menor a cero!")
            continue
        else:
            return numeroDeEjemplares

def debugging():
    nuevoLibro = {
        "titulo" : "En la montaña de la locura",
        "autor" : "HP Lovecraft",
        "ejemplares" : 5,
        "disponible?" : False
    }
    listaDeLosLibros.append(nuevoLibro)
    nuevoLibro = {
        "titulo" : "Don Quijote",
        "autor" : "Miguel de Cervantes",
        "ejemplares" : 0,
        "disponible?" : False
    }
    listaDeLosLibros.append(nuevoLibro)
    nuevoLibro = {
        "titulo" : "No Longer Human",
        "autor" : "Osamu Dazai",
        "ejemplares" : 12,
        "disponible?" : False
    }
    listaDeLosLibros.append(nuevoLibro)

def agregarLibro():
    tituloValidado = validar_titulo()
    autorValidado = validar_autor()
    ejemplaresValidados = validar_ejemplares()


    print(f"Los datos del libro son X Y Z")

    libroNuevo = {
        "titulo" : tituloValidado,
        "autor" : autorValidado,
        "ejemplares" : ejemplaresValidados,
        "disponible?" : False
    }
    listaDeLosLibros.append(libroNuevo)

def mostrarLibros():
    print("=== LISTA DE LIBROS === \n")
    for libro in listaDeLosLibros:
        print(f"Titulo : {libro["titulo"]}")
        print(f"Autor : {libro["autor"]}")
        print(f"Ejemplares : {libro["ejemplares"]}")
        if libro["disponible?"] == True:
            print(f"Estado : Disponible!")
        else:
            print(f"Estado : Sin ejemplares")
        print("***************************************")


def BuscadorDeLista(NombreDelLibro): # Esta funcion solo se dedicara a recorrer la lista de todos los libros
    for libro in listaDeLosLibros:
        if libro["titulo"] == NombreDelLibro:
            indiceDelLibro = listaDeLosLibros.index(libro)
            return indiceDelLibro
        elif libro["titulo"] != NombreDelLibro and listaDeLosLibros.index(libro) > 2:
            continue
    return

def eliminarLibro(nombreDelLibroAEliminar):
    indiceDelLibro = BuscadorDeLista(nombreDelLibroAEliminar)
    if listaDeLosLibros.pop(indiceDelLibro):
        return True
    
def actualizarDisponibilidadDeLibro():
    for libro in listaDeLosLibros:
        if libro["ejemplares"] > 0:
            libro["disponible?"] = True


def IniciarPrograma():
    while True:
        menuPrincipal()
        try:
            selectorDeOpcion = int(input("\nIngrese el valor que desea \n[]: "))
            if selectorDeOpcion == 1:
                agregarLibro()
            elif selectorDeOpcion == 2:
                    NombreDelLibro = input("Ingrese el titulo del libro a buscar \n[]: ")
                    indiceEncontrado = BuscadorDeLista(NombreDelLibro)
                    if indiceEncontrado is not None:
                        print(f"{NombreDelLibro} existe!")
                        print(f"Titulo del libro : {listaDeLosLibros[indiceEncontrado]["titulo"]}")
                        print(f"Nombre del autor : {listaDeLosLibros[indiceEncontrado]["autor"]}")
                        print(f"Cantidad de ejemplares : {listaDeLosLibros[indiceEncontrado]["ejemplares"]}")
                        print(f"Esta disponible? : {listaDeLosLibros[indiceEncontrado]["disponible?"]}")
                    else:
                        print("No existen ejemplares")
            elif selectorDeOpcion == 3:
                nombreDelLibroAEliminar = input("Ingrese el nombre del libro a eliminar \n[]: ")
                se_elimino = eliminarLibro(nombreDelLibroAEliminar)
                if se_elimino is not None:
                    print(f"{nombreDelLibroAEliminar} existe!")
                    print("Se elimino con exito")
                else:
                    print("No se puede eliminar algo que no existe")
            elif selectorDeOpcion == 4:
                actualizarDisponibilidadDeLibro()
            elif selectorDeOpcion == 5:
                mostrarLibros()
            elif selectorDeOpcion == 6:
                print("Salimos!")
                break
            elif selectorDeOpcion == 7:
                debugging()
        except ValueError:
            print("Valor no aceptado!")

IniciarPrograma()