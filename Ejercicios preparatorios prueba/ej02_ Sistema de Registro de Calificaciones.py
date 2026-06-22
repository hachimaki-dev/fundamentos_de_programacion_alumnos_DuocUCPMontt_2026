#Variables necesarias para resolver el ejercicio
registro_calificaciones = []
menu = ['1', '2', '3', '4', '5', '6']

#Aqui van las funciones del programa :p
#Funciones para el menu
def mostrarMenu():
    print("""\n========== MENÚ PRINCIPAL ==========
1. Agregar registro
2. Buscar registro
3. Eliminar registro
4. Actualizar estados
5. Mostrar registros
6. Salir
=====================================""")

def validarOpcion():
    while True:
        opcion = input("Ingresa una opción: ")
        if opcion in menu:
            return opcion
        else:
            print("Ingresa una opción válida")

#Función para agregar registro (haremos una función para cada uno de los datos solicitados)
def validarNombre():
    while True:
        nombre_alumno = input("Ingrese el nombre del estudiante: ").strip()
        if len(nombre_alumno) == 0:
            print("EL nombre del estudiante no puede ser un espacio vacío.")
        else:
            return nombre_alumno

def validarAsignatura():
    while True:
        asignatura = input("Ingrese asignatura: ").lower().strip()
        if len(asignatura) == 0:
            print("La asignatura no puede ser un espacio vacío.")
        else:
            return asignatura

def validarCalificacion():
    while True:
        try: 
            calificacion = float(input("Ingrese calificación del estudiante: "))
            if 1.0 <= calificacion <= 7.0:
                return calificacion
            else:
                print("Las calificaciones deben ser un número entre 1.0 y 7.0")
        except ValueError:
            print("Ingrese una calificación válida.")

def agregarLista(dict):
    registro_calificaciones.append(dict)
    return True

def agregarRegistro():
    nombre = validarNombre()
    asignatura = validarAsignatura()
    calificacion = validarCalificacion()

    registro_estudiante = {
        'Nombre': nombre,
        'Asignatura':asignatura,
        'Calificación':calificacion,
        'Aprobado': False
    }

    agregar = agregarLista(registro_estudiante)
    if agregar == True:
        print("El registro se ha realizado exitosamente.")
        return True
    else:
        print("Ha ocurrido un error inesperado.")
        return False

#Función para buscar
def BuscarXnombre(list, nombre_alumno):
    buscar = nombre_alumno.lower().strip()
    for i in range(len(list)):
        if list[i]['Nombre'].lower() == buscar:
            return i
            
    return -1

#Ahora eliminaremos a un alumno
def eliminarAlumnoXnombre(nombre_alumno):
    indice = BuscarXnombre(registro_calificaciones, nombre_alumno)
    if indice != -1:
        eliminar = registro_calificaciones.pop(indice)
        print(f"Se eliminó a '{eliminar['Nombre']}' existosamente.")
        return True
    else:
        print("Estudiante no se encuentra registrado.")
        return False

#Función para actualizar el estado de los estudiantes
def actualizarEstado(list):
    for i in list:
        if i['Calificación'] >= 4.0:
            i['Aprobado'] = True
        else:
            i['Aprobado'] = False
    print("El registro ha sido actualizado.")

#Mostrar registro
def mostrarRegistro(list):
    if len(list) == 0:
        print("No hay alumnos registrados")
        return

    for i in list:
        if i['Aprobado']:
            estado = "APROBADO"
        else:
            estado = "REPROBADO"

        print(f"Nombre: {i['Nombre']}")
        print(f"Asignatura: {i['Asignatura']}")
        print(f"Calificación: {i['Calificación']}")
        print(f"Estado: {estado}")
        print("*" * 30)

#Aqui va la función main, para iniciar el programa D:
def main():
    while True:
        mostrarMenu()
        opcion_elegida = validarOpcion()
        if opcion_elegida == '6':
            print("\nGracias por usar el sistema. ¡Hasta pronto!")
            break
        
        elif opcion_elegida == '1':
            print("\n========= AGREGAR REGISTRO =========")
            agregarRegistro()

        elif opcion_elegida == '2':
            print("\n========= BUSCAR REGISTRO =========")
            alumno_a_buscar = validarNombre()
            indice = BuscarXnombre(registro_calificaciones, alumno_a_buscar)

            if indice != -1:
                print("Búsqueda exitosa")
                print("--------- RESULTADOS BÚSQUEDA ---------")
                print(f"Nombre: {registro_calificaciones[indice]['Nombre']}")
                print(f"Asignatura: {registro_calificaciones[indice]['Asignatura']}")
                print(f"Calificación: {registro_calificaciones[indice]['Calificación']}")
            else: 
                print("El estudiante no se encuentra registrado")

        elif opcion_elegida == '3':
            print("\n========= ELIMINAR REGISTRO =========")
            alumno_a_eliminar = validarNombre()
            eliminar = eliminarAlumnoXnombre(alumno_a_eliminar)

        elif opcion_elegida == '4':
            print("\n========= ACTUALIZAR ESTADOS =========")
            actualizarEstado(registro_calificaciones)

        elif opcion_elegida == '5':
            print("\n========= MOSTRAR REGISTRO =========")
            mostrarRegistro(registro_calificaciones)

        else:
            print("Ingrese una opción válida")
main()