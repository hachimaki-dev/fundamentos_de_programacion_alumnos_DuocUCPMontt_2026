
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

def agregarLibro():
    tituloValidado = validar_titulo()
    autorValidado = validar_autor()
    ejemplaresValidados = validar_ejemplares()


    print(f"Los datos del libro son X Y Z")

    libroNuevo = {
        "titulo" : tituloValidado,
        "autor" : autorValidado,
        "ejemplares" : ejemplaresValidados,
        "disponible?" : False,
    }
    listaDeLosLibros.append(libroNuevo)

def mostrarLibros():
    print(listaDeLosLibros)


def BuscadorDeLista(NombreDelLibro): # Esta funcion solo se dedicara a recorrer la lista de todos los libros
    for libro in listaDeLosLibros:
        if libro["titulo"] == NombreDelLibro:
            indiceDelLibro = listaDeLosLibros.index(libro)
            return indiceDelLibro
        elif libro["titulo"] != NombreDelLibro and listaDeLosLibros.index(libro) > 2:
            continue
    return

def eliminarLibro():
    libroAEliminar = input("Cual es el libro que desea eliminar?")
    indiceDelLibro = BuscadorDeLista(libroAEliminar)
    if listaDeLosLibros.pop(indiceDelLibro):
        return True


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
                    if indiceDelLibro is not None:
                        print(f"{NombreDelLibro} existe!")
                        print(f"Titulo del libro : {listaDeLosLibros[indiceEncontrado]["titulo"]}")
                        print(f"Nombre del autor : {listaDeLosLibros[indiceEncontrado]["autor"]}")
                        print(f"Cantidad de ejemplares : {listaDeLosLibros[indiceEncontrado]["ejemplares"]}")
                        print(f"Esta disponible? : {listaDeLosLibros[indiceEncontrado]["disponible?"]}")
                    else:
                        print("No existen ejemplares")
            elif selectorDeOpcion == 3:
                nombreDelLibroAEliminar = input("Ingrese el nombre del bicho a eliminar \n[]: ")
            se_elimino = eliminar_bicho(nombreDelLibroAEliminar)
            if se_elimino is not None:
                print(f"{nombreDelLibroAEliminar} existe!")
                print("Se elimino con exito")
            else:
                print("No se puede eliminar algo que no existe")
            elif selectorDeOpcion == 4:
                return
            elif selectorDeOpcion == 5:
                mostrarLibros()
            elif selectorDeOpcion == 6:
                print("Salimos!")
                break
            elif selectorDeOpcion == 7:
                return
        except ValueError:
            print("Valor no aceptado!")

IniciarPrograma()