estudiantes = []
def menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar registro")
    print("2. Buscar registro")
    print("3. Eliminar registro")
    print("4. Actualizar estados")
    print("5. Mostrar registros")
    print("6. Salir")
    print("=====================================")

def opcion_usuario():
    while True:
            opcion_elegida_usuario = input("ingresa una opcion del (1 al 6) :\n")
            if opcion_elegida_usuario in ["1","2","3","4","5","6"]:
                return opcion_elegida_usuario
            else:
                print("opcion invalida, intenta nuevamente ")

#"nombre" Nombre del estudiante No vacío ni solo espacios en blanco
def validacion_nombre_estudiante():
    while True:
        opcion_usuario_nombre_estudiante = input("ingresa el nombre del estudiante\n").strip()
        if " " in opcion_usuario_nombre_estudiante or len(opcion_usuario_nombre_estudiante) <=0:
            print("ingresa el nombre del usuario sin espacios ni la casilla en blanco")
        else:
            return opcion_usuario_nombre_estudiante
                

#"asignatura"Nombre de la asignatura No vacío ni solo espacios en blanco
def validacion_nombre_asignatura():
    while True:
        opcion_usuario_nombre_asignatura =input("ingresa el nombre de la asignatura: \n").strip()
        if " "in opcion_usuario_nombre_asignatura or len(opcion_usuario_nombre_asignatura) <=0:
            print("ingresa el nombre de la asignatura sin espacios ni la casilla en blanco")
        else:
            return opcion_usuario_nombre_asignatura

#"nota" Calificación obtenida Número decimal entre 1.0 y 7.0 inclusive
def validacion_numero_nota():
    while True:
            try:
                opcion_usuario_nota_estudiante = float(input("ingresa la nota del estudiante: \n"))
                if opcion_usuario_nota_estudiante <1.0 or opcion_usuario_nota_estudiante > 7.0:
                    print("la nota asignada tiene que ser entre 1.0 y 7.0 ")
                else:
                    return opcion_usuario_nota_estudiante
            except ValueError:
                print("ingresa un numero valido")

def agregar_registro_opcion1():
    nombre_estudiante_validado = validacion_nombre_estudiante()
    nombre_asignatura_validada = validacion_nombre_asignatura()
    numero_nota_validada = validacion_numero_nota()

    datos_estudiantes = {
        "nombre":nombre_estudiante_validado,
        "asignatura":nombre_asignatura_validada,
        "nota":numero_nota_validada,
        "aprobado" : False
    }
    estudiantes.append(datos_estudiantes)
    print(estudiantes)

def iniciar_programa():
    while True:
        menu()
        opcion_menu_elegida = opcion_usuario()

        if opcion_menu_elegida == "1":
            agregar_registro_opcion1()

iniciar_programa()
