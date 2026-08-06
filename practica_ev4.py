lista_alumnos = []

def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1.- Agregar registro")
    print("2.- Buscar registro")
    print("3.- Eliminar registro")
    print("4.- Actualizar estados")
    print("5.- Mostrar registros")
    print("6.- Salir")
    print("====================================\n")

def validar_nota():
    try:
        nota_alumno = float(input("Ingrese nota del alumno: "))
    except ValueError:
        print("ERROR, ingrese un numero entre 1.0 y 7.0")
    
    if nota_alumno < 0 or nota_alumno > 7.0:
        print("Ingrese una nota valida!")
    else:
        print("Nota registrada con exito!")
        return nota_alumno

def agregar_registro():
    nombre_alumno = input("Ingrese el nombre a registrar: ")
    asignatura_alumno = input("Ingrese la asignatura del alumno: ")
    nota_validada = validar_nota()

    datos_alumnos = {
        "nombre_alumno" : nombre_alumno,
        "asignatura_alumno" : asignatura_alumno,
        "nota_alumno" : nota_validada,
        "estado" : False
    }

    lista_alumnos.append(datos_alumnos)

def buscar_registro():
    alumno_buscado = input("Ingrese nombre del alumno a buscar: ")

    for alumno in lista_alumnos:
        if alumno["nombre_alumno"] == alumno_buscado:
            print(f"Alumno {alumno["nombre_alumno"]} encontrado!")
        else:
            print("No se ha encontrado a ningun alumno con ese nombre")