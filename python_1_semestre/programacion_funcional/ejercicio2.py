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
            print("ingresa el nombre del usuario no puede tener espacios ni la casilla en blanco")
        else:
            return opcion_usuario_nombre_estudiante
                

#"asignatura"Nombre de la asignatura No vacío ni solo espacios en blanco
def validacion_nombre_asignatura():
    while True:
        opcion_usuario_nombre_asignatura =input("ingresa el nombre de la asignatura: \n").strip()
        if " "in opcion_usuario_nombre_asignatura or len(opcion_usuario_nombre_asignatura) <=0:
            print("ingresa el nombre de la asignatura  no puede tener espacios ni la casilla en blanco")
        else:
            return opcion_usuario_nombre_asignatura

#"nota" Calificación obtenida Número decimal entre 1.0 y 7.0 inclusive
def validacion_numero_nota():
    while True:
            try:
                opcion_usuario_nota_estudiante = float(input("ingresa la nota del estudiante: \n"))
                if opcion_usuario_nota_estudiante <1.0 or opcion_usuario_nota_estudiante > 7.0:
                    print("la nota asignada tiene que ser entre 1.0 y 7.0 con decimal ")
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
    

def buscar_registro_estudiante_opcion2(lista_estudiantes,nombre_busqueda_estudiantes):
    if not nombre_busqueda_estudiantes : 
        return -1
    for pocicion_estudiante in range(len(lista_estudiantes)):
        if lista_estudiantes[pocicion_estudiante]["nombre"].lower() == nombre_busqueda_estudiantes.lower():
            return pocicion_estudiante
        
    return -1

def buscar_estudiante_por_nombre():
    nombre_estudiante_busqueda = input("ingresa el nombre del estudiante a buscar ; \n").strip()
    if " " in nombre_estudiante_busqueda or len(nombre_estudiante_busqueda) <=0:
        print("intenta nuevamente , no dejes la casilla en blanco y el nombre sin espacios")
    else:
        return nombre_estudiante_busqueda

def actualizar_datos(lista_alumnos):
    for estudiante in estudiantes:
        if estudiante["nota"] >= 4.0:
            estudiante["aprobado"] = True
            

        
def iniciar_programa():
    while True:
        menu()
        opcion_menu_elegida = opcion_usuario()

        if opcion_menu_elegida == "1":
            agregar_registro_opcion1()

        elif opcion_menu_elegida == "2":
            nombre_estudiante_a_buscar = buscar_estudiante_por_nombre()
            indice_estudiante_entontrado = buscar_registro_estudiante_opcion2(estudiantes,nombre_estudiante_a_buscar)
            if indice_estudiante_entontrado != -1:
                print (f" estudiante encontrado en la posicion : {indice_estudiante_entontrado}")
            

        elif opcion_menu_elegida == "3":
            nombre_ingresado_para_eliminar = buscar_estudiante_por_nombre()
            nombre_encontrado_para_eliminar = buscar_registro_estudiante_opcion2(estudiantes,nombre_ingresado_para_eliminar)
            if nombre_encontrado_para_eliminar != -1:
                estudiantes.pop(nombre_encontrado_para_eliminar)
            else:
                print(f"El registro de {nombre_ingresado_para_eliminar} no se encuentra en el sistema")

        elif opcion_menu_elegida == "4":
            actualizar_el_estado_de_estudiantes = actualizar_datos(estudiantes)

        elif opcion_menu_elegida == "5":
            print("=== LISTA DE REGISTROS ===")
            for estudiante in estudiantes:
                if estudiante ["aprobado"] == True:
                    estudiante["aprobado"] = "aprobado"
                else:
                    estudiante["aprobado"] = "reprobado"

                print(f"Nombre : {estudiante["nombre"]}")
                print(f"Asignatura: {estudiante["asignatura"]}")
                print(f"Nota:{estudiante["nota"]}")
                print(f"Estado:{estudiante["aprobado"]}")
                print("*******************************************")
                
        elif opcion_menu_elegida == "6":
            print("Gracias por usar el sistema. ¡Hasta pronto!")
            break

iniciar_programa()
