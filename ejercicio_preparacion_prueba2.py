listaDeAlumnos = []

def menuPrincipal():
    print("= = = = = = = = = = = = = MENU PRINCIPAL = = = = = = = = = = = = =")
    print("1. Agregar Registro \n2. Buscar Registro \n3. Eliminar Registro \n4. Actualizar Estados \n5. Mostrar Registros \n6. Salir \n7. Debugging (SOLO DESARROLADOR)")
    print("= = = = = = = = = = = = = = = =  = = = = = = = = = = = = = = = = =")

def validar_estudiante():
    while True:
        nombreDelEstudiante = input("Ingrese el nombre del estudiante a agregar \n[]: ")
        if len(nombreDelEstudiante) <= 0 or nombreDelEstudiante.isspace():
            print("El nombre no puede estar vacio!")
            continue
        else:
            return nombreDelEstudiante
def validar_asignatura():
    while True:
        nombreDeLaAsignatura = input("Ingrese el nombre de la asignatura que desea agregar \n[]: ")
        if len(nombreDeLaAsignatura) <= 0 or nombreDeLaAsignatura.isspace():
            print("La asignatura no puede estar vacia!")
        else:
            return nombreDeLaAsignatura
def validar_calificacion():
    while True:
        notaDelEstudiante = float(input("Ingrese la nota que desea registrar (de 1-7!) \n[]: "))
        if notaDelEstudiante < 1.0:
            print("La nota no puede ser menor que 1.0!")
            continue
        elif notaDelEstudiante > 7.0:
            print("La nota no puede superar 7.0!")
        else:
            return notaDelEstudiante

def debugging():
    nuevoEstudiante = {
        "nombre" : "Spiderman",
        "asignatura" : "Matematicas",
        "nota" : 5.0,
        "aprobado" : False
    }
    listaDeAlumnos.append(nuevoEstudiante)
    nuevoEstudiante = {
        "nombre" : "Ellen",
        "asignatura" : "Fundamentos de Programacion",
        "nota" : 6.1,
        "aprobado" : False
    }
    listaDeAlumnos.append(nuevoEstudiante)
    nuevoEstudiante = {
        "nombre" : "Mildred",
        "asignatura" : "Habilidades de Comunicacion",
        "nota" : 3.2,
        "aprobado" : False
    }
    listaDeAlumnos.append(nuevoEstudiante)

def agregarRegistro():
    estudianteValidado = validar_estudiante()
    asignaturaValidada = validar_asignatura()
    calificacionValidada = validar_calificacion()


    print(f"Los datos del estudiante son, el nombre: {estudianteValidado}, la asignatura: {asignaturaValidada} y su nota: {calificacionValidada}.")

    estudianteNuevo = {
        "nombre" : estudianteValidado,
        "asignatura" : asignaturaValidada,
        "nota" : calificacionValidada,
        "aprobado" : False
    }
    listaDeAlumnos.append(estudianteNuevo)

def mostrarEstudiantes():
    print("=== LISTA DE REGISTROS === \n")
    for estudiante in listaDeAlumnos:
        print(f"Nombre : {estudiante["nombre"]}")
        print(f"Asignatura : {estudiante["asignatura"]}")
        print(f"Nota : {estudiante["nota"]}")
        if estudiante["aprobado"] == True:
            print(f"Estado : Aprobado!")
        else:
            print(f"Estado : Reprobado!")
        print("***************************************")


def BuscadorDeLista(nombreDelAlumno):
    for estudiante in listaDeAlumnos:
        if estudiante["nombre"] == nombreDelAlumno:
            indiceDelAlumno = listaDeAlumnos.index(estudiante)
            return indiceDelAlumno
        elif estudiante["nombre"] != nombreDelAlumno and listaDeAlumnos.index(estudiante) > len(listaDeAlumnos):
            continue
    return

def eliminarRegistro(nombreDelRegistroAEliminar):
    indiceDelAlumno = BuscadorDeLista(nombreDelRegistroAEliminar)
    if listaDeAlumnos.pop(indiceDelAlumno):
        return True
    
def actualizarEstados():
    for estudiante in listaDeAlumnos:
        if estudiante["nota"] > 4.0:
            estudiante["aprobado"] = True


def IniciarPrograma():
    while True:
        menuPrincipal()
        try:
            selectorDeOpcion = int(input("\nIngrese el valor que desea \n[]: "))
            if selectorDeOpcion == 1:
                agregarRegistro()
            elif selectorDeOpcion == 2:
                    NombreDelEstudiante = input("Ingrese el nombre del estudiante a buscar \n[]: ")
                    indiceEncontrado = BuscadorDeLista(NombreDelEstudiante)
                    if indiceEncontrado is not None:
                        print(f"{NombreDelEstudiante} existe!")
                        print(f"Estudiante : {listaDeAlumnos[indiceEncontrado]["nombre"]}")
                        print(f"Asignatura : {listaDeAlumnos[indiceEncontrado]["asignatura"]}")
                        print(f"Nota : {listaDeAlumnos[indiceEncontrado]["nota"]}")
                        print(f"Aprobado? : {listaDeAlumnos[indiceEncontrado]["aprobado"]}")
                    else:
                        print("No existen registros")
            elif selectorDeOpcion == 3:
                nombreDelRegistroAEliminar = input("Ingrese el nombre del estudiante a eliminar \n[]: ")
                se_elimino = eliminarRegistro(nombreDelRegistroAEliminar)
                if se_elimino is not None:
                    print(f"{nombreDelRegistroAEliminar} esta registrado!")
                    print("Se elimino con exito")
                else:
                    print("No se puede eliminar algo que no existe")
            elif selectorDeOpcion == 4:
                actualizarEstados()
            elif selectorDeOpcion == 5:
                mostrarEstudiantes()
            elif selectorDeOpcion == 6:
                print("Gracias por usar el sistema. Hasta pronto!")
                break
            elif selectorDeOpcion == 7:
                debugging()
        except ValueError:
            print("Valor no aceptado!")

IniciarPrograma()