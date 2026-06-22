notas_de_estudiantes_por_asignatura = []
def validacion_nombre():
    while True:
        nombre = input("Ingrese el nombre del estudiante: ").strip()
        if len(nombre) > 0:
            return nombre.lower()
        else:
            print("Error, no puede estar vacio ni tener solo espacios.")
def validacion_asignatura():
    while True:
        asignatura = input("Ingrese la asignatura: ").strip()
        if len(asignatura) > 0:
            return asignatura.lower()
        else:
            print("Error, no puede estar vacio ni tener solo espacios.")
def validacion_nota():
    while True:
        try:
            nota = float(input("Calificaciíon obtenida: "))
        except ValueError:
            print("Error, no puede ser numero negativo, ni tener letras.")
            continue
        if (nota >= 1.0) and (nota <= 7.0):
            return nota
        else:
            print("Error, no puede ser numero negativo, ni tener letras.")
def agregar_registro():
    nombre_estudiante = validacion_nombre()
    asignatura_estudiante = validacion_asignatura()
    calificacion_obtenida = validacion_nota()
    nuevo_estudiante_a_agregar = {"Nombre" : nombre_estudiante, "Asignatura": asignatura_estudiante, "Calificación" : calificacion_obtenida, "Aprobado" : False}
    return notas_de_estudiantes_por_asignatura.append(nuevo_estudiante_a_agregar)
def buscar_registro():
    nombre_estudiante = validacion_nombre()
    for estudiante in notas_de_estudiantes_por_asignatura:
        if estudiante["Nombre"] == nombre_estudiante:
            indice = notas_de_estudiantes_por_asignatura.index(estudiante)
            return indice
        else:
            return -1
def Eliminar_registro():
    estudiante = buscar_registro()
    if estudiante >= 0:
        return notas_de_estudiantes_por_asignatura.pop(estudiante)
    else:
        print("El estudinate no fue encontrado.")
def Actualizacion_aprobado():
    for i in notas_de_estudiantes_por_asignatura:
        if i["Calificación"] >= 4.0:
            i["Aprobado"] = True
        else:
            print("Reprobado")
def Mostrar_registros():
    for i in notas_de_estudiantes_por_asignatura:
        print(f"Nombre: {i["Nombre"]} | Asignatura: {i["Asignatura"]}\nCalificación: {i["Calificación"]} | Aprobado: {i["Aprobado"]}")
def menu_principal():
    print("=== MENU PRINCIPAL ===")
    print("1. Agregar registro\n2. Buscar registro\n3. Eliminar\n4.Actualizar\n5.Mostrar\6.Salir")
def opcion_elegida():
    while True:
        opcion = input("Escoja su opción: ").strip()
        if opcion in ["1", "2", "3", "4", "5", "6"]:
            return opcion
        else:
            print("Error, escoja una opción valida.")
def inicio_del_programa():
    while True:
        menu_principal()
        eleccion_user = opcion_elegida()
        if eleccion_user == "1":
            agregar_registro()
        elif eleccion_user == "2":
            buscar_registro()
        elif eleccion_user == "3":
            Eliminar_registro()
        elif eleccion_user == "4":
            Actualizacion_aprobado()
        elif eleccion_user == "5":
            Mostrar_registros()
        elif eleccion_user == "6":
            print("Gracias por usar el sistema. ¡Hasta pronto!")
            break
        else:
            print("Error, vuelva a escoger una de las opciones.")
inicio_del_programa()